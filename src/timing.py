from dataclasses import dataclass
from json import dumps as json_dumps
import logging
from time import time

class TimingData:
    start: float = 0
    _stop: float = 0
    diff: float = 0

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value: float):
        self._stop = value
        self.diff = self._stop - self.start

    def __dict__(self):
        return {
            'start': self.start,
            'stop': self.stop,
            'diff': self.diff,
        }

def dict_format(data: TimingData) -> dict:
    return dict(data)

def json_format(data: TimingData) -> str:
    return json_dumps(dict(data))

def no_format(data: TimingData) -> TimingData:
    return data

class Timer:
    def __init__(self, name = 'timer', logger = None, format = None, timing_container = None):
        if logger == False:
            self.logger = logging.getLogger().debug
            self.format = format or json_format
        elif logger is None:
            self.logger = None
            self.format = None
        else:
            self.logger = logger
            self.format = format or no_format
        self.data = timing_container or TimingData()
        self.name = name

    def start(self):
        self.data.start = time()
        return self

    def stop(self):
        self.data.stop = time()
        if self.logger:
            self.logger(self.format(self.data))
        return self

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
