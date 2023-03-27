from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activities')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)


    def __str__(self):
        return self.name
    

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    prix_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    nombre_etoiles = models.CharField(max_length=10)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name