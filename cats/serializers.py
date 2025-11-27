from rest_framework import serializers

from .models import Cat, Owner


class CatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner')


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
