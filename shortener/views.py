import random
import string
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import URLSerializer
from .models import URL
# Create your views here.
@api_view(['POST'])
def shortenURL(request):
    serializer = URLSerializer(data=request.data)
    print("HI")
    if serializer.is_valid():
        print("HIiii")
        original_url = serializer.validated_data['original_url']
        try:
            check_url = URL.objects.get(original_url = original_url)
            return Response({"Error":"Shorten URL already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except URL.DoesNotExist:    
            characters = string.ascii_letters + string.digits
            short_url = ''.join(random.choice(characters) for _ in range(6))
            url = URL(original_url=original_url,short_url=short_url)
            url.save()
            return Response({"long_url":original_url,"shorten_url":short_url})
    return Response({"Error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

