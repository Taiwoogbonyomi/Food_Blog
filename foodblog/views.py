from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import Recipe, Comment
from django.contrib.auth.decorators import login_required

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


def add_comment(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()

    return render(request, 'foodblog/add_comment.html', {'form': form, 'recipe': recipe})



@login_required
def recipe_upvote(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.upvotes += 1
    recipe.save()
    return redirect('recipe_detail', pk=pk)

@login_required
def recipe_downvote(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.downvotes += 1
    recipe.save()
    return redirect('recipe_detail', pk=pk)