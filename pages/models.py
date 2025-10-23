from django.db import models

# Create your models here.
# pages/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # phone = models.CharField(max_length=11, blank=True, null=True)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}> - {self.date_sent:%Y-%m-%d %H:%M}"


