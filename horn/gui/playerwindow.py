from abc import ABC, abstractmethod
import curses


class PlayerWindow(ABC):

    def __init__(self, win):
        self._win = win
        self._dirty = True

    def touch(self):
        self._dirty = True

    def redraw(self):
        if self._dirty:
            self.draw()
            self._dirty = False

    def resize(self, y, x, height, width):
        try:
            self._win.resize(height, width)
            self._win.mvwin(y, x)
            self._win.clear()
            self._win.refresh()
        except curses.error:
            # ignore curses errors for now
            pass
        self._dirty = True

    @abstractmethod
    def draw(self):
        self._win.clear()
