from django.db import models
from django.contrib.auth import get_user_model


class Blog(models.Model):
    STATUS = (
        ('Pen', 'Pending'),
        ('Pub', 'Publish')
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    blog = models.TextField()

    status = models.CharField(max_length=3, choices=STATUS, default=STATUS[0][0])

    create_at = models.DateField(auto_now=True)
    modified_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
