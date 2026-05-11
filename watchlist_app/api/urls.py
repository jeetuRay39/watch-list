from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieListAPIView, MovieDetailAPIView



# urlpatterns = [

#     path('list/', movie_list , name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie-details'),
# ]

urlpatterns = [
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
]