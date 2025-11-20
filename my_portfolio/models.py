from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Photo(models.Model):   # ✅ Added this model
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption if self.caption else "Photo"


class Certificate(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.title
