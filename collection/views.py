from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request): 
    # this is your new view
    now = datetime.now()
    return render(request, 'index.html', {'name': 'Bolaji', 'now': now })
