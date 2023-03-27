from django.urls import include, path, re_path
from django.http.response import HttpResponse
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from django.contrib import admin

urlpatterns = [
    path(r"graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("admin/", admin.site.urls),
]
