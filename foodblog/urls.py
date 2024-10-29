from django.urls import path
from .views import RecipeListView, RecipeDetailView, CommentCreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
]