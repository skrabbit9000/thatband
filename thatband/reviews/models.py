from django.db import models


class Rating(models.TextChoices):
    SUX = "SUX", "Sux"
    MEH = "MEH", "Meh"
    OK = "OK", "Ok"
    GOOD = "GOOD", "Good"
    GREAT = "GREAT", "Great"


class Genre(models.TextChoices):
    THRASH = "THRASH", "Thrash Metal"
    BLACK = "BLACK", "Black Metal"
    DEATH = "DEATH", "Death Metal"
    INDUSTRIAL = "INDUSTRIAL", "Industrial Metal"
    DOOM = "DOOM", "Doom Metal"
    PROGRESSIVE = "PROGRESSIVE", "Progressive Metal"
    INSTRUMENTAL = "INSTRUMETAL", "Instrumental Metal"
    AMBIENT = "AMBIENT", "Ambient"
    ELECTRONIC = "ELECTRONIC", "Electronic"


class Review(models.Model):

    band_name = models.CharField(max_length=120, unique=True, null=False)

    # TODO fix these magic max_length numbers.
    rating = models.CharField(
        max_length=5, choices=Rating.choices,  # Rating has 5 chars max at the moment.
    )

    genre = models.CharField(
        max_length=11, choices=Genre.choices  # Genre has 11 chars max at the moment
    )

    description = models.TextField()

    sounds_like = models.CharField(
        max_length=120,
        blank = True
    )  # TODO add functionality to link to another band.

    def __str__(self):
        return self.band_name
