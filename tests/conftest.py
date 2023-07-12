#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.04.22
@author: felix
"""
import pytest
from pathlib import Path

# select the directory of the current file
BASE_DIR = Path(__file__).parent
TEST_FILE = BASE_DIR / Path("tim.csv")

REQUIRED_CSV_HEADER = ["CLIENT", "TASK", "SUB-TASK", "START TIME", "END TIME", "HOURS"]


@pytest.fixture(scope="function")
def cleanup():
    yield
    if TEST_FILE.exists():
        TEST_FILE.unlink()
