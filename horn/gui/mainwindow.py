# -*- coding: utf-8 -*-

from curses import wrapper
from horn.player.player import Player
from horn.event.event import EventObserver
import time


def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr('Implement me')
        stdscr.refresh()
        time.sleep(1)


def run():
    wrapper(main)
