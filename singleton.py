import datetime
from typing import Callable
from threading import Lock, RLock


class SingletonMeta(type):
    """
    Singleton as a metaclass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonMetaThreadSafe(type):
    """
    Thread safe singleton as a metaclass
    """
    _instances = {}
    _loc: Lock = RLock()

    def __call__(cls, *args, **kwargs):
        with cls._loc:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton:
    """
    Singleton as a class
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            cls._instance = instance
        return cls._instance


class Logger(metaclass=SingletonMetaThreadSafe):
    """
    Logger is good example of using singleton
    If you need to log some information in other module,
    you don't need to create another instance of logger.
    """
    def __init__(self, view_method: Callable, logger_id: str):
        self.view_method = view_method
        self.id = logger_id

    def info(self, message: str):
        self.view_method(f'[{self.id}]: {datetime.datetime.now()} [INFO] -> {message}')

    def debug(self, message: str):
        self.view_method(f'[{self.id}]: {datetime.datetime.now()} [DEBUG] -> {message}')


if __name__ == '__main__':
    from threading import Thread

    def test_singleton(view_function, logger_id):
        logger = Logger(view_function, logger_id)
        logger.info('Hello World!')


    t1 = Thread(target=test_singleton, args=(print, 'main_logger'))
    t2 = Thread(target=test_singleton, args=(print, 'custom_logger'))

    t1.start()
    t2.start()

