from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
        # fields = ('id','Name','Email','Profile','Created','Updated')