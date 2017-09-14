# -*- coding: utf-8 -*-

from horn.event.event import EventObserver
from horn.player.player import Player
from curses.textpad import Textbox


class InputWindow(EventObserver):

    def __init__(self, win):
        EventObserver.__init__(self)
        Player.instance().add_observer(self)
        self._win = win
        self._text_box = Textbox(self._win)

    def edit(self):
        self._win.move(0, 0)
        self._text_box.edit()
        file_names = self._text_box.gather().strip().split(' ')
        self._win.clear()
        self._win.refresh()
        for file_name in file_names:
                Player.instance().add(file_name)

    def update(self, event, event_type):
        return False
