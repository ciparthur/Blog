from django.db import models

class BlogPost(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
