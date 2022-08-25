from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()

    @action(detail=False)
    def books_by_publishing_company(self,request):
        publishing_company = request.query_params['publishing']
        book_list = models.Books.objects.filter(publishing_company = publishing_company)

        serializers = self.get_serializer(book_list, many= True)
        return Response(serializers.data)

    @action(detail=False)
    def books_by_author(self,request):
        author = request.query_params['author']
        book_list = models.Books.objects.filter(author = author)

        serializer = self.get_serializer(book_list,  many=True)
        return Response(serializer.data)



    @action(detail=False)
    def books_by_id(self, request):
        id = request.query_params['id']
        book = models.Books.objects.filter(id_book=id)

        serializer = self.get_serializer(book, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def book_by_name(self,request):
        name = request.query_params['name']
        book = models.Books.objects.filter(title = name)

        serializer = self.get_serializer(book,  many=True)
        return Response(serializer.data)


    @action(detail=False)
    def books_by_author(self,request):
        author = request.query_params['author']
        book_list = models.Books.objects.filter(author = author)

        serializer = self.get_serializer(book_list,  many=True)
        return Response(serializer.data)

    