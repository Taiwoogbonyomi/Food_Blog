from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, Comment
from .forms import CommentForm  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages


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
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            
            # Add success message
            messages.success(request, 'Your comment has been posted successfully!')

            return redirect('recipe_detail', pk=recipe.pk)

        return render(request, 'recipe_detail.html', {
            'recipe': recipe,
            'form': form,
        })

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = CommentForm()
        return render(request, 'recipe_detail.html', {
            'recipe': recipe,
            'form': form,
        })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your desired page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

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
