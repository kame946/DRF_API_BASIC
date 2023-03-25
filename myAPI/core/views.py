from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET'])
def core(request):
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response({'status': 200, 'payload': serializer.data})

@api_view(['POST'])
def post_details(request):
    data = request.data
    print(data)
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'message': "Something went wrong"})

    return Response({'status': 200, 'paylaod': data, 'message': 'sent'})