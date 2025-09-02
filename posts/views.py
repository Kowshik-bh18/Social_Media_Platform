from django.shortcuts import render,redirect
from .forms import Postcreateform,CommentForm
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.
@login_required
def Post_create(request):
    if request.method=="POST":
        form = Postcreateform(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = Postcreateform(data=request.GET)
    return render(request,"posts/post_create.html",{'form':form})

def feed(request):
    if request.method=="POST":
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Posts,id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    post = Posts.objects.all()
    logged_user = request.user
    return render(request,'posts/all_posts.html',{'post':post,'logged_user':logged_user,'comment_form':comment_form,})


@login_required
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Posts, id=post_id)

        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            liked = False
        else:
            post.liked_by.add(request.user)
            liked = True
        
        # Return JSON response for AJAX
        return JsonResponse({
            'success': True,
            'liked': liked,
            'like_count': post.liked_by.count()
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
