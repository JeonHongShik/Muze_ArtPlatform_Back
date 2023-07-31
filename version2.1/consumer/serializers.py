from .models import Consum
from rest_framework import serializers


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consum
        fields = "__all__"
        # ('Age','Educations','Career','Award','Introduce','Created','Updated')
