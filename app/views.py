from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def listado(request):
    return render(request,'listado.html')


def create_post(request):
    if request.method == 'POST':
        form=CreatePostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            obj=form.instance
            return render(request,"create_post.html",{"obj":obj})
    else:
        return render(request,'create_post.html',{'form':CreatePostForm})

def view_post(request):
    post=Post.objects.all()
    print(post)
    return render(request,'view_post.html', {'posts':post})

def delete_post(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        post.delete()
        return redirect('view_post')

    