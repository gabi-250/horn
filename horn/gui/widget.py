from abc import ABC, abstractmethod


class Widget(ABC):
    def __init__(self):
        self._dirty = True

    def touch(self):
        self._dirty = True

    def redraw(self):
        if self._dirty:
            self.draw()
            self._dirty = False

    @abstractmethod
    def draw(self):
        pass
