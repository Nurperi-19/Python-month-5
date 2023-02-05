from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = 'text movie stars'.split()

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'title duration director rating reviews'.split()

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        directors = Director.objects.filter(id=director_id)
        if len(directors) == 0:
            raise ValidationError(f'Director with id({director_id}) does not exist')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        movies = Movie.objects.filter(id=movie_id)
        if len(movies) == 0:
            raise ValidationError(f'Movie with id({movie_id}) does not exist')
        return movie_id
