from django.shortcuts import render
from hello.models import Greeting

def hello_world(request):
    greetings = Greeting.objects.all()
    return render(request, 'hello/hello-world.html', context={
        'greeting': "what's up",
        'my_func': lambda : 'hello world from function',
        'my_array': [1,2,3, 'hello'],
        'condition': True,
        'footer_message': 'Gil & Tom',
        'greetings': greetings
    })



