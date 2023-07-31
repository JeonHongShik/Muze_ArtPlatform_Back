from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Consum
from .serializers import ConsumerSerializer

# Create your views here.
class ConsumList(APIView):
    def get(self, request):
        queryset = Consum.objects.all()
        serializer = ConsumerSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class ConsumDetail(APIView):
    def get_object(self, pk):
        try:
            return Consum.objects.get(pk=pk)
        except Consum.DoesNotExist:
            return None

    def get(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)
        serializer = ConsumerSerializer(consum_user)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)
        serializer = ConsumerSerializer(consum_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk):
        consum_user = self.get_object(pk)
        if not consum_user:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)
        consum_user.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)
