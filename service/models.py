from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images')
    
    class Meta:
        verbose_name_plural = 'Services'
        
    def __str__(self) -> str:
        return self.name