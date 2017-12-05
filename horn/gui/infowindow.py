from horn.player.event import EventObserver
from horn.player.player import Player
from horn.player.event import Event
from horn.gui.playerwindow import PlayerWindow
import curses


class InfoWindow(PlayerWindow, EventObserver):
    """
    A simple window that displays the path of the selected media.

    This displays <user>@<hostname> followed by the path of the
    selected file in the playlist.
    """
    def __init__(self, win):
        import platform
        import getpass
        PlayerWindow.__init__(self, win)
        EventObserver.__init__(self, Player.instance())
        self.user_info = '{user}@{hostname}'.format(user=getpass.getuser(),
                                                    hostname=platform.node())

    def draw(self):
        self._win.clear()
        file_path = Player.instance().current_track.file_path
        to_display = '{user_info}: {path}'.format(user_info=self.user_info,
                                                  path=file_path)
        try:
            self._win.addstr(0, 0, to_display)
        except curses.error:
            pass
        self._win.refresh()

    def update(self, event):
        if event == Event.next:
            self._dirty = True
