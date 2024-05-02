from django.shortcuts import render, redirect
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
# def post_creation(request):
#     if request.method == 'POST':
#         form = PostCreationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('index')
#     else:
#         form = PostCreationForm(data = request.GET)
#     return render(request, 'posts/post_creation.html', {'form': form})
