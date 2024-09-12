from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    project_list = [
        {"name": "Project 1", "status": "Completed", "details": "Details of project 1"},
        {"name": "Project 2", "status": "Ongoing", "details": "Details of project 2"}
    ]
    return render(request, 'projects.html', {'projects': project_list})

def documents(request):
    documents_list = [
        {"name": "Resume", "link": "/static/docs/resume.pdf"},
        {"name": "Certificate 1", "link": "/static/docs/certificate1.pdf"},
    ]
    return render(request, 'documents.html', {'documents': documents_list})

from django.http import HttpResponse
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        return HttpResponse(f"Thanks for reaching out, {name}!")
    return render(request, 'contact.html')
