from django.db import models

# Create your models here.
class Video(models.Model):
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='./video/')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    img = models.ImageField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Type(models.Model):
    img = models.ImageField(default=1)
    name = models.CharField(max_length=255)


    def __str__(self):
        return str(self.name)

class User(models.Model):
    img = models.ImageField(default=1)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)