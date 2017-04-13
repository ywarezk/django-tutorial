from django.shortcuts import render
from hello.models import Greeting
from hello.forms import GreetingForm

def hello_world(request):
    if request.method == "POST":
        my_form = GreetingForm(request.POST)
        valid = my_form.is_valid()
        if valid:
            greeting = my_form.save()
    greetings = Greeting.objects.all()
    my_form = GreetingForm()
    return render(request, 'hello/hello-world.html', context={
        'greeting': "what's up",
        'my_func': lambda : 'hello world from function',
        'my_array': [1,2,3, 'hello'],
        'condition': True,
        'footer_message': 'Gil & Tom',
        'greetings': greetings,
        'greeting_form': my_form
    })



