from django.db import models
from guns.models import Gun
from users.models import User


class Review(models.Model):
    gun = models.ForeignKey(
        Gun,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        help_text="Rating from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review for {self.gun.name}"
