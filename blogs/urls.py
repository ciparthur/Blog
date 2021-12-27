from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo_post/', views.novo_post, name='novo_post'),
    path('editar_post/<int:post_id>', views.editar_post, name='editar_post'),
    path('post/<int:post_pk>', views.post, name='post'),
]
