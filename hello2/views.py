from django.shortcuts import render

# Create your views here.
def say_hello2(request):
    return render(request, 'hello2/hello.html')