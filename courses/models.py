from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.
class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title= models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Course(models.Model):
    title= models.CharField(max_length=255)
    description=models.TextField()
    source =models.CharField(max_length=255,default='')
    STATUS=Choices('In progress','Completed','Bookmarked')
    status=StatusField()
    order= models.IntegerField(null=True)
    topic= models.ForeignKey('Topic',
    on_delete=models.CASCADE,
)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
