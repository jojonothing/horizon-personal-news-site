# Horizon 个人 AI 新闻日报站设计

状态：已确认，进入实施计划<br>
日期：2026-10-22

## 目标

基于 Horizon 建立一个公开的个人 AI 新闻日报站，使用 GitHub Pages 托管。Horizon 继续负责抓取、评分、筛选和生成日报；GitHub Actions 负责定时运行；Jekyll 将 Markdown 日报渲染成可浏览、可订阅的静态网站。

首版成功标准：

1. 首页能阅读最新一期，并按日期浏览历史日报。
2. 网站提供中文 RSS 订阅。
3. 日报每天自动生成，也可从 GitHub Actions 手动补跑。
4. API 密钥不进入 Git、构建产物或网站内容。
5. 信息源和分析 Profile 可通过 Horizon 现有配置调整，不需要编写新的采集后端。

## 已确认的设计选择

- **项目基础**：在当前登录的 GitHub 账号 `jojonothing` 下新建 Horizon fork。当前本地副本位于 `/Users/wenxiongzhou/Dev/horizon-personal-news-site`，从 Horizon `main` 分支克隆；仓库名为 `horizon-personal-news-site`，预期 Pages 地址为 `https://jojonothing.github.io/horizon-personal-news-site`。远程仓库尚未创建。
- **生成与发布**：保留 Horizon 的 Python 流水线、Jekyll 页面和 GitHub Pages 发布方式，不重写前端，也不增加服务端。
- **语言与内容**：首版中文为主，使用公开科技/AI 信息源，以 `tech-news` Profile 作为起点。当前 `data/config.github.json` 有 4 个 GitHub 源和 7 个 RSS 源；实施时会从公开示例中筛选适合个人日报的内容，并将语言配置调整为中文。
- **阅读体验**：将首页改成个人品牌入口，突出最新一期，提供近期日报归档、原文链接和 RSS。保留 Horizon 生成的 Markdown 正文，不在首版重做内容模板。
- **非目标**：首版不实现账号、评论、数据库、动态 API、站内搜索或自定义域名。

## 组件和数据流

```text
GitHub Actions 定时触发或手动触发
  -> 安装 Horizon 依赖，载入公开配置和 Actions Secrets
  -> 运行 Horizon（默认回看最近 24 小时）
  -> 生成中文 Markdown 日报到 Jekyll 内容目录
  -> Jekyll / GitHub Pages 发布首页、归档和 RSS
```

网站由静态文件组成，访客浏览不需要调用 Horizon 或 AI API。日报生成仍会调用配置的模型，因此模型费用取决于信息源数量和每日运行次数。

## 页面结构

- **首页**：个人站点标题和简短介绍；最新一期入口；按日期排列的近期日报列表；RSS 订阅链接。
- **日报页**：Horizon 生成的中文 Markdown，保留标题、摘要、评分、背景说明和来源链接等配置中启用的区块。
- **历史归档**：复用 Jekyll posts 和现有 Feed 机制，首屏展示近期内容，旧日报仍可通过日期链接访问。

现有 `docs/index.md` 同时承担 Horizon 项目文档首页和双语日报列表。实施时会将它改成个人日报首页，并从公开导航移除不适用于个人站的项目介绍；Horizon 的运行代码和许可证保留在仓库中。

## 自动运行和发布

- 启用当前禁用的 `.github/workflows/daily-summary.yml.disabled` 模板，手动验证阶段只开放 `workflow_dispatch`，增加 `hours` 输入并默认回看 24 小时；最终确认后再启用每日定时触发，避免验证期间产生计划外的模型调用。
- 初始默认按北京时间每天 07:00 运行（GitHub Actions 的 cron 使用 UTC，对应前一日 23:00 UTC）；定时注释应与实际 cron 保持一致。Actions 可能延迟启动，手动触发用于补跑。
- 日报工作流和文档发布工作流都会更新 `gh-pages`。实施时要确认两者不会互相覆盖已生成的历史日报，并在需要时串行化 Pages 发布。
- 先通过手动工作流完成端到端验证，再依赖定时运行。

## 密钥和公开内容

- GitHub Pages 是公开站点；日报、RSS 和发布目录中的所有内容都按公开信息处理。
- API 密钥只放在 GitHub Actions Secrets，并映射为配置所引用的环境变量。
- 不提交 `.env`、会话凭据、订阅者数据、带令牌的私有 RSS URL 或其他个人访问凭据。
- `data/config.github.json` 只保留非敏感设置和环境变量名称；不能在配置或 Markdown 中写入密钥值。

## 失败行为

- Horizon 生成步骤失败时，后续 Pages 发布步骤不应运行；已经部署的上一版网站继续提供访问，失败详情通过 Actions 日志查看。
- 生成成功但 Pages 发布失败时，Actions 应显示失败，之后可手动重试；不要把部分生成结果当作成功发布。
- 日报生成采用最近 24 小时作为初始窗口。若运行延迟导致内容缺口，手动补跑时可按实际情况扩大回看窗口。

## 验证方案

1. 检查配置只引用环境变量，不含凭据；确认公开信息源和 Profile 能通过 Horizon 读取。
2. 手动运行工作流，检查是否生成中文日报、是否没有把密钥写入日志或发布文件。
3. 检查 Pages 首页、单期正文、归档链接和中文 RSS；确认新一期出现且历史链接仍可访问。
4. 检查 Actions 失败路径不会覆盖已发布网站，并验证手动重跑可恢复。
5. 确认定时工作流的 UTC cron 与北京时间说明一致。

## 实施顺序

1. 创建个人 GitHub fork，并确认 Pages 站点 URL 和仓库路径。
2. 定制 `data/config.github.json`、`tech-news` Profile、`docs/_config.yml`、`docs/index.md` 和站点样式。
3. 配置 Actions Secrets，启用并校准日报工作流，处理两个 Pages 发布工作流之间的历史内容保留与并发。
4. 手动运行并验证日报、站点和 RSS。
5. 手动验证完成后请用户审阅生成内容；确认后启用 GitHub Pages 和每日定时运行。
