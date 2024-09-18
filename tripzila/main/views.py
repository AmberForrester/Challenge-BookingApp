from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

#Homepage - landing page view -
def homepage(request):
    template = loader.get_template('homepage.html') #Load the homepage.html template.
    return HttpResponse(template.render()) #Outputs the HTML rendered by template. 
