import pygame

class Timer:
    # can execute a function oce the exit_timer is over
    def __init__(self, duration_in_ms):
        self.__duration_in_ms = duration_in_ms
        self.__start_time = 0
        self.__curren_moment = 0
        self.__is_active = False

    @property
    def is_timer_active_read_only(self):
        return self.__is_active

    @property
    def elapsed_time_read_only(self):
        return self.__curren_moment - self.__start_time

    def activate(self):
        self.__is_active = True
        self.__start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.__is_active = False
        self.__start_time = 0

    def timer_update(self):
        self.__curren_moment = pygame.time.get_ticks()
        if self.elapsed_time_read_only > self.__duration_in_ms and self.__is_active:
            self.deactivate()