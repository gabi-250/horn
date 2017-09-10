# -*- coding: utf-8 -*-

import curses
from curses import wrapper
from horn.player.player import Player
from .listwindow import ListWindow
from horn.event.event import EventObserver
import time
import os


def print_playlist(stdscr, args):
    stdscr.clear()
    if args:
        if not Player.instance().current_track:
            Player.instance().play()
        stdscr.addstr(0, 0, 'Type "h" for help.\nYour playlist is:')
        for index, arg in enumerate(args):
            filename = os.path.basename(arg)
            track_path = Player.instance().current_track.file_path
            if filename == os.path.basename(track_path):
                stdscr.addstr(index + 1, 0, ('{:<8}{:}'.format('*', filename)))
            else:
                stdscr.addstr(index + 1, 0, ('{:<8}{:}'.format('', filename)))
        if Player.instance().is_playing():
            stdscr.addstr('\nPlaying')
        elif Player.instance().is_paused:
            stdscr.addstr('\nPaused')
        else:
            stdscr.addstr('\nStopped')
        stdscr.refresh()
    else:
        print_help(stdscr)


def print_help(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Type 'a' to enter append mode")
    stdscr.addstr(1, 0, "Type 'n' to play the next track")
    stdscr.addstr(2, 0, "Type 'p' to play and 'P' to pause")
    stdscr.addstr(3, 0, "Type 'q' to quit")
    stdscr.addstr(4, 0, "Type 'r' to return to the main menu")


def main(stdscr, playlist):
    player = Player(list(set(playlist)))
    win = curses.newwin(50, 50, 5, 5)
    list_win = ListWindow(win)
    if playlist:
        player.instance().play()
    while True:
        print_playlist(stdscr, playlist)
        input_char = stdscr.getkey()
        if input_char == 'h':
            print_help(stdscr)
        elif input_char == 'n':
            Player.instance().play_next()
        elif input_char == 'p':
            player = Player.instance()
            if player.is_playing():
                player.pause()
            else:
                player.play()
        elif len(input_char) and input_char[0] == 'a':
            tracks = input_char.split(' ')[1:]
            for track in tracks:
                Player.instance().add(track)
                playlist.append(track)
            print_playlist(playlist)
        elif input_char == 'q':
            Player.instance().stop()
            break
        else:
            stdscr.clear()
            stdscr.addstr('Unknown command %s' % input_char)
            stdscr.refresh()
        list_win.refresh()
        time.sleep(1)


def run(args):
    wrapper(main, args)
