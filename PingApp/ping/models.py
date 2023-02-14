from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ip(ip):
     for char in ip:
          if char.isalpha():
               raise ValidationError(
                    _('%(ip)s contains letters'),
                    params={'ip':ip},
               )
          if char == ' ':
                raise ValidationError(
                    _('%(ip)s contains spaces'),
                    params={'ip':ip},
               )
     
class Setup(models.Model):
     name = models.CharField(max_length=50)
     ip = models.CharField(max_length=30, validators=[validate_ip])

     def __str__(self):
          return f'{self.name} - {self.ip}'
          