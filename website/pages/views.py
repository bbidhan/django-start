from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader

def home(request):
    '''
    This is the homepage of the website.
    '''

    template = loader.get_template('pages/index.html')

    context = RequestContext(request, {
        'title': "Blah : Motto Blah",
        'menuindex': 1,
    })
    return HttpResponse(template.render(context))
