from django.shortcuts import render, get_object_or_404
from .models import Course, Topic

def home(request):
    return render(request, 'home.html')

def topic_list(request):
    topics = Topic.objects.all()
    return render(request,'courses/topic_list.html',{'topics':topics})

def topic_detail(request,pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'courses/topic_detail.html', {'topic':topic})

def course_detail(request, course_pk, topic_pk):
    course=get_object_or_404(Course, topic_id=topic_pk, pk=course_pk)
    return render(request, 'courses/course_detail.html', {'course':course})
