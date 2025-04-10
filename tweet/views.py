from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import tweetForm,userRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def abouts(request):
    return render(request, 'abouts.html')

def tweetList(request):
    tweets = Tweet.objects.all().order_by('-createdOn')
    return render(request, 'tweetList.html', {'tweets': tweets})

def tweetCreate(request):
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('tweetList')
            else:
                return redirect('login')
    else:
        form = tweetForm()
    return render(request, 'tweetForm.html', {'form': form})

@login_required
def tweetEdit(request, tweetID):
    tweet = get_object_or_404(Tweet, pk=tweetID, user=request.user)
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweetList')
    else:
        form = tweetForm(instance=tweet)
    return render(request, 'tweetForm.html', {'form': form})

@login_required
def tweetDelete(request, tweetID):
    tweet = get_object_or_404(Tweet, pk=tweetID, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweetList')
    return render(request, 'tweetDelete.html', {'tweet': tweet})


def register(request):
    if request.method=='POST':
        form=userRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweetList')
    else:
        form=userRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
