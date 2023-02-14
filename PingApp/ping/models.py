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
     try:
          object = Setup.objects.get(name=name)
          raise ValidationError(
               _('%(name)s is already in the database'),
               params={'name':name},
          )
     except:
          pass
class Setup(models.Model):
     name = models.CharField(max_length=50, validators=[validate_name], unique=True)
     ip = models.CharField(max_length=30, validators=[validate_ip], unique=True)
     uefi = models.BooleanField(default=False)
     
     def __str__(self):
          return f'{self.name} - {self.ip}'
          