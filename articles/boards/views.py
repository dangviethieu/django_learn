from pickle import FRAME
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Board, Post, Topic

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request=request, template_name='home.html', context={'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', context={'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()
        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )
        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics', pk=board.pk)
    return render(request, 'new_topic.html', context={'board': board})