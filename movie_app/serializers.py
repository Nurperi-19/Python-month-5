from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    class Meta:
        model = Movie
        fields = 'title duration director'.split()

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['text', 'movie']
