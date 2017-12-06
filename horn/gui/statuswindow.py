from horn.player.event import EventObserver
from horn.player.player import Player
from horn.player.event import Event
from horn.tools.timeformatter import hms_format
from horn.gui.playerwindow import PlayerWindow
import curses


class StatusWindow(PlayerWindow, EventObserver):
    """
    A window that displays the state of the player.

    The state can be `playing`, `paused` or `stopped`.
    This also displays the titles of the selected media and the volume.
    """
    def __init__(self, win):
        PlayerWindow.__init__(self, win)
        EventObserver.__init__(self, Player.instance())
        self.display_format = '{state} {title} | {progress}/{duration}' + \
                              ' | Volume: {volume}%'

    def draw(self):
        player = Player.instance()
        self._win.clear()
        state = 'Stopped'
        if player.is_playing():
            state = 'Playing'
        elif player.is_paused():
            state = 'Paused'
        name = player.current_track.title if player.current_track else ''
        to_display = self.display_format.format(
            state=state,
            title=name,
            progress=hms_format(player.get_current_second()),
            duration=hms_format(player.get_song_duration()),
            volume=str(int(round(player.volume, 2) * 100)))
        try:
            self._win.addstr(0, 0, to_display)
        except curses.error:
            pass
        self._win.refresh()

    def update(self, event):
        if event == Event.progress:
            self._dirty = True
