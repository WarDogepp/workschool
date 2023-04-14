from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавим свои поля для профиля пользователя
    # Например, можно добавить поле "аватар"
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    class Meta:
        app_label = 'worksch'

    def __str__(self):
        return self.user.username
