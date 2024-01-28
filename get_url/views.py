from django.shortcuts import redirect, render
from rest_framework.decorators import api_view 
from shortener.models import URL
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def get_url(request):
    short_url = request.GET.get('short_url')
    try:
        check_url = URL.objects.get(short_url=short_url)
        original_url = check_url.original_url
        check_url.click_count+= 1
        check_url.save()
        return redirect(original_url)
        #return Response({"Error":None},status=status.HTTP_200_OK)
    except URL.DoesNotExist:
        return Response({"Error":"Shorten URL does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"Error":e}, status=status.HTTP_400_BAD_REQUEST)
    