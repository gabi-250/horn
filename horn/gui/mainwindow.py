# -*- coding: utf-8 -*-

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from horn.player.player import Player
from .listwindow import ListWindow
import time


def print_playlist(stdscr, args):
    # stdscr.clear()
    if args:
        if not Player.instance().current_track:
            Player.instance().play()
        stdscr.addstr(0, 0, 'Type "h" for help.')
        if Player.instance().is_playing():
            stdscr.addstr('\nPlaying')
        elif Player.instance().is_paused:
            stdscr.addstr('\nPaused')
        else:
            stdscr.addstr('\nStopped')
    else:
        print_help(stdscr)


def print_help(stdscr):
    stdscr.addstr(0, 0, "Type 'a' to enter append mode")
    stdscr.addstr(1, 0, "Type 'n' to play the next track")
    stdscr.addstr(2, 0, "Type 'p' to play and 'P' to pause")
    stdscr.addstr(3, 0, "Type 'q' to quit")
    stdscr.addstr(4, 0, "Type 'r' to return to the main menu")


def main(stdscr, playlist):
    player = Player(list(set(playlist)))
    std_max_y, std_max_x = stdscr.getmaxyx()
    win = stdscr.derwin(std_max_y, int(0.5 * std_max_x), 0, std_max_x // 2)
    list_win = ListWindow(win)
    input_win = curses.newwin(20, 20, 10, 0)
    if playlist:
        player.instance().play()

    while True:
        print_playlist(stdscr, playlist)
        stdscr.refresh()
        list_win.draw()
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
            text_box = Textbox(input_win)
            input_win.clear()
            rectangle(input_win, 0, 0, 18, 18)
            text_box.edit()
            file_names = text_box.gather().split(' ')
            input_win.clear()
            for file_name in file_names:
                Player.instance().add(file_name)
        elif input_char == ord('q'):
            Player.instance().exit()
            break
        elif input_char == curses.KEY_RESIZE:
            # resize all inner windows
            win.erase()
            std_max_y, std_max_x = stdscr.getmaxyx()
            win.mvderwin(0, std_max_x // 2)
            win.resize(std_max_y, std_max_x // 2)
        else:
            stdscr.addstr('Unknown command %s' % input_char)
        time.sleep(1)


def run(args):
    wrapper(main, args)
