from django.urls import path
from .views import CreateRecipe, RecipeRecommendView, RecipeDetailDeleteView, RecipeCategoryListView, RecipeSearchKeywordView

urlpatterns = [
    # /api/v1/recipes
    path("", CreateRecipe.as_view(), name="create-recipe"),
    # /api/v1/recipes/1
    path("/<int:id>", RecipeDetailDeleteView.as_view(), name="detail-recipe"),
    # /api/v1/recipes/category/book
    path("/category/<str:category>", RecipeCategoryListView.as_view(), name="category-recipe"),
    # /api/v1/recipes/search/%EA%B3
    path("/search/<str:keyword>", RecipeSearchKeywordView.as_view(), name="keyword-recipe"),
    # /api/v1/recipes/recommend
    path("/recommend", RecipeRecommendView.as_view(), name="recommend-recipe"),
]