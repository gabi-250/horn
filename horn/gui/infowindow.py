from horn.player.event import EventObserver
from horn.player.player import Player
from horn.player.event import Event
from horn.gui.playerwindow import PlayerWindow
import curses
import os


class InfoWindow(PlayerWindow, EventObserver):
    """
    A simple window that displays the path of the selected media.

    This displays <user>@<hostname> followed by the path of the
    selected file in the playlist.
    """
    NO_PLAYLIST_ERR = 'No playlist'

    def __init__(self, win):
        PlayerWindow.__init__(self, win)
        EventObserver.__init__(self, Player.instance())
        self.user_info = '{user}@{hostname}'\
            .format(user=os.getenv('USER'),
                    hostname=os.getenv('HOSTNAME'))

    def draw(self):
        self._win.clear()
        player = Player.instance()
        if player.current_track:
            file_path = player.current_track.file_path
        else:
            file_path = ''
        to_display = '{user_info}: {path}'.format(user_info=self.user_info,
                                                  path=file_path)
        try:
            self._win.addstr(0, 0, to_display, curses.A_NORMAL)
            if not player.current_track:
                self._win.addstr(InfoWindow.NO_PLAYLIST_ERR, curses.A_REVERSE)
        except curses.error:
            pass
        self._win.refresh()

    def update(self, event):
        if event == Event.play:
            self._dirty = True
