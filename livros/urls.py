from django.urls import path

from livros.views import LivroCreate, LivroList

app_name = 'livros'


urlpatterns = [
    path('livros/', LivroList.as_view()),
    path('livros/new', LivroCreate.as_view()),
]
