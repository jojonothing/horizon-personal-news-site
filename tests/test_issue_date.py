import asyncio
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from types import SimpleNamespace

from rich.console import Console

import src.orchestrator as orchestrator_module
from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


def test_issue_outputs_use_shanghai_date_and_fetch_window_stays_utc(
    monkeypatch, tmp_path
) -> None:
    monkeypatch.setenv("HORIZON_TIMEZONE", "Asia/Shanghai")

    class FixedDateTime(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[no-untyped-def]
            fixed = datetime(2026, 10, 21, 23, tzinfo=timezone.utc)
            return fixed if tz is None else fixed.astimezone(tz)

    monkeypatch.setattr(orchestrator_module, "datetime", FixedDateTime)

    requested_issue_dates: list[str] = []
    saved_issue_dates: list[str] = []
    fetch_windows: list[datetime] = []

    class StubStorage:
        def save_daily_summary(self, issue_date, summary, language):  # type: ignore[no-untyped-def]
            saved_issue_dates.append(issue_date)
            return Path("data/summaries") / f"{issue_date}-{language}.md"

    class StubSummarizer:
        def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
            pass

        async def generate_summary(
            self, items, issue_date, item_count, language
        ) -> str:
            requested_issue_dates.append(issue_date)
            return "# Summary\n\nBody"

    item = ContentItem(
        id="item-1",
        source_type=SourceType.RSS,
        title="Example",
        url="https://example.com/story",
        content="Story content",
        author="Example",
        published_at=datetime(2026, 10, 21, 22, tzinfo=timezone.utc),
    )
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(
        ai=SimpleNamespace(languages=["en"]),
        digest=SimpleNamespace(profile_order=[]),
        collection=SimpleNamespace(time_window_hours=24),
        email=None,
    )
    orchestrator.storage = StubStorage()
    orchestrator.console = Console(file=StringIO())
    orchestrator.profiles = SimpleNamespace(names=["Default"])
    orchestrator.last_fetch_report = None
    orchestrator.email_manager = None
    orchestrator.webhook_notifier = None
    orchestrator.wechat_notifier = None

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        fetch_windows.append(since)
        return [item]

    async def select_digest_items(items):  # type: ignore[no-untyped-def]
        return SimpleNamespace(items=items)

    async def enrich_items(items):  # type: ignore[no-untyped-def]
        return None

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "analyze_items", lambda items: _resolved(items))
    monkeypatch.setattr(orchestrator, "select_digest_items", select_digest_items)
    monkeypatch.setattr(orchestrator, "enrich_items", enrich_items)
    monkeypatch.setattr(orchestrator_module, "DailySummarizer", StubSummarizer)
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    assert requested_issue_dates == ["2026-10-22"]
    assert saved_issue_dates == ["2026-10-22"]
    assert fetch_windows == [datetime(2026, 10, 20, 23, tzinfo=timezone.utc)]
    shanghai_post = tmp_path / "docs" / "_posts" / "2026-10-22-summary-en.md"
    assert shanghai_post.read_text(encoding="utf-8").startswith(
        '---\nlayout: default\ntitle: "Horizon Summary: 2026-10-22 (EN)"\n'
        "date: 2026-10-22\nlang: en\n---\n\n"
    )

    requested_issue_dates.clear()
    saved_issue_dates.clear()
    fetch_windows.clear()
    monkeypatch.delenv("HORIZON_TIMEZONE")
    asyncio.run(orchestrator.run())

    assert requested_issue_dates == ["2026-10-21"]
    assert saved_issue_dates == ["2026-10-21"]
    assert fetch_windows == [datetime(2026, 10, 20, 23, tzinfo=timezone.utc)]
    utc_post = tmp_path / "docs" / "_posts" / "2026-10-21-summary-en.md"
    assert utc_post.read_text(encoding="utf-8").startswith(
        '---\nlayout: default\ntitle: "Horizon Summary: 2026-10-21 (EN)"\n'
        "date: 2026-10-21\nlang: en\n---\n\n"
    )


async def _resolved(value):  # type: ignore[no-untyped-def]
    return value
