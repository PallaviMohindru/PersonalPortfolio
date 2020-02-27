from django.shortcuts import render, get_object_or_404
from .models import blog

def allblogs(request):
    blogs = blog.objects
    return render(request,'blog/allblogs.html', {'blogs': blogs})

def blogdetail(request,blog_id):
    blog_detail = get_object_or_404(blog, pk = blog_id)
    return render(request,'blog/blogdetail.html',{'blogdetail': blog_detail})
