from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('memos/', views.memos_index, name='memos_index'),
    path('memos/search/', views.MemoList.as_view(), name='memos_search'),
    path('memos/<int:pk>/', views.MemoDetail.as_view(), name='memos_detail'),
    path('memos/create/', views.MemoCreate.as_view(), name='memos_create'),
    path('memos/<int:pk>/update/', views.MemoUpdate.as_view(), name='memos_update'),
    path('memos/<int:pk>/delete/', views.MemoDelete.as_view(), name='memos_delete'),
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
    path('memos/<int:memos_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('accounts/signup/', views.signup, name='signup')
   
]
