from rest_framework import generics

from livros.serializers import LivroSerializer
from livros.models import Livro


class LivroList(generics.ListAPIView):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroCreate(generics.CreateAPIView):
    serializer_class = LivroSerializer
