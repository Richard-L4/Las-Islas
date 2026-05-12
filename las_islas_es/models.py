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

    def __str__(self):
        return self.title


class Places(models.Model):
    card = models.ForeignKey(CardText, on_delete=models.CASCADE, null=True, blank=True )
    destinations = models.CharField(max_length=50)
    content = models.TextField()
    image_name = models.CharField(
        max_length=100,
        help_text="Enter file name (eg Cancun).",
        default="default.jpg",
        blank=True
    )

    def __str__(self):
        return self.destinations or f"Card for {self.image_name}"
    
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'