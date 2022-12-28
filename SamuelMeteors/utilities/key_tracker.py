import pygame.key


class KeyTracker:

    def __init__(self, pygame_key_code):
        self.pygame_key_code = pygame_key_code
        self.__total_times_fired: int = 0
        self.__has_key_been_fired_at_this_frame = False
        self.__has_key_been_released_at_this_frame = False
        self.__is_key_being_held_down = False
        self.__has_key_been_already_fired_but_not_released = False

    @property
    def has_key_been_released_at_this_frame_read_only(self):
        return self.__has_key_been_released_at_this_frame

    @property
    def has_key_been_fired_at_this_frame_read_only(self):
        return self.__has_key_been_fired_at_this_frame

    @property
    def is_key_being_held_down_read_only(self):
        return self.__is_key_being_held_down

    @property
    def total_times_fired_read_only(self):
        return self.__total_times_fired

    def reset_total_times_fired(self):
        self.__total_times_fired = 0

    def update_tracker(self):

        keys = pygame.key.get_pressed()

        # TRACKED KEY HELD DOWN
        self.__is_key_being_held_down = keys[self.pygame_key_code]

        # TRACKED KEY FIRED AND RELEASED
        self.__has_key_been_fired_at_this_frame = False
        self.__has_key_been_released_at_this_frame = False
        if self.__is_key_being_held_down and not self.__has_key_been_already_fired_but_not_released and not self.__has_key_been_fired_at_this_frame:
            self.__has_key_been_fired_at_this_frame = True
            self.__total_times_fired += 1
            self.__has_key_been_already_fired_but_not_released = True
        if self.__has_key_been_already_fired_but_not_released and not self.__is_key_being_held_down:
            self.__has_key_been_already_fired_but_not_released = False
            self.__has_key_been_released_at_this_frame = True

    def get_inspector_debugging_status(self) -> str:
        return f"COMPONENT(KeyTracker)\n" \
               f"tracked key: {self.pygame_key_code}\n" \
               f"total times fired: {self.__total_times_fired}\n" \
               f"this frame: (fired={self.__has_key_been_fired_at_this_frame} | released={self.__has_key_been_released_at_this_frame})\n" \
               f"is held down: {self.__is_key_being_held_down}\n" \
