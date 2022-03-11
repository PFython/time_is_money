#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 11.03.22
@author: felix
"""
import click

from tasks import start_new_task
from tasks import stop_some_task
from tasks import total_task_time
from tasks import total_task_time_since


@click.group()
def messages():
    pass


messages.add_command(start_new_task)
messages.add_command(stop_some_task)
messages.add_command(total_task_time)
messages.add_command(total_task_time_since)


if __name__ == '__main__':
    messages()
