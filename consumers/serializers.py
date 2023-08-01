from .models import ConsumUser
from rest_framework import serializers

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumUser
        fields = ('__all__')
        # ('Age','Educations','Career','Award','Introduce','Created','Updated')