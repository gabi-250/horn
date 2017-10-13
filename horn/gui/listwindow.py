import os
import curses
from horn.player.player import Player
from horn.player.event import EventObserver
from horn.gui.widget import Widget


class ListWindow(Widget, EventObserver):
    def __init__(self, pad, begin_y, begin_x, end_y, end_x):
        Widget.__init__(self)
        EventObserver.__init__(self, Player.instance())
        self._pad = pad
        self._begin_y = begin_y
        self._begin_x = begin_x
        self._end_y = end_y
        self._end_x = end_x

    def draw(self):
        for index, track in enumerate(Player.instance().track_list):
            filename = os.path.basename(track.file_path)
            track_path = Player.instance().current_track.file_path
            if filename == os.path.basename(track_path):
                self._pad.addstr(index, 0, track.name, curses.A_REVERSE)
                selected_index = index
            else:
                self._pad.addstr(index, 0, track.name, curses.A_NORMAL)
        diff = selected_index - (self._end_y - 1) // 2
        start_row = 0 if diff < 0 else diff
        try:
            self._pad.refresh(start_row, 0,
                              self._begin_y, self._begin_x,
                              self._end_y - 1, self._end_x - 1)
        except:
            # do nothing because refresh returns ERR if two refreshes
            # happen in quick succession
            pass
        finally:
            self.dirty = False

    def _play_item(self, list_box, row):
        player = Player.instance()
        player.play(player.track_list[row.get_index()].file_path)

    def resize(self, y, x, height, width):
        self._begin_y = y
        self._begin_x = x
        self._end_y = y + height
        self._end_x = x + width
        self._dirty = True

    def update(self, event):
        from horn.player.event import Event
        if event == Event.play or event == Event.next or \
                event == Event.new:
            self._dirty = True
