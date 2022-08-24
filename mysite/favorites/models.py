from django.db import models


class FavoriteNews(models.Model):
    is_favorite = models.BooleanField(default=True)
