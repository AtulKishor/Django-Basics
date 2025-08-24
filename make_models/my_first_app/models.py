from django.db import models

def a():
    pass

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    def __str__(self) -> str:
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=a)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=a)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)
    

    
