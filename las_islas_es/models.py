from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.email}"
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'