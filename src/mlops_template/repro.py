"""再現性のためのユーティリティ。"""

from __future__ import annotations

import os
import random


def set_global_seed(seed: int) -> int:
    """乱数シードを設定し、再現可能な実行状態を作る。"""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    return seed
