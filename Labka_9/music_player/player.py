import pygame
import os


class MusicPlayer:
    def __init__(self):
        self.playlist = [
            "music/Candy_Shop.mp3",
            "music/PIMP.mp3",
            "music/Shot_Down.mp3"
        ]

        self.current_track = 0
        self.is_playing = False
        self.is_paused = False

        self.load_track(self.current_track)

    def load_track(self, index):
        pygame.mixer.music.load(self.playlist[index])

    def play(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play()

        self.is_playing = True
        self.is_paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True
        self.is_playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.load_track(self.current_track)
        self.play()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.load_track(self.current_track)
        self.play()

    def get_track_name(self):
        return os.path.basename(self.playlist[self.current_track])

    def get_status(self):
        if self.is_paused:
            return "Paused"
        elif self.is_playing:
            return "Playing"
        else:
            return "Stopped"

    def get_time_text(self):
        pos = pygame.mixer.music.get_pos() / 1000
        return f"Time: {round(pos, 1)}s"