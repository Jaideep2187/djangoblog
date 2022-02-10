from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'JD',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2008'    
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2008'    
    },  
]
def home(request):
    context={
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})