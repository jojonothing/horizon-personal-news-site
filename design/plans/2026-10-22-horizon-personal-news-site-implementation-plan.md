# Horizon Personal AI News Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Chinese-first personal AI news digest site from Horizon, publish it as a static GitHub Pages site, and generate a daily issue with an optional manual catch-up run.

**Architecture:** Keep Horizon's existing Python pipeline and Jekyll Pages site. GitHub Actions loads a public tech/AI configuration plus a model key stored as a repository Secret, generates Markdown posts, and publishes `docs/` to `gh-pages`; the site remains static for visitors.

**Tech Stack:** Python 3.12, uv, Horizon, GitHub Actions, Jekyll, GitHub Pages.

**Spec:** `design/2026-10-22-horizon-personal-news-site.md`

## Global Constraints

- The site, RSS feed, generated posts, and Pages output are public.
- `data/config.github.json` generates Chinese posts only with `ai.languages` set to `["zh"]`.
- Use public tech/AI sources; set `webhook.enabled` and `sources.telegram.enabled` to `false`, remove finance and the `LWN_KEY`-based RSS feed, and clear the unrelated Telegram channels.
- Keep Horizon's `tech-news` and `tech-blog` Profiles; remove the unused finance Profile from the active configuration.
- Keep the DeepSeek provider configured in the current sample; the `DEEPSEEK_API_KEY` value must be entered as a GitHub Actions Secret, never committed or printed.
- Manual validation exposes an `hours` input defaulting to 24. After the user approves launch, scheduled runs use a 24-hour fetch window at 23:00 UTC (07:00 Asia/Shanghai).
- Use static Jekyll Pages only; do not add a database, backend, login, comments, search service, or custom domain.
- Both Pages workflows publish to `gh-pages`; serialize their publish jobs and preserve previously generated posts with `keep_files: true`.
- Keep Pages disabled and omit the schedule trigger during validation. GitHub only allows `workflow_dispatch` when the workflow exists on the repository's default branch, so merge the manual-only workflow before running the GitHub verification; enable Pages and the daily schedule only after the user reviews the generated result.

---

## File Structure

- `data/config.github.json` — runtime configuration copied by the manual or scheduled workflow. It defines the provider, Chinese output language, public sources, Profiles, and disabled delivery integrations.
- `docs/_config.yml` — Jekyll title, description, canonical host `https://jojonothing.github.io`, and repository `baseurl` `/horizon-personal-news-site`.
- `docs/index.md` — Chinese landing page, latest issue link, date archive, and RSS link.
- `docs/assets/css/horizon.css` — small visual adjustments for the personal landing page while keeping the existing theme and responsive behavior.
- `docs/_includes/head-custom.html` — favicon, stylesheet, script, and Chinese RSS discovery link.
- `.github/workflows/daily-summary.yml.disabled` → `.github/workflows/daily-summary.yml` — manual generation and publication workflow during validation; the scheduled trigger is added only at launch.
- `.github/workflows/deploy-docs.yml` — documentation/page publication workflow; share the deployment concurrency group with the daily workflow.

No Python product code or Profile prompt files need to change for the initial version.

### Task 1: Curate the public Chinese tech/AI feed configuration

**Files:**
- Modify: `data/config.github.json`

**Interfaces:**
- Consumes: Horizon's existing `Config` schema and built-in `tech-news` / `tech-blog` Profiles.
- Produces: A valid Actions configuration with Chinese-only output, public tech/AI sources, and no notification side effects or source-specific secret requirements.

- [ ] **Step 1: Set language, active Profiles, and delivery flags**

Set `ai.languages` to `["zh"]`. Keep `tech-news` as the default Profile and keep `tech-blog` for long-form feeds. Remove `finance-news` from `processing.profile_settings` and `digest.profile_order`. Set `webhook.enabled` to `false`.

- [ ] **Step 2: Keep only the approved public tech/AI source examples**

Keep the existing GitHub activity/release sources for Karpathy, vLLM, SGLang, and Triton; keep Hacker News and the `MachineLearning` / `LocalLLaMA` Reddit sources; keep the RSS sources Simon Willison, vLLM Blog, Sean Goedecke, GitHub Trending, and SemiAnalysis. Remove the CNBC Finance feed and the LWN feed containing `${LWN_KEY}`. Keep `sources.telegram` with `enabled: false` and an empty `channels` list; omitting this field restores Horizon's model default `enabled: true`.

- [ ] **Step 3: Validate JSON syntax and configuration invariants**

Run:

