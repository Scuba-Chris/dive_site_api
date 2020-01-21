from rest_framework import serializers
from .models import DiveSite

class DiveSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveSite
        fields = [
            'id', 'author', 'title', 'created_at',
        ]