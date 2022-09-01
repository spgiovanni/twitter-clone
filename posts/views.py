from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.template import loader

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            # If yes save it
            form.save()
            # Redirect Home
            return HttpResponseRedirect('/')
        else:

            #If NO show error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    # Show
    return render(request, 'posts.html',
                {'posts': posts}
    )


def delete (request,post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect('/')    

def edit (request,post_id):
        post = Post.objects.get(id=post_id)
        template = loader.get_template('update_post.html')
        context = { 'post' }
        return HttpResponse(template.render(context, request))