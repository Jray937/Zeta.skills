#!/usr/bin/env python3
"""Install the bundled Zeta pet into the current user's Codex pet directory."""

from __future__ import annotations

import hashlib
import json
import shutil
import argparse
from datetime import datetime, timezone
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
PET_SOURCE = SKILL_DIR / "assets" / "pet"
REQUIRED_FILES = ("pet.json", "spritesheet.webp")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path.home() / ".codex" / "pets" / "zeta",
        help="Override the destination directory (primarily for validation).",
    )
    args = parser.parse_args()
    pet_destination = args.destination.expanduser().resolve()

    missing = [name for name in REQUIRED_FILES if not (PET_SOURCE / name).is_file()]
    if missing:
        raise SystemExit(f"Zeta skill package is incomplete: missing {', '.join(missing)}")

    pet_config = json.loads((PET_SOURCE / "pet.json").read_text(encoding="utf-8"))
    if pet_config.get("id") != "zeta" or pet_config.get("spritesheetPath") != "spritesheet.webp":
        raise SystemExit("Bundled pet.json does not describe the Zeta asset")

    desired = {name: sha256(PET_SOURCE / name) for name in REQUIRED_FILES}
    installed = {
        name: sha256(pet_destination / name)
        for name in REQUIRED_FILES
        if (pet_destination / name).is_file()
    }

    if installed == desired:
        print(json.dumps({"ok": True, "status": "already-installed", "path": str(pet_destination)}))
        return

    if pet_destination.exists() and installed:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = pet_destination.with_name(f"zeta.backup-{stamp}")
        shutil.copytree(pet_destination, backup)
    else:
        backup = None

    pet_destination.mkdir(parents=True, exist_ok=True)
    for name in REQUIRED_FILES:
        shutil.copy2(PET_SOURCE / name, pet_destination / name)

    actual = {name: sha256(pet_destination / name) for name in REQUIRED_FILES}
    if actual != desired:
        raise SystemExit("Zeta installation checksum verification failed")

    print(json.dumps({"ok": True, "status": "installed", "path": str(pet_destination), "backup": str(backup) if backup else None}))


if __name__ == "__main__":
    main()
