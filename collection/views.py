from datetime import datetime

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from collection.forms import ResourceForm
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

def edit_resource(request, slug):
    # grab the object
    resource = Resources.objects.get(slug=slug)
    # set the form we're using
    form_class = ResourceForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=resource)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('resource_detail', slug=resource.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=resource)

    # and render the template
    return render(request, 'resources/edit_resource.html', {
        'resource': resource,
        'form': form,
    })

# add below your edit_thing view
def create_resource(request):
    form_class = ResourceForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            resource = form.save(commit=False)

            # set the additional details
            resource.user = request.user
            resource.slug = slugify(resource.name)

            # save the object
            resource.save()

            # redirect to our newly created thing
            return redirect('resource_detail', slug=resource.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'resources/create_resource.html', {
        'form': form,
    })
