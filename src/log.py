#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from pathlib import Path

import pandas as pd

import pendulum

OUTPUT_FILE = Path("tim.csv")
HEADERS = ["CLIENT", "TASK", "SUB-TASK", "START TIME", "END TIME", "HOURS", "PROBONO"]
DATE_TIME_FORMAT = "YYYY-MM-DD HH:mm:ss"
DATE_FORMAT = "YYYY-MM-DD"


def create_csv_if_needed(output_file=OUTPUT_FILE):
    if not output_file.is_file():
        with open(output_file, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(HEADERS)
        return True
    return False


def add_new_task(*args):
    with open(OUTPUT_FILE, "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(args)


def stop_task():
    now = pendulum.now()
    now_str = now.format(DATE_TIME_FORMAT)
    df = pd.read_csv(OUTPUT_FILE)
    last_element_idx = df.tail(1).index
    df.loc[last_element_idx, HEADERS[-2]] = now_str
    end_time = df.loc[last_element_idx]["END TIME"].values[0]
    start_time = df.loc[last_element_idx]["START TIME"].values[0]
    total_hours = (
        pendulum.from_format(end_time, DATE_TIME_FORMAT)
        - pendulum.from_format(start_time, DATE_TIME_FORMAT)
    ).total_hours()
    df.loc[last_element_idx, HEADERS[-1]] = total_hours
    df.to_csv(OUTPUT_FILE, index=False)


def total_time():
    df = pd.read_csv(OUTPUT_FILE)
    return df[df["HOURS"] > 0]["HOURS"].sum()


def last_task_closed():
    df = pd.read_csv(OUTPUT_FILE)
    last_task_hours = df.tail(1)["HOURS"].values.tolist()[0]
    return not pd.isna(last_task_hours)


def time_since(datetime_obj):
    df = pd.read_csv(OUTPUT_FILE)
    df["START TIME"] = pd.to_datetime(df["START TIME"])
    return df[df["START TIME"] > datetime_obj]["HOURS"].sum()
