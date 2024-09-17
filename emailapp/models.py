from django.db import models
from .utils import validate_custom_email
# Create your models here.


class EmailPost(models.Model):
    email = models.EmailField(validators=[validate_custom_email])
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email