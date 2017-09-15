from horn.player.player import Player
from horn.gui.playerwindow import PlayerWindow
from curses.textpad import Textbox


class InputWindow(PlayerWindow):

    def __init__(self, win):
        PlayerWindow.__init__(self, win)
        self._text_box = Textbox(self._win)

    def draw(self):
        self._win.clear()
        self._win.refresh()

    def edit(self):
        self._win.move(0, 0)
        self._text_box.edit()
        file_names = self._text_box.gather().split()
        self.draw()
        for file_name in file_names:
                Player.instance().add(file_name)
