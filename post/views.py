from rest_framework.views import APIView
from .models import PerformancePost
from .serializers import PostSerializer
from rest_framework import status
from django.http import JsonResponse


# Create your views here.
class PostList(APIView):
    def get(self, request):
        queryset = PerformancePost.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return PerformancePost.objects.get(pk=pk)
        except PerformancePost.DoesNotExist:
            return None

    def get(self, request, pk):
        post_user = self.get_object(pk)
        if not post_user:
            return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post_user)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        post_user = self.get_object(pk)
        if not post_user:
            return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post_user = self.get_object(pk)
        if not post_user:
            return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
        post_user.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
