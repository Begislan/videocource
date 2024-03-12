from django.shortcuts import render
from django.views.generic.detail import DetailView
from app.models import Video, User,Type


# Create your views here.
def core(request):
    return render(request, 'app/index.html')

def videos(request):
    video = Video.objects.all()
    context = {
        'video': video
    }

    return render(request, 'app/video/video.html', context)

class VideoDetailView(DetailView):
    model = Video
    template_name = 'app/video/detail_videos.html'

def mentors(request):
    user = User.objects.all()
    return render(request, 'app/mentor/mentor_list.html', {'user': user})

def mentor_details(request,pk):
    videos = Video.objects.filter(user__id=pk)
    user = videos.all()
    return render(request, 'app/mentor/mentor.html', {'user': user, "videos": videos})

def category(request):
    category = Type.objects.all()
    return render(request, 'app/category/category_list.html', {'category': category})

def category_details(request,pk):
    videos = Video.objects.filter(type__id=pk)
    type = videos.all()
    return render(request, 'app/category/category_details.html', {'type': type, "videos": videos})





















