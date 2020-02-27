from django.db import models

# Create your models here.
class Allrecipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    chef = models.CharField(max_length=200)
    def __str__(self): #we use the string here so our database can display the names as strings not the primary in integers
        return self.recipe_name


class details(models.Model):
    food_class = models.ForeignKey(Allrecipes, on_delete=models.CASCADE)#models.CASCADE is used incase anything is deleted in the Allrecipes section
    food_state = models.CharField(max_length=500)
    food_taste = models.CharField(max_length=500)
    def __str__(self):
        return self.food_state
