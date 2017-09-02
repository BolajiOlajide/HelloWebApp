from datetime import datetime

from django.shortcuts import render

from collection.models import Resources

# Create your views here.
def index(request): 
    # this is your new view
    resources = Resources.objects.all().order_by('?') # Sort the items randomly
    # The .get() method will retrieve the object that matches the query, but keep in mind it'll 
    # throw an error if more than one object is found (or none.) 
    # If you want to grab a bunch of things that match, you'll use .filter():
	# things = Thing.objects.filter(name='Hello')
	# things = Thing.objects.filter(name='Hello').order_by('name')
	# things = Thing.objects.filter(name__contains='Hello')
    return render(request, 'index.html', {'resources': resources})

def resource_detail(request, slug):
	# grab the object...
    resource = Resources.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'resources/resource_detail.html', {
        'resource': resource,
    })
