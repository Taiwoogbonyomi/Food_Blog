from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.db import IntegrityError

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients, separated by commas")
    steps = models.TextField(help_text="Describe each step for preparation")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    upvotes = models.IntegerField(default=0)  
    downvotes = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

def save(self, *args, **kwargs):
    if not self.slug:
        original_slug = slugify(self.title)
        self.slug = original_slug
        counter = 1
        while Recipe.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
    super().save(*args, **kwargs)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'
