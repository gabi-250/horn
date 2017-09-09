from enum import Enum
from gi.repository import GLib
from abc import ABC, abstractmethod
import threading


class Event(Enum):
    play = 0
    pause = 1
    stop = 2
    next = 3
    progress = 4


class EventProducer(object):

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def send_event(self, info):
        for obs in self._observers:
            event = threading.Event()
            GLib.idle_add(obs.update, event, info)


class EventObserver(ABC):

    @abstractmethod
    def update(self, event, info):
        return False
