import curses
from curses import wrapper
from horn.player.player import Player
from .listwindow import ListWindow
from .inputwindow import InputWindow
from .statuswindow import StatusWindow
from .playerwindow import PlayerWindow
import time


class MainWindow(PlayerWindow):

    def __init__(self, win):
        curses.use_default_colors()
        PlayerWindow.__init__(self, win)
        win.nodelay(1)
        max_y, max_x = win.getmaxyx()
        self.list_win = ListWindow(win.derwin(max_y, max_x // 2,
                                              0, max_x // 2))
        self.status_win = StatusWindow(win.derwin(1, max_x,
                                                  max_y - 2, 0))
        self.input_win = InputWindow(win.derwin(1, max_x,
                                                max_y - 1, 0))

    def draw(self):
        self._win.refresh()
        self.list_win.redraw()
        self.status_win.redraw()

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
                # self.playlist_win.win.erase()
                std_max_y, std_max_x = self._win.getmaxyx()
                # self.playlist_win.win.mvderwin(0, std_max_x // 2)
                # self.playlist_win.win.resize(std_max_y, std_max_x // 2)
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
    player.instance().play()
    main_window = MainWindow(stdscr)
    main_window.main_loop()


def run(args):
    wrapper(main, args)
