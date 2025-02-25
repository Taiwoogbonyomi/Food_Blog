from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Comment, Category
from .forms import CommentForm
from django.urls import reverse_lazy
from django import forms


class RecipeListView(ListView):
    model = Recipe
    template_name = 'foodblog/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 3

    def get_queryset(self):
        return Recipe.objects.all().order_by('-created_at')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foodblog/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.splitlines()
        context['comments'] = self.object.comments.order_by('-created_at')
        context['form'] = CommentForm()
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'foodblog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


def recipes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)

    return render(
        request,
        'foodblog/recipes_by_category.html',
        {'recipes': recipes, 'category': category}
    )


@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'foodblog/recipe_detail.html'

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form.instance.recipe = recipe
        form.instance.author = self.request.user
        messages.success(
            self.request, 'Your comment has been posted successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        context['recipe'] = recipe
        context['comments'] = recipe.comments.order_by('-created_at')
        return context


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Write your comment here...'
                       }),
        }
        labels = {
            'content': 'Comment',
        }


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'foodblog/comment_update.html'

    def get_success_url(self):
        return reverse_lazy(
            'recipe_detail', kwargs={'pk': self.object.recipe.pk}
        )

    def test_func(self):
        return self.request.user == self.get_object().author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'foodblog/comment_confirm_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy(
            'recipe_detail', kwargs={'pk': self.object.recipe.pk}
        )

    def test_func(self):
        return self.request.user == self.get_object().author


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome, {username}! Your account has been created.'
            )
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
            messages.success(request, 'Logged in successfully!')
            return redirect('recipe_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def recipe_upvote(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.user in recipe.upvotes.all():
        recipe.upvotes.remove(request.user)
        messages.info(request, 'You removed your upvote.')
    else:
        recipe.upvotes.add(request.user)
        recipe.downvotes.remove(request.user)
        messages.success(request, 'You upvoted this recipe!')

    return redirect('recipe_detail', pk=pk)


@login_required
def recipe_downvote(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.user in recipe.downvotes.all():
        recipe.downvotes.remove(request.user)
        messages.info(request, 'You removed your downvote.')
    else:
        recipe.downvotes.add(request.user)
        recipe.upvotes.remove(request.user)
        messages.success(request, 'You downvoted this recipe!')

    return redirect('recipe_detail', pk=pk)