```bash
python -m json.tool data/config.github.json >/dev/null
python - <<'PY'
import json
from pathlib import Path

config = json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
assert config["ai"]["languages"] == ["zh"]
assert config["webhook"]["enabled"] is False
assert "finance-news" not in config["processing"]["profile_settings"]
assert "finance-news" not in config["digest"]["profile_order"]
assert config["sources"]["telegram"]["enabled"] is False
assert config["sources"]["telegram"]["channels"] == []
rss_names = {source["name"] for source in config["sources"]["rss"]}
assert rss_names == {
    "Simon Willison", "vLLM Blog", "Sean Goedecke",
    "GitHub Trending - Daily", "Semianalysis",
}
assert all("${" not in source["url"] for source in config["sources"]["rss"])
PY
```

Expected: both commands exit successfully; the five intended public RSS feeds are the only RSS feeds, Telegram is explicitly disabled with no channels, and no source-specific secret placeholder remains.

- [ ] **Step 4: Load the config through Horizon's schema and run focused tests**

Run:

```bash
uv run python - <<'PY'
import tempfile
from src.storage.manager import StorageManager

with tempfile.TemporaryDirectory() as data_dir:
    StorageManager(data_dir=data_dir, config_path="data/config.github.json").load_config()
PY
uv run pytest tests/test_storage.py tests/test_profiles.py -q
```

Expected: the config loads without a model API request, and both existing test modules pass.

- [ ] **Step 5: Commit the configuration**

```bash
git add data/config.github.json
git commit -m "feat: 配置个人中文科技日报信息源"
```

### Task 2: Rebrand the Jekyll landing page

**Files:**
- Modify: `docs/_config.yml`
- Modify: `docs/index.md`
- Modify: `docs/assets/css/horizon.css`
- Modify: `docs/_includes/head-custom.html`

**Interfaces:**
- Consumes: Jekyll's `site.posts`, `relative_url`, the existing `lang: zh` post metadata, and the repository's Chinese Atom feed at `/feed-zh.xml`.
- Produces: A Chinese personal-news landing page that links to the latest post, the 20 most recent posts, and the Chinese feed.

- [ ] **Step 1: Set the site title and GitHub Pages URL**

In `docs/_config.yml`, set `title: 个人 AI 日报`, use a concise Chinese description such as `每日筛选与解读值得关注的 AI 和科技动态。`, set `url: "https://jojonothing.github.io"`, and set `baseurl: "/horizon-personal-news-site"`. This composes to `https://jojonothing.github.io/horizon-personal-news-site`. Keep the existing `jekyll-theme-cayman` theme and `jekyll-feed` plugin.

- [ ] **Step 2: Replace the project documentation landing page with the digest index**

Keep the existing `layout: default` front matter and replace the bilingual project-documentation content with a Chinese introduction, latest-issue link, dated archive, and a clear RSS link. Use these classes consistently with the CSS task and this Liquid structure so empty archives remain valid:

```liquid
<div class="home-intro">
每天阅读经过筛选的 AI 与科技动态，快速了解值得关注的新进展。
</div>

{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign latest_post = zh_posts | first %}

{% if latest_post %}
<p class="latest-issue"><a href="{{ latest_post.url | relative_url }}">阅读最新一期：{{ latest_post.date | date: "%Y-%m-%d" }} — {{ latest_post.title }}</a></p>
{% else %}
<p class="latest-issue"><em>日报生成后会显示在这里。</em></p>
{% endif %}

<h2>近期日报</h2>
<ul class="issue-archive">
{% for post in zh_posts limit:20 %}
  <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }} — {{ post.title }}</a></li>
{% endfor %}
</ul>
```

Add a visible link to `{{ '/feed-zh.xml' | relative_url }}`. Keep the `Home` page front-matter title and do not include upstream project documentation links on the landing page.

Use this visible link in the page body:

```liquid
<p><a href="{{ '/feed-zh.xml' | relative_url }}">订阅中文 RSS</a></p>
```

- [ ] **Step 3: Keep the existing theme and remove bilingual feed discovery**

In `docs/_includes/head-custom.html`, keep the favicon, stylesheet, and script references; update the Chinese RSS discovery title to `个人 AI 日报 RSS（中文）`; and remove the English/all-language feed discovery links. In `docs/assets/css/horizon.css`, retain the existing light/dark palette and add only spacing and typography for `.home-intro`, `.latest-issue`, and `.issue-archive`; avoid adding a CSS framework.

Use this RSS discovery element and keep all asset/feed paths relative to the configured base URL:

```liquid
<link rel="alternate" type="application/atom+xml" title="个人 AI 日报 RSS（中文）" href="{{ '/feed-zh.xml' | relative_url }}">
```

Append these focused styles without changing the existing palette:

```css
.home-intro { margin: 0 0 1.25rem; line-height: 1.75; color: var(--hz-text-muted); }
.latest-issue { margin: 1.25rem 0 2rem; font-size: 1.1rem; font-weight: 700; }
.issue-archive { padding-left: 1.25rem; line-height: 1.9; }
.issue-archive li { margin: 0.2rem 0; }
```

