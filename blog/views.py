from django.shortcuts import render

from django.db.models import Q

from django.core.exceptions import ObjectDoesNotExist

from blog.models import Blog


def blog_list(request):
    context = {}
    context["blog_list"] = Blog.objects.all()
    print(context)
    return render(request, "blog/blog_list.html", context=context)


def show_blog(request, content):
    context = {}
    
    try:
        context['show_blog'] = Blog.objects.filter(Q(title__icontains=content) | Q(content__icontains=content))[:1].get()
        if context['show_blog']:
            return render(request, 'blog/show_blog.html', context=context)   
    except ObjectDoesNotExist:
        return render(request, 'blog/blog_list.html') 
