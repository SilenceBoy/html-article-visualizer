# Token Efficiency

统一样式能节约 token，但前提是把样式从“每次生成的内容”里移出去，变成可复用资产。

## 原则

- 让模型主要生成信息架构和正文片段，而不是反复重写 CSS。
- 固定视觉语言用 `assets/styles/warm-neutral-artifact.css` 承载。
- 固定 HTML 外壳用 `assets/templates/artifact-template.html` 承载。
- 常见示意图用 `assets/examples/*.svg` 复用，只有内容强相关时才重绘。
- 最终交付仍然是单文件 HTML，但合成动作交给 `scripts/build_artifact.py`。

## 推荐路径

1. 先生成一个轻量 HTML fragment，只写 `<section>`、`.hav-window`、`.hav-grid`、`.hav-card` 等结构。
2. 将 fragment 保存到临时文件。
3. 调用脚本合成最终 HTML：

```bash
python3 html-article-visualizer/scripts/build_artifact.py \
  --content-file /tmp/article-fragment.html \
  --output /path/to/final.html \
  --title "文章标题" \
  --subtitle "一句话摘要" \
  --kicker "Article Explainer" \
  --example markdown-vs-html.svg
```

## 什么时候不用脚本

- 用户明确要求直接输出完整 HTML 代码。
- HTML 很短，内联样式比脚本流程更省事。
- 用户要的是一次性提示词模板，而不是在本机生成文件。

## 组件类名优先级

优先复用这些类，减少重复样式：

- 页面：`.hav-page`、`.hav-shell`、`.hav-hero`
- 标题：`.hav-kicker`、`.hav-title`、`.hav-subtitle`、`.hav-section-title`
- 布局：`.hav-grid`、`.hav-section`
- 容器：`.hav-card`、`.hav-window`、`.hav-window-bar`、`.hav-window-body`
- 内容：`.hav-feature-card`、`.hav-flow`、`.hav-flow-node`、`.hav-code`、`.hav-annotation`
- 动作：`.hav-button`、`.hav-pill`、`.hav-copy-row`

## 取舍

- 如果最终答案直接贴完整 HTML，输出 token 不会因为统一样式消失；CSS 仍然要出现在最终 HTML 中。
- 如果在本地创建文件，脚本合成能显著减少模型需要生成和审阅的样式 token。
- 样式越统一，后续修改越便宜；但不要为了省 token 牺牲文章特有的信息图表达。
