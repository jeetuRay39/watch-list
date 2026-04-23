from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieListAPIView


# urlpatterns = [

#     path('list/', movie_list , name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie-details'),
# ]

urlpatterns = [
    path('list/', MovieListAPIView.as_view(), name='movie-lsit'),
]