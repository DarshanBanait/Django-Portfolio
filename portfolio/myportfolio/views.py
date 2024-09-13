from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})
    
    project = get_object_or_404(projects, id=project_id)
    
    return render(request, 'project_detail.html', {'project': project})

def documents(request):
    documents_list = [
        {"name": "Resume", "link": "/static/docs/resume.pdf"},
        {"name": "Certificate 1", "link": "/static/docs/certificate1.pdf"},
    ]
    return render(request, 'documents.html', {'documents': documents_list})

from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        return render(request, 'thank_you.html', {'name': name})
    return render(request, 'contact.html')

