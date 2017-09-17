from abc import ABC, abstractmethod


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

    @abstractmethod
    def draw(self):
        self._win.clear()

    # @abstractmethod
    def resize(self, y, x, height, width):
        pass
