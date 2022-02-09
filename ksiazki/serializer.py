from rest_framework import serializers

from .models import ksiazki


class ksiazkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ksiazki
        # fields=['__all__']
        fields = ['tytuł', 'autor', 'jezyk', 'data', 'strony', 'ISBN']
