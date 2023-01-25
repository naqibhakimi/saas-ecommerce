from django.urls import include, path, re_path
from django.http.response import HttpResponse

def index(request):
    return HttpResponse('Wellcome to ecommerce')

urlpatterns = [
    path('', index)
]