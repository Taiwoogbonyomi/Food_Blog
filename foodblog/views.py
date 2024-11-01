from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, Comment
from .forms import CommentForm  # Assuming CommentForm is defined for the comment creation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RecipeListView(ListView):
    model = Recipe
    template_name = 'foodblog/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 3

    def get_queryset(self):
        return Recipe.objects.order_by('-created_at') 

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foodblog/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.splitlines()
        context['comments'] = self.object.comments.all()
        return context

@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'foodblog/add_comment.html'

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('recipe_detail', pk=self.object.recipe.pk)

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
