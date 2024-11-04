from django.shortcuts import render

from blog.models import Blog


def blog_list(request):
    context = {}
    context["blog_list"] = Blog.objects.all()
    print(context)
    return render(request, "blog/blog_list.html", context=context)


def show_blog(request, pk):
    context = {}
    context['show_blog'] = Blog.objects.get()
    return render(request, "blog/show_blog.html", context=context)
