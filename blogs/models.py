from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
