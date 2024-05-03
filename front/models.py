from django.db import models

# Create your models here.
class Feedback(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name="Email")
    descriptions = models.TextField(verbose_name="Сообшение")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio