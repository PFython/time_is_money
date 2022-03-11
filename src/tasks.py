#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import pendulum

from log import add_new_task
from log import create_csv_if_needed
from log import last_task_closed
from log import stop_task
from log import time_since
from log import total_time


@click.command(name="START")
@click.argument('client_name', nargs=1)
@click.argument('task_name', nargs=1)
def start_new_task(client_name, task_name):
    new_created = create_csv_if_needed()
    now = pendulum.now()
    now_str = now.format('YYYY-MM-DD HH:mm:ss')
    if not new_created:
        if not last_task_closed():
            click.echo("⚠ ERROR.  Please STOP previous recording first:")
            return
    add_new_task(client_name, task_name, None, now_str, None, None)
    click.echo("STARTED time recording:")


@click.command(name="STOP")
def stop_some_task():
    if last_task_closed():
        click.echo("⚠ ERROR.  Please start new recording first.  Last entry:")
    else:
        stop_task()
        click.echo("COMPLETED time recording:")


@click.command(name="TOTAL")
def total_task_time():
    click.echo(total_time())


@click.command("SINCE")
@click.argument('date-string', nargs=1)
def total_task_time_since(date_string):
    click.echo(time_since(pendulum.from_format(date_string, "YYYY-MM-DD").ctime()))
