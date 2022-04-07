#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.04.22
@author: felix
"""
import numpy
from click.testing import CliRunner

from src.tasks import start_new_task
import pandas as pd

from tests.conftest import REQUIRED_CSV_HEADER
from tests.conftest import TEST_FILE

runner = CliRunner()


def test_new_task_help_output():
    result = runner.invoke(start_new_task, ["--help"])
    assert result.exit_code == 0
    assert "Usage: START <name of client> <name of task> [PROBONO]" in result.output


def test_create_new_task(cleanup):
    result = runner.invoke(start_new_task, ["client", "testing"])
    assert result.exit_code == 0
    df = pd.read_csv(TEST_FILE)
    for head in REQUIRED_CSV_HEADER:
        assert head in df.columns
    # we should have only one entry the header doesn't count
    assert df.shape[0] == 1
    # END TIME must be empty
    assert numpy.isnan(df.iloc[0]["END TIME"])


def test_create_new_probono_task(cleanup):
    result = runner.invoke(start_new_task, ["client", "testing", "PROBONO"])
    assert result.exit_code == 0
    df = pd.read_csv(TEST_FILE)
    assert "PROBONO" in df.columns
    assert df.iloc[0]["PROBONO"]
