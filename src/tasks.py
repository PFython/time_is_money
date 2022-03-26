#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import pendulum

from src.log import (add_new_task, create_csv_if_needed, last_task_closed,
                     stop_task, time_since, total_time)
from src.messages import os_display_message


@click.command(name="START")
@click.argument("client_name", nargs=1)
@click.argument("task_name", nargs=1)
def start_new_task(client_name, task_name):
    new_created = create_csv_if_needed()
    now = pendulum.now()
    now_str = now.format("YYYY-MM-DD HH:mm:ss")
    if not new_created:
        if not last_task_closed():
            os_display_message("⚠ ERROR.  Please STOP previous recording first:")
            return
    add_new_task(client_name, task_name, None, now_str, None, None)
    os_display_message("STARTED time recording:")


@click.command(name="STOP")
def stop_some_task():
    if last_task_closed():
        os_display_message("⚠ ERROR.  Please start new recording first.  Last entry:")
    else:
        stop_task()
        os_display_message("COMPLETED time recording:")


@click.command(name="TOTAL")
def total_task_time():
    os_display_message(f"Total Task-Time: {total_time()}")


@click.command("SINCE")
@click.argument("date-string", nargs=1)
def total_task_time_since(date_string):
    result = time_since(pendulum.from_format(date_string, "YYYY-MM-DD").ctime())
    os_display_message(f"Total time since {date_string} = {result}")
