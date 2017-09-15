import os
import curses
from horn.player.player import Player
from horn.event.event import EventObserver
from horn.tools.timeformatter import hms_format
from horn.gui.playerwindow import PlayerWindow


class ListWindow(PlayerWindow, EventObserver):
    def __init__(self, win):
        PlayerWindow.__init__(self, win)
        EventObserver.__init__(self, Player.instance())

    def draw(self):
        for index, track in enumerate(Player.instance().track_list):
            filename = os.path.basename(track.file_path)
            track_path = Player.instance().current_track.file_path
            if filename == os.path.basename(track_path):
                self._win.addstr(index + 1, 0, track.name, curses.A_REVERSE)
            else:
                self._win.addstr(index + 1, 0, track.name, curses.A_NORMAL)
        self._win.refresh()

    def _play_item(self, list_box, row):
        player = Player.instance()
        player.play(player.track_list[row.get_index()].file_path)

    def update(self, event):
        from horn.event.event import Event
        if event == Event.play or event == Event.next:
            self._dirty = True

