"""テンプレートCLI。"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from loguru import logger

from mlops_template.logging_utils import (
    collect_runtime_context,
    configure_logger,
    log_runtime_context,
)
from mlops_template.repro import set_global_seed


def build_parser() -> argparse.ArgumentParser:
    """CLI引数パーサーを構築する。"""
    parser = argparse.ArgumentParser(
        prog="mlops-template",
        description="MLOpsテンプレートCLI。再現性情報と実行環境情報を記録します。",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="乱数シード値。再現性を担保するため同一値で固定実行できます。",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="ログレベルを指定します。",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="出力ディレクトリ。Pathlib.Pathとして解決して利用します。",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLIエントリポイント。"""
    parser = build_parser()
    args = parser.parse_args(argv)

    configure_logger(args.log_level)
    runtime_context = collect_runtime_context(extra_packages=["ruff", "mypy", "pytest"])
    log_runtime_context(runtime_context)

    seed = set_global_seed(args.seed)
    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info("seed={} を設定しました。", seed)
    logger.info("output_dir={} を利用します。", output_dir)
    logger.info("テンプレートCLIの実行が完了しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
