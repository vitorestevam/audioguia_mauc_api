from django.urls import include, path
from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register(r"guides", views.GuideList)

urlpatterns = [
    path("api/", include(api_router.urls)),
]