- [ ] **Step 4: Check links and whitespace**

Run:

```bash
git diff --check
rg -n "feed-zh.xml|site.posts|relative_url" docs/index.md docs/_includes/head-custom.html
```

Expected: no whitespace errors; the homepage contains the Chinese post list and RSS link, and all internal URLs use `relative_url` so the project `baseurl` works.

- [ ] **Step 5: Commit the site shell**

```bash
git add docs/_config.yml docs/index.md docs/assets/css/horizon.css docs/_includes/head-custom.html
git commit -m "feat: 定制个人中文日报首页"
```

### Task 3: Add a safe manual Pages workflow for validation

**Files:**
- Rename: `.github/workflows/daily-summary.yml.disabled` to `.github/workflows/daily-summary.yml`
- Modify: `.github/workflows/daily-summary.yml`
- Modify: `.github/workflows/deploy-docs.yml`

**Interfaces:**
- Consumes: `data/config.github.json`, the repository Secret `DEEPSEEK_API_KEY`, and generated Jekyll Markdown under `docs/`.
- Produces: A manual run with a positive integer lookback and serialized updates to `gh-pages`; the daily schedule is added only after the user approves launch.

- [ ] **Step 1: Activate the workflow for manual validation only**

Rename the disabled template to `.github/workflows/daily-summary.yml`. Keep `workflow_dispatch` as the only trigger in this validation version; do not add a `schedule` trigger yet. Preserve the workflow name `Daily Horizon Summary`.

- [ ] **Step 2: Add a manual lookback input and map only the model key**

Add an optional numeric `workflow_dispatch` input named `hours` with description `回看最近多少小时`, default `24`:

```yaml
on:
  workflow_dispatch:
    inputs:
      hours:
        description: 回看最近多少小时
        required: false
        type: number
        default: 24

```

Replace the existing `Run Horizon` step with this block. The positive-integer check uses an environment variable so user input is not interpolated into shell source. Keep only `DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}` in this step's secret environment:

```yaml
      - name: Run Horizon
        env:
          HORIZON_HOURS: ${{ inputs.hours }}
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
        run: |
          hours="${HORIZON_HOURS:-24}"
          if ! [[ "$hours" =~ ^[1-9][0-9]*$ ]]; then
            echo "::error::hours must be a positive integer"
            exit 1
          fi
          uv run horizon --hours "$hours"
```

Remove the unused OpenAI, Anthropic, Google, `HORIZON_WEBHOOK_URL`, and `LWN_KEY` mappings. Do not add secret values to files or workflow logs.

- [ ] **Step 3: Serialize Pages publishes and keep historical posts**

Add this top-level concurrency block to both workflows, before `jobs:`:

```yaml
concurrency:
  group: horizon-pages
  cancel-in-progress: false
```

Keep `publish_dir: ./docs`, `publish_branch: gh-pages`, and `keep_files: true` on both publish actions so source documentation changes do not erase daily posts. If GitHub replaces a waiting run in this concurrency group, rerun that workflow after the active publish finishes.

- [ ] **Step 4: Check the workflow diff and file activation**

Run:

```bash
git diff --check
test -f .github/workflows/daily-summary.yml
test ! -e .github/workflows/daily-summary.yml.disabled
! rg -n '^  schedule:' .github/workflows/daily-summary.yml
rg -n "workflow_dispatch|HORIZON_HOURS|DEEPSEEK_API_KEY|concurrency:|keep_files:" .github/workflows/daily-summary.yml .github/workflows/deploy-docs.yml
! rg -n 'secrets\.(OPENAI_API_KEY|ANTHROPIC_API_KEY|GOOGLE_API_KEY|HORIZON_WEBHOOK_URL|LWN_KEY)' .github/workflows/daily-summary.yml
```

Expected: the active workflow exists, the disabled template and schedule trigger are absent, both workflows share the concurrency group, and only the DeepSeek Secret is mapped into the generator step. Confirm the publish step follows `Run Horizon` and neither it nor the job uses `if: always()` or `continue-on-error`; GitHub's default success condition then prevents publishing after generation fails, while a failed publish leaves the previous `gh-pages` branch intact.

- [ ] **Step 5: Commit the workflow changes**

```bash
git add -A -- .github/workflows
git commit -m "ci: 启用个人日报手动验证工作流"
```

### Task 4: Verify the fork and generated site before launch

**Files:**
- Verify: `data/config.github.json`
- Verify: `docs/_config.yml`, `docs/index.md`, `docs/_includes/head-custom.html`
- Verify: `.github/workflows/daily-summary.yml`, `.github/workflows/deploy-docs.yml`

