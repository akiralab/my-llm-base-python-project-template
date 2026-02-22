"""再現性ユーティリティのテスト。"""

import os
import random

from mlops_template.repro import set_global_seed


def test_set_global_seed_reproduces_random_sequence() -> None:
    set_global_seed(123)
    first = [random.random() for _ in range(3)]
    set_global_seed(123)
    second = [random.random() for _ in range(3)]
    assert first == second


def test_set_global_seed_sets_pythonhashseed_env() -> None:
    seed = set_global_seed(777)
    assert seed == 777
    assert os.environ["PYTHONHASHSEED"] == "777"
