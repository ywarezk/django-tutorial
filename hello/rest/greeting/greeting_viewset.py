from rest_framework.viewsets import ModelViewSet
from hello.models import Greeting
from hello.rest.greeting.greeting_serializer import GreetingSerializer

class GreetingViewset(ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer

