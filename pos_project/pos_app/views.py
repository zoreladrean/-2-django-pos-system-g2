from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'POS Home'}
    return render(request, 'pos_app/index.html', context)