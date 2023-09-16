from rest_framework import serializers
from todos import *


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo