from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from .models import  MusicfileInfo,record_user_click
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import uuid, random
from django.views.decorators.csrf import csrf_exempt
import random


def index(request):
    return render(request,'music_app/html/index.html')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
def signup(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # Check if they provided a profile picture
            #if 'profile_pic' in request.FILES:
            #    print('found it')
            #    # If yes, then grab it from the POST form reply
            #    profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'music_app/html/signup.html',
                          {'user_form':user_form,
                          'profile_form':profile_form,
                           'registered':registered})
def signin(request):

    if request.method == 'POST':
        # First get the username and password supplied
        email = request.POST.get('email')
        password = request.POST.get('password')
        Userlog = User.objects.get(email=email)
        username = Userlog.username

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'music_app/html/signin.html', {})
def discover(request):
    
    post_music = MusicfileInfo.objects.all()
    print(post_music[0].musicid)
    
    num_entities = MusicfileInfo.objects.all().count()
    rand_entities = random.sample(range(num_entities), 5)
    sample_entities =MusicfileInfo.objects.filter(id__in=rand_entities)
    rand_entities_1 = random.sample(range(num_entities), 6)
    sample_entities_1 =MusicfileInfo.objects.filter(id__in=rand_entities_1)
    
    if request.user.is_authenticated:
        return render(request, 'music_app/html/discover.html', {'post_music':post_music,'sample_entities':sample_entities,'sample_entities_1':sample_entities_1})
    else:
        return HttpResponseRedirect(reverse('signin'))
def genres(request):
    post_music = MusicfileInfo.objects.all()
    print(post_music[0].musicid)
    return render(request, 'music_app/html/genres.html', {'post_music':post_music,'session_id': session_id(request)})
def music_detail(request, pk):
    post = MusicfileInfo.objects.get(musicid=pk)
    return render(request, 'music_app/html/item.detail.html', {'post_music': post})
def session_id(request):
    if not "session_id" in request.session:
        request.session["session_id"] = str(uuid.uuid1())
 
    return request.session["session_id"]

@csrf_exempt
def log(request):
    if request.method == 'POST':
        record = record_user_click()
        record.user_id = request.POST['userid']
        record.musicid = request.POST['music_id']
        record.session_id = request.POST['sessionid']
        record.save()
    return HttpResponse("")