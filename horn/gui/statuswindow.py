# -*- coding: utf-8 -*-

from horn.event.event import EventObserver
from horn.player.player import Player
from horn.event.event import Event
from horn.tools.timeformatter import hms_format
import os


class StatusWindow(EventObserver):

    def __init__(self, win):
        EventObserver.__init__(self)
        Player.instance().add_observer(self)
        self._win = win

    def draw(self):
        player = Player.instance()
        self._win.clear()
        state = 'Stopped'
        if player.is_playing():
            state = 'Playing'
        elif player.is_paused():
            state = 'Paused'
        name = player.current_track.name
        if name == '':
            name = os.path.basename(player.current_track.file_path)
        self._win.addstr(0, 0, state + ' ' + name + ' ' +
                         hms_format(player.get_current_second())
                         + '/' + hms_format(player.get_song_duration()))
        self._win.refresh()

    def update(self, event, event_type):
        if event_type == Event.progress:
            self.draw()
        return False
