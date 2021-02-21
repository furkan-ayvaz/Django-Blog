from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def add(request):
    form = ArticleForm(request.POST or None)
    
    if form.is_valid():
        content = form.cleaned_data.get("content")
        title = form.cleaned_data.get("title")

        newArticle = Article(title = title, content = content)
        newArticle.author = request.user
        newArticle.save()
        messages.success(request,"Article added successfully  ...")
        return redirect("article:dashboard")
    return render(request,"addArticle.html",{"form":form})


@login_required(login_url="user:login")
def showArticle(request):
    articles = Article.objects.filter(author = request.user)
    return render(request,"dashboard.html",{"articles" : articles})


def detailArticle(request,id):
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})


@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"The article updated successfully ")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"The article deleted successfully ")
    return redirect("article:dashboard")


def all_Article(request):
    articles = Article.objects.all()
    return render(request,"index.html",{"articles":articles})


def find(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        if articles:
            return render(request,"find.html",{"articles":articles})
        messages.info(request,"There is not article this name !!!")
        return render(request,"find.html")
    return render(request,"find.html")

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()   
    return redirect(reverse("article:detail",kwargs={"id":id}))
