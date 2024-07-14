from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from .forms import CreateUserForm, CustomAuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from django.contrib import messages
from django.contrib.auth import logout
 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from . import serializers
from . import models
from . import permissions

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.has_error:
            print(form.error_messages)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    else:
        form = CreateUserForm()

    return render(request, 'registration/register.html', {'form':form})


@login_required(login_url='login')
def dashboard(request):

    users = models.UserProfile.objects.first()
    context = {'records': users}

    return render(request, 'index/dashboard.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logoutUser(request):

    logout(request)
    messages.success(request, "Logout success!")

    return redirect("login")

class UserProfileViewSet1(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserProfileViewSet2(APIView):
    
    def get(self, request):

        form = CreateUserForm()
        context = {'form':form}

        return render(request, 'registration/register.html', context=context)

    def post(self, request, format=None):
        
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= status.HTTP_201_CREATED)  # serializer.data döndürülüyor
        
        return Response(serializer.errors, status=400)


class UserProfileViewSet3(viewsets.ViewSet):

    def list(self, request):

        form = CreateUserForm()
        context = {'form':form}

        return render(request, 'registration/register.html', context=context)

    def create(self, request, format=None):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=400)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer_class = AuthTokenSerializer
        user = get_object_or_404(models.UserProfile, username=request.data['name'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = serializers.UserProfileSerializer(user)

        return Response({'token': token.key, 'user': serializer.data})
