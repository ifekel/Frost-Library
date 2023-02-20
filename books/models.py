from django.db import models
import uuid
from django.urls import reverse

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    about = models.TextField()
    pages = models.PositiveIntegerField()
    ratings = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_item', args=[str(self.id)])