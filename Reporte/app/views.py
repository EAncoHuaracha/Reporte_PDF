
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from app.render_pdf import html2pdf

from .models import Parasito

# Create your views here.
def home(request):
    p = Parasito.objects.all()
    return render(request,'home.html', {'p': p})

def pdf(request):
    p = Parasito.objects.all()
    data = {
            'p': p
    }
    pdf=html2pdf('pdf.html',data)
    return HttpResponse(pdf,content_type="application/pdf")