from catalog.serializers import BookSerializer
from rest_framework import viewsets
from catalog.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer