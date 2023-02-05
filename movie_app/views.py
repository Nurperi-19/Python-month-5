from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_404_NOT_FOUND)
        # get data from body
        name = serializer.validated_data.get('name')
        # create product by this data
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def directors_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # get data from body
        name = request.data.get('name')
        # update product by this data
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)  #if not serializer.is_valid():
        serializer.is_valid(raise_exception=True)                #return Response(data={'errors': serializer.errors},
                                                                 #status = status.HTTP_404_NOT_FOUND)
        title = serializer.validated_data.get('title')
        duration = serializer.validated_data.get('duration')
        description = serializer.validated_data.get('description')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title, duration=duration, description=description, director_id=director_id
        )
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movies_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = request.data.get('title')
        duration = request.data.get('duration')
        description = request.data.get('description')
        director_id = request.data.get('director_id')
        movie.title = title
        movie.duration = duration
        movie.description = description
        movie.director_id = director_id
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def reviews_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer
        serializer.is_valid(raise_exception=True)

        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review.text = text
        review.movie_id = movie_id
        review.stars = stars
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

