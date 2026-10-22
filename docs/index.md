---
layout: default
title: Home
---

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

<p><a href="{{ '/feed-zh.xml' | relative_url }}">订阅中文 RSS</a></p>
