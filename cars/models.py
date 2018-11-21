from django.db import models
from datetime import datetime
from salesmen.models import Salesman

MAKE = (
  ("bmw", "BMW"),
  ("mercedes", "MERCEDES BENZ"),
  ("toyota", "TOYOTA"),
  ("honda", "HONDA"),
  ("hyundai", "HYUNDAI"),
  ("acura", "ACURA"),
  ("nissan", "NISSAN"),
  ("audi", "AUDI"),
  ("mazda", "MAZDA"),
  ("dodge", "DODGE"),
  ("ford", "FORD"),
  ("kia", "KIA"),

  )



class Cars(models.Model):
  salesman = models.ForeignKey(Salesman, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  make = models.CharField(max_length=200, choices=MAKE)
  model = models.CharField(max_length=200)
  year = models.IntegerField()
  odometer = models.IntegerField()
  engine = models.DecimalField(max_digits=2, decimal_places=1)
  transmission = models.CharField(max_length=10, blank=True, default='Unknown')
  price = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.title

