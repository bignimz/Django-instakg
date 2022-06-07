from django.urls import path
from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('<uuid:post_id>/', views.post_detail, name='post-details'),
    path('tag/<slug:tag_slug>/', views.tags, name='tags'),
    path('<uuid:post_id>/like', views.like, name='like'),
]
