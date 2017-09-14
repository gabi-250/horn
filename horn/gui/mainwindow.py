# -*- coding: utf-8 -*-

import curses
from curses import wrapper
from horn.player.player import Player
from .listwindow import ListWindow
from .inputwindow import InputWindow
from .statuswindow import StatusWindow
import time


def print_help(stdscr):
    stdscr.addstr(0, 0, "Type 'a' to enter append mode")
    stdscr.addstr(1, 0, "Type 'n' to play the next track")
    stdscr.addstr(2, 0, "Type 'p' to play and 'P' to pause")
    stdscr.addstr(3, 0, "Type 'q' to quit")
    stdscr.addstr(4, 0, "Type 'r' to return to the main menu")


def main(stdscr, playlist):
    stdscr.nodelay(1)
    player = Player(list(set(playlist)))
    std_max_y, std_max_x = stdscr.getmaxyx()
    win = stdscr.derwin(std_max_y, int(0.5 * std_max_x), 0, std_max_x // 2)
    list_win = ListWindow(win)
    status_win = StatusWindow(curses.newwin(1, stdscr.getmaxyx()[1],
                                            stdscr.getmaxyx()[0] - 2, 0))
    input_win = InputWindow(curses.newwin(1, stdscr.getmaxyx()[1],
                                          stdscr.getmaxyx()[0] - 1, 0))
    if playlist:
        player.instance().play()
    while True:
        stdscr.refresh()
        list_win.draw()
        status_win.draw()
        input_char = stdscr.getch()
        if input_char == ord('h'):
            print_help(stdscr)
        elif input_char == ord('n'):
            Player.instance().play_next()
        elif input_char == ord('p'):
            player = Player.instance()
            if player.is_playing():
                player.pause()
            else:
                player.play()
        elif input_char == ord('a'):
            input_win.edit()
        elif input_char == ord('q'):
            Player.instance().exit()
            break
        elif input_char == curses.KEY_RESIZE:
            # resize all inner windows
            win.erase()
            std_max_y, std_max_x = stdscr.getmaxyx()
            win.mvderwin(0, std_max_x // 2)
            win.resize(std_max_y, std_max_x // 2)
        elif input_char != -1:
            stdscr.addstr('Unknown command %s' % input_char)
        time.sleep(0.1)


def run(args):
    wrapper(main, args)
