from django.shortcuts import render, HttpResponse
import datetime


html_base= """<h1> Mi Web Personal</h1>
<ul>
    <li><a href="/"> Home </a> </li>
    <li> <a href="/about-me/"> Acerca de mi </a>  </li>
    <li> <a href="/portafolio/"> Portafolio </a>  </li>
    <li> <a href="/contacto/"> Contacto </a>  </li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")


def portafolio(request):
    return render(request,"core/portafolio.html")


def contacto(request):
    
    return render(request,"core/contacto.html")

