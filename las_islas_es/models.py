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


class CardText(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_name = models.CharField(
        max_length=30,
        help_text="Enter file name (eg Cancun.jpg)",
        default="default.jpg",
        blank=True
    )