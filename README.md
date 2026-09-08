# Zeta.skills

Zeta 是一只萌系 Q 版水豚 Codex 桌宠：戴黑色墨镜、穿黑色 Zeta 连帽卫衣和粉色短裤。

这个仓库只有一个技能：`zeta-moyu`。它负责安装或恢复 Zeta，然后陪你摸鱼；没有任务管理、提醒、研究或其他附加功能。

## 直接安装

把下面这条消息发给 Codex：

```text
$skill-installer https://github.com/Jray937/Zeta.skills/tree/main/zeta-moyu
```

安装完成后的下一轮调用：

```text
$zeta-moyu 帮我配置 Zeta，然后陪我摸鱼
```

第一次配置会把随包的 `pet.json` 和 `spritesheet.webp` 安装到 `~/.codex/pets/zeta/`。如果 Codex 已打开，请重新选择 Zeta 或重启 Codex。

也可以直接下载仓库根目录的 `zeta-moyu.skill` 技能包。

## 鼠标动作

- Hover：Zeta 喊“存为王”。
- 左右拖拽：Zeta 喊“存为亡”。
- 拖拽动作行中不包含原来的跑步角色，因此不会发生动画重叠。

## 仓库结构

```text
zeta-moyu/
├── SKILL.md
├── agents/openai.yaml
├── scripts/install_zeta.py
└── assets/pet/
    ├── pet.json
    └── spritesheet.webp
```
