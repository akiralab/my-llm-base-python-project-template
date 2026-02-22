"""再現性ユーティリティのテスト。"""

import random

import numpy as np

from mlops_template.repro import set_global_seed


def test_set_global_seed_reproduces_random_sequence() -> None:
    set_global_seed(123)
    first = [random.random() for _ in range(3)]
    set_global_seed(123)
    second = [random.random() for _ in range(3)]
    assert first == second


def test_set_global_seed_reproduces_numpy_sequence() -> None:
    set_global_seed(777)
    first = np.random.random(3).tolist()
    set_global_seed(777)
    second = np.random.random(3).tolist()
    assert first == second
