from rest_framework import serializers
from .models import City, Attraction, Review

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city-detail-api',
        read_only=True
    )

    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'hours', 'city')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction-detail-api',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'title', 'comment', 'rating', 'attraction')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attraction-detail-api',
        many=True,
        read_only=True
    )

    reviews = serializers.HyperlinkedRelatedField(
        view_name='review-detail-api',
        many=True,
        read_only=True
    )

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'population', 'attractions', 'reviews')
