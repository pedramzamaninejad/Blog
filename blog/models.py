from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field


class Blog(models.Model):
    STATUS = (
        ('Pen', 'Pending'),
        ('Pub', 'Publish')
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='blogs')
    title = models.CharField(max_length=128)
    blog = CKEditor5Field('Text', config_name='extends')

    status = models.CharField(max_length=3, choices=STATUS, default=STATUS[0][0])

    create_at = models.DateField(auto_now=True)
    modified_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('blog:detail', kwargs={'pk': self.id})


class Comment(models.Model):
    STAR = (
        ('5', 'Vary good'),
        ('4', 'Good'),
        ('3', 'Average'),
        ('2', 'Bad'),
        ('1', 'Very bad'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')

    body = models.CharField(max_length=512)
    star = models.CharField(max_length=1, choices=STAR, default=STAR[0][0])

    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.blog}"


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reply')

    body = models.CharField(max_length=256)

    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.comment}"
