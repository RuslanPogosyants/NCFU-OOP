# Программирование на языке высокого уровня (Python).
# Задание №4.3.6 Вариант 1
#
# Выполнил: Погосянц Р.М.
# Группа: ПИН-б-о-22-1
# E-mail: ruspogosyants@bk.ru

class Player:
    def __init__(self):
        self._is_playing = False

    def play(self):
        self._is_playing = True

    def stop(self):
        self._is_playing = False

class AudioPlayer(Player):
    def __init__(self):
        super().__init__()
        self._current_track = None

    def play(self, track):
        super().play()
        self._current_track = track
        print(f"Playing audio track '{track}'")

    def stop(self):
        super().stop()
        self._current_track = None
        print("Audio stopped")

class VideoPlayer(Player):
    def __init__(self):
        super().__init__()
        self._current_video = None

    def play(self, video):
        super().play()
        self._current_video = video
        print(f"Playing video '{video}'")

    def stop(self):
        super().stop()
        self._current_video = None
        print("Video stopped")

class DvdPlayer(VideoPlayer):
    def __init__(self):
        super().__init__()
        self._current_position = 0

    def play(self, dvd):
        super().play(dvd)
        print(f"Playing DVD '{dvd}'")

    def stop(self):
        super().stop()
        self._save_position()
        print("DVD stopped")

    def _save_position(self):
        self._current_position = 0
