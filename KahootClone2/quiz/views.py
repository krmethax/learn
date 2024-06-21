from django.shortcuts import render
from django.http import *
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from django.http import JsonResponse

# Create your views here.
def home(req):
    return HttpResponse('This is quiz home')

def create(req):
    return HttpResponse('Create a quizz ...')

def pdf(req):
    #how to retern a pdf
    buf = io.BytesIO()
    p = canvas.Canvas(buf)
    p.drawString(100, 100, 'Hello, world.')
    p.showPage()
    p.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='hello.pdf')

def json(req):
    return JsonResponse({
        'name': 'Kahoot',
        'age': 10,
        'gpa': 4.00
        })

def bg(req):
    f = open('quiz/birthday.jpg', 'rb')
    return FileResponse(f)