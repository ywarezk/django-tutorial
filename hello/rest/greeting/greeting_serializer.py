from rest_framework.serializers import ModelSerializer
from hello.models import Greeting

class GreetingSerializer(ModelSerializer):
    class Meta:
        model = Greeting
        exclude = ()