**Interfaces:**
- Consumes: the completed local branch, a public Horizon fork, and the user's model API key entered directly in GitHub Actions Secrets.
- Produces: A manually generated Chinese issue on `gh-pages`; Pages remains disabled until the user approves launch.

- [ ] **Step 1: Run the repository test suite**

Run:

```bash
uv sync --extra dev
git diff --exit-code -- uv.lock
uv run pytest -q
```

Expected: the full existing Horizon suite passes and `uv.lock` remains unchanged. The local `uv` available in the implementation environment is version `0.2.21`, which does not support `uv sync --locked`; inspect and revert any lock-only rewrite before continuing because this plan does not change project dependencies.

- [ ] **Step 2: Create the public fork and connect the local branch**

Create the public fork `jojonothing/horizon-personal-news-site` from `Thysrael/Horizon` in GitHub. Set `origin` to `git@github.com:jojonothing/horizon-personal-news-site.git`, leave `upstream` at `https://github.com/Thysrael/Horizon.git`, then push the implementation branch and open a pull request:

```bash
git remote add origin git@github.com:jojonothing/horizon-personal-news-site.git
git push --set-upstream origin codex/personal-daily-news-design
```

Do not enable GitHub Pages or add the scheduled trigger.

- [ ] **Step 3: Add the model key without exposing it in chat or Git**

In the fork's Settings → Secrets and variables → Actions, add `DEEPSEEK_API_KEY` with the user's value. Do not ask the user to paste the value into chat or write it to a local file.

- [ ] **Step 4: Obtain approval to merge the verified source into the default branch**

Show the pull request diff and local test results to the user. After the user approves the merge, merge the pull request into `main`. This is required because GitHub only exposes `workflow_dispatch` for a workflow file present on the default branch. Keep Pages disabled and leave the schedule trigger absent.

- [ ] **Step 5: Run a manual Actions verification**

Run `Daily Horizon Summary` from the Actions tab on `main` with `hours: 24`. Verify the workflow succeeds, the generated Chinese post appears on `gh-pages`, and the run log contains no unmasked secret. Verify repository Pages settings remain disabled and the workflow still has no scheduled trigger.

- [ ] **Step 6: Verify docs publication preserves the generated issue**

Run `Deploy Docs` manually from `main` after the daily summary succeeds. Verify the generated post remains on `gh-pages` after both workflows publish. Check that the generated post is Chinese and has working source links, the home page source links to the latest issue and archive, and `docs/feed-zh.xml` retains its `/feed-zh.xml` permalink and Chinese-post filter. Keep Pages disabled so the result is not public yet; the Atom feed is rendered only after GitHub Pages builds the branch.

- [ ] **Step 7: Present the completed result for final launch approval**

Show the merged source diff, generated Markdown post, successful manual Actions run, and `gh-pages` contents to the user. Do not enable GitHub Pages or the daily schedule until the user approves this concrete result.

### Task 5: Launch Pages and daily generation after approval

**Files:**
- Modify: `.github/workflows/daily-summary.yml`
- Verify: GitHub repository Settings → Pages

**Interfaces:**
- Consumes: the approved generated post, the verified `gh-pages` branch, and the repository Secret `DEEPSEEK_API_KEY`.
- Produces: the public site at `https://jojonothing.github.io/horizon-personal-news-site` and daily generation at 07:00 Asia/Shanghai.

- [ ] **Step 1: Add the approved daily schedule**

After the user approves launch, add this trigger to the existing manual workflow and keep `workflow_dispatch` available:

```yaml
on:
  schedule:
    # GitHub Actions uses UTC; 23:00 UTC is 07:00 the following day in Shanghai.
    - cron: '0 23 * * *'
  workflow_dispatch:
    inputs:
      hours:
        description: 回看最近多少小时
        required: false
        type: number
        default: 24
```

- [ ] **Step 2: Update the workflow on the default branch**

Commit the schedule addition to `main` and push it so GitHub activates the daily trigger:

```bash
git add .github/workflows/daily-summary.yml
git commit -m "ci: 启用个人日报每日调度"
git push origin main
```

- [ ] **Step 3: Publish the verified `gh-pages` branch and enable Pages**

Run `Deploy Docs` from `main` and wait for success. In Settings → Pages, choose `Deploy from a branch`, select `gh-pages` and `/ (root)`, and save. Confirm the canonical URL is `https://jojonothing.github.io/horizon-personal-news-site`.

- [ ] **Step 4: Verify the public site and feed**

Open the Pages URL and verify the home page, a generated issue, the dated archive, and `https://jojonothing.github.io/horizon-personal-news-site/feed-zh.xml`. Confirm the workflow remains available for manual catch-up runs and is scheduled for 23:00 UTC.
