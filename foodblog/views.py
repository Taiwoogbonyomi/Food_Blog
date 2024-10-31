from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import Recipe, Comment

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'foodblog/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 6

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foodblog/recipe_detail.html'

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.splitlines()  # Split by lines here
    return render(request, 'foodblog/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'foodblog/add_comment.html'


