from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
     RecipeListView, RecipeDetailView, CommentCreateView,
     recipe_upvote, recipe_downvote, signup, CommentUpdateView
    )
from . import views

urlpatterns = [
    path(
        '', RecipeListView.as_view(),
        name='recipe_list'
    ),
    path(
        'recipe/<int:pk>/',
        RecipeDetailView.as_view(),
        name='recipe_detail'
    ),
    path(
        'recipe/<int:pk>/comment/',
        CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        'comment/<int:pk>/update/',
        CommentUpdateView.as_view(),
        name='comment_update'
    ),
    path(
        'recipe/<int:pk>/upvote/',
        recipe_upvote,
        name='recipe_upvote'
    ),
    path(
        'recipe/<int:pk>/downvote/',
        recipe_downvote,
        name='recipe_downvote'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='account_logout'
    ),
    path(
        'login/',
        views.custom_login,
        name='home'
    ),
    path(
        'signup/',
        signup,
        name='signup'
    ),
]
