from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

# @api_view()
# def movie_list(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)

# @api_view()
# def movie_details(request, pk):
#     movies = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movies)
#     return Response(serializer.data)

class MovieListAPIView(APIView):
    def get(self, request):
        #query set for getting the objects
        movies = Movie.objects.all()
        #serializing the objects 
        serializer = MovieSerializer(movies, many=True)
        # many = Ture because we are serializing multiple objects
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        #serializing the incoming json data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class MovieDetailAPIView(APIView):

    def get(self, request, pk):
        #queryset for getting the specific object
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'message':'deleted'})




