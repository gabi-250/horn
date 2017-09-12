# -*- coding: utf-8 -*-

import os
import curses
from horn.player.player import Player
from horn.event.event import EventObserver
from horn.tools.timeformatter import hms_format


class ListWindow(EventObserver):
    def __init__(self, win):
        EventObserver.__init__(self)
        Player.instance().add_observer(self)
        self._win = win
        self.draw()

    def draw(self):
        for index, track in enumerate(Player.instance().track_list):
            filename = os.path.basename(track.file_path)
            track_path = Player.instance().current_track.file_path
            if filename == os.path.basename(track_path):
                self._win.addstr(index + 1, 0, track.name, curses.A_REVERSE)
            else:
                self._win.addstr(index + 1, 0, track.name, curses.A_NORMAL)
        self._win.refresh()

    def _add_track(self, widget):
        pass

    def _play_item(self, list_box, row):
        player = Player.instance()
        player.play(player.track_list[row.get_index()].file_path)

    def _create_list_item(self, item, data):
        pass

    def update(self, event, event_type):
        from horn.event.event import Event
        if event_type == Event.play or event_type == Event.next:
            player = Player.instance()
            row = self.playlist.get_row_at_index(player.curr_track_index)
            self.playlist.select_row(row)
        return False
