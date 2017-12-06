import curses
from curses import wrapper
from horn.player.player import Player
from .listwindow import ListWindow
from .inputwindow import InputWindow
from .statuswindow import StatusWindow
from .playerwindow import PlayerWindow
from .infowindow import InfoWindow
import time


class MainWindow(PlayerWindow):
    """
    A window which displays all the other player windows.
    """
    def __init__(self, win):
        curses.use_default_colors()
        PlayerWindow.__init__(self, win)
        win.nodelay(1)
        max_y, max_x = win.getmaxyx()
        # max_y - 2 because the list should not overlap with the control bar
        self.list_win = ListWindow(curses.newpad(100, 100),
                                   1, max_x // 2, max_y - 2, max_x)
        self.status_win = StatusWindow(curses.newwin(1, max_x, max_y - 2, 0))
        self.info_win = InfoWindow(curses.newwin(1, max_x, 0, 0))
        self.input_win = InputWindow(curses.newwin(1, max_x, max_y - 1, 0))

    def draw(self):
        self._win.refresh()
        self.status_win.redraw()
        self.info_win.redraw()
        self.list_win.redraw()

    def main_loop(self):
        while True:
            player = Player.instance()
            self.draw()
            input_char = self._win.getch()
            if input_char == ord('h'):
                self.print_help()
            elif input_char == ord('n'):
                player.play_next()
            elif input_char == ord('p'):
                if player.is_playing():
                    player.pause()
                else:
                    player.play()
            elif input_char == ord('+'):
                volume = player.volume + 0.1
                if volume >= 1.0:
                    volume = 1.0
                player.volume = volume
            elif input_char == ord('-'):
                volume = player.volume - 0.1
                if volume >= 1.0:
                    volume = 1.0
                player.volume = volume
            elif input_char == ord('a'):
                self.input_win.edit()
            elif input_char == ord('q'):
                player.exit()
                break
            elif input_char == curses.KEY_RESIZE:
                # resize all inner windows
                self._win.clear()
                max_y, max_x = self._win.getmaxyx()
                self.list_win.resize(1, max_x // 2,
                                     max_y - 2, max_x // 2)
                self.status_win.resize(max_y - 2, 0, 1, max_x)
                self.info_win.resize(0, 0, 1, max_x)
            elif input_char != -1:
                self._win.addstr('Unknown command %s' % input_char)
            time.sleep(0.1)

    def print_help(self):
        self._win.addstr(0, 0, "Type 'a' to enter append mode")
        self._win.addstr(1, 0, "Type 'n' to play the next track")
        self._win.addstr(2, 0, "Type 'p' to play and 'P' to pause")
        self._win.addstr(3, 0, "Type 'q' to quit")
        self._win.addstr(4, 0, "Type 'r' to return to the main menu")


def main(stdscr, playlist):
    player = Player(list(set(playlist)))
    if playlist:
        player.instance().play()
    main_window = MainWindow(stdscr)
    main_window.main_loop()


def run(args):
    wrapper(main, args)
