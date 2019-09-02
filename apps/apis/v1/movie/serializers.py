from rest_framework import serializers

from apps.movie import models
from apps.utils.serializers import ChoicesField

from apps.apis.v1.user.serializers import UserModelSerializer


class MovieImageModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = models.MovieImage
        fields = ('id', 'user', 'path')


class VoteSerializer(serializers.ModelSerializer):
    vote = ChoicesField(choices=models.Vote.VOTE_TYPE)
    user = UserModelSerializer()

    class Meta:
        model = models.Vote
        fields = ('id', 'user', 'vote')


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = ('id', 'name')


class MoviePersonModelSerializer(serializers.ModelSerializer):
    movie = MovieModelSerializer()

    class Meta:
        model = models.MoviePerson
        fields = ('movie', 'detail')


class PersonListSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = ('id', 'name')


class PersonDetailSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    writer = serializers.SerializerMethodField()

    class Meta:
        model = models.Person
        fields = ('id', 'name', 'date_of_birth', 'died_on', 'actor',
                  'director', 'writer')

    def get_actor(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.actors(),
                                          many=True).data

    def get_director(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.directors(),
                                          many=True).data

    def get_writer(self, obj):
        return MoviePersonModelSerializer(obj.movieperson_set.writers(),
                                          many=True).data


class MovieDetailSerializer(serializers.ModelSerializer):
    rating = ChoicesField(choices=models.Movie.RATING_TYPE)

    class Meta:
        model = models.Movie
        fields = ('id', 'name', 'plot', 'rating')
