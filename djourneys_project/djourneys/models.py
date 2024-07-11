from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hours = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
   

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
   

    def __str__(self):
        return self.title


# Create your models here.
