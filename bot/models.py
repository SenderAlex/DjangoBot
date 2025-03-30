from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)  # ID telegram
    username = models.CharField(max_length=255, blank=True, null=True)  # username
    created_at = models.DateTimeField(auto_now_add=True)  # дата и время создания

    def __str__(self):
        return f'{self.username} {self.user_id} {self.created_at}'
