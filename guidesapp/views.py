from .models import Guide
from .serializers import GuideSerializer
from rest_framework import viewsets

# Create your views here.

class GuideList(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer