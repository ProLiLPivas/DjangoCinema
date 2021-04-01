from django.db import models
from django.contrib.auth.models import User

from apps.films.models import Film


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.TimeField(auto_now_add=True)
    likes_amount = models.IntegerField(default=0)
    is_changed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time']


class BaseLike:
    liked_object = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    is_exist = models.BooleanField(default=False)


class FilmLike(BaseLike, models.Model):
    liked_object = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)


class CommentLike(BaseLike):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE , null=True)


class FilmEstimate(models.Model):
    ESTIMATE_TYPES = ((1, 'Bad') , (2, 'Bad') , (3, 'Normal') , (4, 'Good'), (5, 'Great'))

    rating = models.IntegerField(choices=ESTIMATE_TYPES , default=1)
    user = models.ForeignKey(User , on_delete=models.CASCADE , default='1')
