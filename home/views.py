from django.shortcuts import redirect, render
from .models import Education, Experience, Skill, PortfolioDetail
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    skills=Skill.objects.all()
    education = Education.objects.all()[::-1]
    experience = Experience.objects.all()[::-1]
    details = PortfolioDetail.objects.all()
    # email configuration

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        email_subject = "You have new message from Portfolio website regarding"+ subject
        message_body  = 'Name:' +name + '.Email:' +email +'.Message:'+message
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 
        send_mail(
        email_subject,
        message_body,
        'aiswaryaasubash@gmail.com',
        [admin_email],
        fail_silently=False,
    )
        messages.success(request,"Thank you for contacting us ")
        return redirect('index')



    return render(request,'home/index.html',{
        'skills':skills,
        'education':education,
        'experience':experience,
        'details':details
    })
def portfolio_details(request,id):
    details = PortfolioDetail.objects.get(pk=id)
    return render(request,'home/portfolio-details.html',{
        "details":details,
    })