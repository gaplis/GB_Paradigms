# Задание 1:
#
# Контекст:
# В каждом телефоне есть это замечательное приложение.
# Секундомер - это программа, которая засекает сколько
# времени прошло от момента запуска до момента остановки.
# Также, как правило там присутствует функция “паузы”,
# которая позволяет временно приостановить секундомер, с
# возможностью продолжить отсчет в будущем.

# Ваша задача:
# Реализовать секундомер на любом языке программирования
# в любой парадигме. Секундомер должен поддерживать
# следующий функционал:
# ○ Запуск
# ○ Пауза
# ○ Выход из паузы
# ○ Остановка

from time import time, sleep
from typing import Any


class Timer:
    is_running: bool
    is_pause: bool
    restart: Any
    stop: Any
    start_pause_time: Any
    total_pause_time: Any

    def __init__(self):
        self.reset()

    def start(self):
        self.is_running = True
        self.restart = time()

    def pause(self):
        if self.is_running and not self.is_pause:
            self.is_pause = True
            self.start_pause_time = time()

    def resume(self):
        if self.is_running and self.is_pause:
            self.is_pause = True
            self.total_pause_time += time() - self.start_pause_time

    def reset(self):
        self.is_running = False
        self.is_pause = False
        self.restart = None
        self.stop = 0
        self.start_pause_time = 0
        self.total_pause_time = 0

    def print_result(self):
        print(f'Time taken: {time() - self.restart - self.total_pause_time}')


timer = Timer()
timer.start()
sleep(3)
timer.print_result()
timer.pause()
sleep(3)
timer.resume()
timer.print_result()
sleep(3)
timer.print_result()
