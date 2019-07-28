from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'content':'hej'}
    return render(request, 'test/index.html', context)
