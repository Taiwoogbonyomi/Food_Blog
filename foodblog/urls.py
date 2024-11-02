from django.urls import path
from .views import RecipeListView, RecipeDetailView, CommentCreateView, recipe_upvote, recipe_downvote, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('recipe/<int:pk>/upvote/', recipe_upvote, name='recipe_upvote'),
    path('recipe/<int:pk>/downvote/', recipe_downvote, name='recipe_downvote'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'), 
]