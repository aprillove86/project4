from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('memos/', views.MemoList.as_view(), name='memos_index'),
    path('memos/<int:pk>/', views.MemoDetail.as_view(), name='memos_detail'),
    path('memos/create/', views.MemoCreate.as_view(), name='memos_create'),
    path('memos/<int:pk>/update/', views.MemoUpdate.as_view(), name='memos_update'),
    path('memos/<int:pk>/delete/', views.MemoDelete.as_view(), name='memos_delete'),
    path('accounts/signup/', views.signup, name='signup')
   
]
