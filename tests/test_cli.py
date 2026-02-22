"""CLIの挙動テスト。"""

from pathlib import Path

from mlops_template.cli import build_parser, main


def test_parser_default_seed() -> None:
    parser = build_parser()
    args = parser.parse_args([])
    assert args.seed == 42


def test_main_returns_zero() -> None:
    result = main(["--seed", "10", "--log-level", "INFO"])
    assert result == 0


def test_main_creates_output_dir(tmp_path: Path) -> None:
    output_dir = tmp_path / "artifacts"
    result = main(["--output-dir", str(output_dir)])
    assert result == 0
    assert output_dir.exists()
