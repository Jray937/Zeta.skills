---
name: zeta-moyu
description: Install or restore the bundled Zeta Codex pet, then help the user take a harmless break. Use when the user asks to configure Zeta, install the Zeta pet, 摸鱼, 放空, or take a short break. Do not use for productivity workflows or unrelated pet creation.
---

# Zeta 摸鱼

This skill has one job: make sure the bundled Zeta pet is installed, then accompany the user while they 摸鱼.

## Configure Zeta

At the first invocation, or whenever the user asks to repair or restore Zeta, run:

```bash
python3 scripts/install_zeta.py
```

Run it from this skill directory. The script verifies the bundled files, backs up a different existing Zeta installation, and copies the pet to `~/.codex/pets/zeta/`. If the sandbox blocks that destination, request narrowly scoped write permission for that directory and retry.

After installation, tell the user to reselect Zeta or restart Codex if the app is already open. Do not claim that the pet is active unless the UI was actually verified.

Zeta's interaction mapping is intentionally unusual:

- Hover plays “存为王”.
- Dragging left or right plays “存为亡”.
- The original directional running artwork is absent from the drag rows.

## 摸鱼

After Zeta is configured, keep the interaction light. Offer one short, playful line inviting the user to breathe, stretch, drink water, stare into space, or enjoy a brief break with Zeta. Do not create tasks, reminders, plans, reports, research, or other productivity features unless the user separately asks for them outside this skill.
