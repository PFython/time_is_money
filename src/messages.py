#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess


def os_display_message(message):
    try:
        from ctypes import windll
    except ImportError:
        subprocess.call(["notify-send", "Easy Time Recorder", message])
    else:
        windll.user32.MessageBoxW(0, message, "Easy Time Recorder")
