from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients, separated by commas")
    steps = models.TextField(help_text="Describe each step for preparation")
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes", null=True, blank=True)
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes", null=True, blank=True)
    servings = models.PositiveIntegerField(help_text="Number of servings", default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

    def total_time(self):
        """Calculate the total time for preparation and cooking"""
        return (self.prep_time or 0) + (self.cook_time or 0)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'

