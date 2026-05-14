# Default Style System

在用户没有指定品牌风格时，优先使用这套默认风格。它来自用户提供的文章案例图：暖中性色、窗口式容器、细边框、serif 标题、mono 标签、克制的 clay/olive/sky 强调色。

## 资产

- 默认 CSS：`assets/styles/warm-neutral-artifact.css`
- HTML 外壳模板：`assets/templates/artifact-template.html`
- 单文件合成脚本：`scripts/build_artifact.py`
- 案例图：
  - `assets/examples/eight-capabilities.svg`
  - `assets/examples/markdown-vs-html.svg`
  - `assets/examples/tuning-interface.svg`
  - `assets/examples/code-review-annotations.svg`
  - `assets/examples/design-tokens.svg`
  - `assets/examples/config-editor.svg`

这些 SVG 是根据文章截图重绘的案例示意图，不依赖外部图片。生成单文件 HTML 时，可将 SVG 内容内联到页面，或在多文件预览/skill 文档中用 `<img>` 引用。

## 风格关键词

- Warm neutral background: `#FAF8F5`
- Surface: `#F0EDE8`
- Border: `#D4CFC7`
- Text: `#2C2825`
- Accent clay: `#D97757`
- Olive: `#788C5D`
- Sky: `#6A8CAF`
- Slate/code: `#141413`

## 默认版式

1. 用 editorial hero 呈现标题、中心观点和阅读路径。
2. 用 sticky/compact 目录提供章节跳转。
3. 用 `.hav-window` 表达浏览器窗口、代码窗口、控制台或编辑器。
4. 用 `.hav-card` / `.hav-feature-card` 表达概念组，不要嵌套卡片。
5. 用 SVG 表达流程、关系、矩阵、diff 注释和界面示意。
6. 用 `.hav-code` 表达代码、配置、提示词或导出结果。
7. 用 `.hav-button` 做复制、导出、切换和选择动作。

## 嵌入方式

当生成单文件 HTML 时：

1. 本机创建文件时，优先生成正文 HTML fragment，再用 `scripts/build_artifact.py` 注入统一 CSS、外壳、基础 JS 和可选 SVG。
2. 如果用户要求直接输出完整 HTML 代码，才手动内联 `warm-neutral-artifact.css` 的必要部分。
3. 如果用户允许 CDN，可用 Tailwind 负责基础布局，但仍保留本默认风格的变量和组件类。
4. 如果用户要求离线，不引用 Tailwind，直接内联 CSS。
5. 如果要使用案例图，优先把对应 SVG 文件内容复制进 HTML，而不是 `<img src="...">` 外链。
6. 如果只是借鉴视觉风格，不需要嵌入案例图；重绘与文章内容相关的新 SVG 更好。

## 适用场景

- 文章解释页：用 `eight-capabilities` 或自绘能力矩阵做开场。
- Markdown vs HTML 论证：用 `markdown-vs-html` 做对比图。
- 双向交互/调参：用 `tuning-interface` 做机制示意。
- PR/代码审查：用 `code-review-annotations` 做 diff 注释样式参考。
- 设计系统/品牌参考：用 `design-tokens` 做默认 tokens 展示。
- 结构化配置编辑：用 `config-editor` 做表单编辑与 diff 导出示意。

## 注意

- 这套风格是默认值，不是强制品牌。用户给出品牌、产品或行业风格时，优先匹配用户上下文。
- 不要在所有 HTML 文档里机械插入这些案例图；只有当它们能帮助说明内容时才使用。
- 案例图里的文字是示意，不应冒充用户文章中的事实。
