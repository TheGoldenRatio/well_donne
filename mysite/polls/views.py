from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World. THis is a website. it\'ll be the best john donne database soon...' )
