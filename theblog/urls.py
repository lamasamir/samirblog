
from django.urls import path,include
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView,DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
urlpatterns = [
    # path('',views.home, name='home')
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article"),
    path('addpost/',AddPostView.as_view(), name="addpost"),
    path('article/edit/<int:pk>/',UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove/',DeletePostView.as_view(), name="delete_post"),
    path('addcategory/',AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name="category_list"),
    path('like/<int:pk>',LikeView, name="like_post"),
    path('article/<int:pk>/comments/',AddCommentView.as_view(), name="add_comments")
    
]