from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import Recipe, Comment

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'foodblog/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 5

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foodblog/recipe_detail.html'

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'foodblog/add_comment.html'

