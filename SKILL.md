---
name: html-article-visualizer
description: 将文章、长文本、研究材料、PR/代码说明、产品方案、报告或结构化资料转化为完整、自包含、可直接打开的单文件 HTML5 可视化文档。用户要求“生成 HTML 文档/HTML artifact/交互式说明页/可视化文章/把 Markdown 变成更好读的网页/做成单文件 HTML/可分享报告/HTML 信息图”时使用；也适用于需要用 SVG、CSS、表格、标签页、折叠面板、搜索、复制按钮、拖拽或表单编辑器提升信息密度和可读性的场景。
---

# HTML Article Visualizer

把用户提供的文章或资料转成一个完整、自包含、可直接打开的 HTML5 文档。核心目标不是“把 Markdown 包一层网页”，而是用 HTML 的版面、视觉层级、SVG 和交互能力，让信息更容易阅读、比较、导航、分享和二次使用。

## 工作流

1. **识别用途**
   - 文章解读：突出主张、论证链、关键概念、反例和行动建议。
   - 方案/规格：突出目标、约束、决策、架构、流程和待确认问题。
   - 代码/PR：突出 diff、调用链、风险、数据流和审查结论。
   - 报告/研究：突出摘要、证据、时间线、数据表、图表和结论。
   - 编辑界面：突出可操作控件、实时预览和导出按钮。

2. **先做信息架构**
   - 提炼 1 个中心观点、3-7 个一级章节、关键术语、可视化机会和适合交互的区域。
   - 长文本必须先重组，不能按原文顺序机械搬运。
   - 保留重要原意；对缺失、推断和不确定内容用文案明确标注。

3. **选择表现形式**
   - 对比/取舍：并排卡片、矩阵、雷达图、滑块或开关。
   - 流程/机制：SVG 流程图、泳道图、状态机或步骤时间线。
   - 层级/概念：思维导图、树图、术语卡片、悬浮解释。
   - 数据/事实：表格、条形图、迷你图、统计摘要。
   - 行动项/提示词：高亮区块和“复制”按钮。
   - 大段内容：标签页、折叠面板、搜索框、目录锚点。

4. **选择视觉风格**
   - 用户提供品牌、参考图或产品上下文时，优先匹配用户风格。
   - 用户没有指定风格时，读取 `references/default-style-system.md`，使用 warm neutral 默认风格。
   - 默认风格包含窗口容器、能力卡片、Markdown vs HTML 对比、调参界面、代码审查注释等案例资产。

5. **生成单文件 HTML**
   - 只输出或写入一个 `.html` 文件，能直接用浏览器打开。
   - 如果是在本机创建文件，优先读取 `references/token-efficiency.md`，用 `scripts/build_artifact.py` 合成最终 HTML，避免重复生成固定 CSS 和外壳。
   - 只有在用户要求“直接输出完整 HTML 代码”时，才把完整 CSS/HTML 全量写入最终回答。
   - 默认可用 Tailwind CDN：`https://cdn.tailwindcss.com`。如果用户明确要求离线，则不要依赖外部 CDN，改用内联 CSS。
   - 使用内联 `<style>`、内联 `<script>` 和内联 SVG；不要引用外部 JS 包或远程字体，除非用户明确允许。
   - 如果使用 skill 自带案例图，将 `assets/examples/*.svg` 的内容内联到 HTML，避免生成依赖本地相对路径的成品。
   - 用 `<article>` 包裹正文，包含目录导航、返回顶部、页脚和移动端适配。

6. **验证**
   - 检查 HTML 结构完整：`<!doctype html>`、`<html>`、`<head>`、`<meta name="viewport">`、`<title>`、`<body>`。
   - 检查交互不会阻断阅读：无 JS 时核心内容仍可读。
   - 检查移动端：主要网格可单列显示，按钮和表格不溢出。
   - 如果创建了本地 HTML 文件，优先用浏览器或 Playwright 打开做一次基本渲染验证。

## 设计要求

- 以阅读效率为第一目标，视觉效果服务于理解，不做无意义装饰。
- 使用清晰的信息层级：摘要、目录、主张、证据、图解、细节、结论。
- 提高信息密度，但保持足够留白；不要把所有内容塞进卡片。
- 使用 SVG 表达真正有结构的信息，例如流程、关系、时间线、对比和空间布局。
- 对代码块提供复制按钮；对提示词、JSON、配置、行动清单提供复制/导出按钮。
- 对长文提供搜索、章节跳转、折叠详情或标签页。
- 支持浅色/深色模式，颜色语义稳定：重点、风险、证据、行动项应可区分。
- 遵守可访问性基本要求：语义标签、足够对比度、按钮有可读标签、交互可键盘触达。

## 默认样式与案例图

- 默认样式说明：`references/default-style-system.md`
- token 节省策略：`references/token-efficiency.md`
- 默认 CSS：`assets/styles/warm-neutral-artifact.css`
- HTML 外壳模板：`assets/templates/artifact-template.html`
- 单文件合成脚本：`scripts/build_artifact.py`
- 案例 SVG：
  - `assets/examples/eight-capabilities.svg`
  - `assets/examples/markdown-vs-html.svg`
  - `assets/examples/tuning-interface.svg`
  - `assets/examples/code-review-annotations.svg`
  - `assets/examples/design-tokens.svg`
  - `assets/examples/config-editor.svg`

使用规则：

- 只有当案例图能帮助理解文章主题时才嵌入；否则只借鉴其视觉语言。
- 输出单文件 HTML 时，必须内联 CSS 和 SVG，不要让最终 HTML 依赖 skill 目录里的相对文件。
- 创建本地文件时，优先只生成正文 fragment，再用 `scripts/build_artifact.py` 注入统一样式、外壳和基础交互。
- 如果文章有自己的截图或图片素材，优先使用用户提供的真实素材；没有素材时，用 SVG 重绘概念图。
- 默认风格不是强制风格；用户给出品牌或审美方向时，覆盖默认样式。

## 输出约束

- 当用户要求“直接给 HTML 代码”时，最终回答只包含完整 HTML，不包 Markdown 代码块，不加解释。
- 当用户要求“创建文件”时，将 HTML 写入用户指定路径；未指定时在当前工作区创建语义化文件名，并在最终回复给出路径和验证结果。
- 不要把原文全部无脑复制成网页；应进行结构化编辑和信息可视化。
- 不要生成多文件项目，除非用户明确要求。
- 不要把 Tailwind 当作唯一设计来源；复杂图表、交互和版式可以使用原生 CSS、SVG 和 JavaScript。

## 提示词模板

如果用户要的是“完善提示词”而不是直接生成 HTML，读取 `references/article-to-html-prompt.md`，基于其模板按用户场景裁剪。
