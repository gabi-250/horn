# -*- coding: utf-8 -*-

from horn.player.player import Player
from horn.event.event import EventObserver
from horn.tools.timeformatter import hms_format
from .tools.iconhelp import get_name


class ListWindow(EventObserver):
    def __init__(self):
        EventObserver.__init__(self)
        Player.instance().add_observer(self)

    def _create_playlist(self):
        pass

    def _add_track(self, widget):
        pass

    def _play_item(self, list_box, row):
        player = Player.instance()
        player.play(player.track_list[row.get_index()].file_path)

    def _create_list_item(self, item, data):
        pass

    def update(self, event, event_type):
        from horn.player import player as event
        if event_type == event.PLAY_EVENT or event_type == event.NEXT_EVENT:
            player = Player.instance()
            row = self.playlist.get_row_at_index(player.curr_track_index)
            self.playlist.select_row(row)
        return False
