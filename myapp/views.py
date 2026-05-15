from django.shortcuts import render,redirect
from .models import Profile



def dashboard(request):
    resumes = Profile.objects.all()
    return render(request,'myapp/dashboard.html',{'resumes':resumes})
    

# Create your views here.
def save_profile(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        profile = Profile(name=name,email=email,phone =phone,degree=degree,university=university,summary=summary,  previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('dashboard')
    
    return render(request,'myapp/accept.html')

def resume(request,id):
    user_profile=Profile.objects.get(id=id)
    return render(request,'myapp/resume.html',{'user_profile':user_profile})

