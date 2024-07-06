from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, Cancellation, Return, Refund
from .serializers import OrderSerializer, CancellationSerializer, ReturnSerializer, RefundSerializer
from .services import create_order, cancel_order, return_order, process_refund
from .forms import OrderForm, CancellationForm, ReturnForm, RefundForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            errmsg = form.errors
    else:
        form = SignUpForm()
        errmsg = None
    context = {'form': form, 'errmsg': errmsg}
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
                errmsg = 'Invalid email or password'
        else:
            errmsg = form.errors
    else:
        form = LoginForm()
        errmsg = None
    
    return render(request, 'login.html', {'form': form, 'errmsg': errmsg})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    return render(request, 'home.html', {'username': username})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        form = OrderForm(request.data)
        if form.is_valid():
            order = create_order(form.cleaned_data['user'], request.data['items'])
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class CancellationViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer

    def create(self, request, *args, **kwargs):
        form = CancellationForm(request.data)
        if form.is_valid():
            cancel_order(form.cleaned_data['order'].id, form.cleaned_data['reason'])
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnViewSet(viewsets.ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

    def create(self, request, *args, **kwargs):
        form = ReturnForm(request.data)
        if form.is_valid():
            return_order(form.cleaned_data['order'].id, form.cleaned_data['reason'])
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer

    def create(self, request, *args, **kwargs):
        form = RefundForm(request.data)
        if form.is_valid():
            process_refund(form.cleaned_data['order'].id, form.cleaned_data['amount'])
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
