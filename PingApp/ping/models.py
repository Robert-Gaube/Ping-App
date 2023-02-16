from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ip(ip):
     try:
          object = Setup.objects.get(ip=ip)
          raise ValidationError(
               _('%(ip)s is already in the database'),
               params={'ip':ip},
          )
     except:
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
def validate_name(name):
     parts = name.split('-')
     if len(parts) != 4:
          raise ValidationError(
               _('%(name)s is not in the S-S-S-DDD format (S - text of any size, D - digit)'),
               params={'name':name},
          )
     for ch in parts[3]:
          if not ch.isdigit():
              raise ValidationError(
                    _('%(name)s is not in the S-S-S-DDD format (S - text of any size, D - digit)'),
                    params={'name':name},
               ) 
     

class Setup(models.Model):
     name = models.CharField(max_length=50, validators=[validate_name], unique=True)
     ip = models.CharField(max_length=30, validators=[validate_ip], unique=True)
     uefi = models.BooleanField(default=False)
     
     def __str__(self):
          return f'{self.name} - {self.ip}'
     

          
          