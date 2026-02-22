"""ロギング設定と実行環境情報の記録機能。"""

from __future__ import annotations

import json
import platform
import subprocess
import sys
from collections.abc import Iterable
from datetime import UTC, datetime
from importlib import metadata
from pathlib import Path

from loguru import logger


def configure_logger(level: str = "INFO") -> None:
    """ロガーの出力形式とレベルを初期化する。"""
    logger.remove()
    logger.add(
        sys.stderr,
        level=level.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
    )


def _get_git_sha() -> str:
    """現在のGitコミットSHAを取得する。"""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            timeout=2,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"
    if result.returncode != 0:
        return "unknown"
    return result.stdout.strip() or "unknown"


def _get_package_version(name: str) -> str:
    """指定パッケージのバージョン文字列を返す。"""
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return "not-installed"


def collect_runtime_context(extra_packages: Iterable[str] | None = None) -> dict[str, str]:
    """実行環境のメタ情報を収集する。"""
    package_versions = {"loguru": _get_package_version("loguru")}
    for package in extra_packages or ():
        package_versions[package] = _get_package_version(package)

    return {
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "git_sha": _get_git_sha(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
        "packages": json.dumps(package_versions, ensure_ascii=False, sort_keys=True),
    }


def log_runtime_context(context: dict[str, str]) -> None:
    """実行環境情報を一括でログ出力する。"""
    logger.info("runtime_context={}", json.dumps(context, ensure_ascii=False, sort_keys=True))
