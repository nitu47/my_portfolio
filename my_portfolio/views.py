from django.shortcuts import render, redirect
from .models import Project, Message, Photo, Certificate
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    photos = Photo.objects.all()
    certificates = Certificate.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')

        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=msg
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')

    context = {
        "name": "Nitu Kumari",
        "bio": "Computer Engineering student passionate about Python, Django, and AI.",
        "skills": ["Python", "Django", "HTML", "CSS", "Bootstrap", "AI Tools"],
        "socials": {
            "github": "https://github.com/nitu47",
            "linkedin": "https://www.linkedin.com/in/nitu-kumari-442100365/",
            "email": "nitu.kumari70386@gmail.com",
        },
        "projects": projects,
        "photos": photos,
        "certificates": certificates,
    }

    return render(request, 'my_portfolio/home.html', context)
