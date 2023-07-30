from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ConsumUser
from .serializers import ConsumerSerializer


class ConsumList(APIView):
    def get(self, request):
        queryset = ConsumUser.objects.all()
        serializer = ConsumerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumDetail(APIView):
    def get_object(self, pk):
        try:
            return ConsumUser.objects.get(pk=pk)
        except ConsumUser.DoesNotExist:
            return None

    def get(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ConsumerSerializer(consum_user)
        return Response(serializer.data)

    def put(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ConsumerSerializer(consum_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consum_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
