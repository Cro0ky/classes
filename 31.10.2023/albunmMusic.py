import random


class MusicAlbum:
    def __init__(self, title, artist, realese_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.realese_year = realese_year
        self.genre = genre
        self.tracklist = tracklist

    def info(self):
        print(f'Название альбома: {self.title}\n'
              f'Артист: {self.artist}\n'
              f'Год выпуска: {self.realese_year}\n'
              f'Жанр: {self.genre}\n'
              f'Треки: {self.tracklist}')

    def play_trandom_track(self):
        return f'Случайный трек с альбома: {random.choice(self.tracklist)}'


music_album = MusicAlbum('Kingdom made', 'Pepel nahudi', 2023, 'Hip-hop',
                ['Ненадолго', 'Все чем дорожил', 'Заново завоевать', "Дай мне", "Тунайт", "Вдохновение",
                 "Так сложилось", "Минерал", "Звезда упала", "Мы не видели рая"])
music_album.info()
print(music_album.play_trandom_track())
