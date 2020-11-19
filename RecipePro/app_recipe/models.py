from django.db import models

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredient_list = models.TextField()
    making_process = models.TextField()

