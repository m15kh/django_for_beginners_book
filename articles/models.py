from django.conf import settings
from django.db import models
from django.urls import reverse




class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
    def get_absolute_url(self):
        return reverse("article_list")
    
    def __str__(self) :
        return self.comment