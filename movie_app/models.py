from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return self.movie.count()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movie', null=True)

    def __str__(self):
        return self.title

    @property
    def filtered_reviews(self):
        return self.reviews.filter(stars__gte=1)

    @property
    def rating(self):
        reviews = self.filtered_reviews
        count = reviews.count()
        total = 0
        for i in reviews:
            total += i.stars
        try:
            return total/count
        except ZeroDivisionError:
            return 0

STAR_CHOICES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(choices=STAR_CHOICES, default=0)

    def __str__(self):
        return self.text
