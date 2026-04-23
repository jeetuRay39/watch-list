from rest_framework import serializers
from watchlist_app.models import Movie

#serializer class
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#ModelSerializer class

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        #sepecific field include
        # fields = ['name', 'description']

        #excluding the fields
        # fields = ['name', 'description']