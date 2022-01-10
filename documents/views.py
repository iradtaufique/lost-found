from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Idcollection
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from . models import*
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator
# from.forms import Comments


class Login(LoginView):
    template_name = 'documents/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    # messages.SUCCESS('Welcome')


class Logout(LogoutView):
    template_name = 'documents/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    # messages.SUCCESS('Welcome')


class Register(FormView):
    template_name = 'documents/registration.html'
    form_class = UserCreationForm
    redirect_authenitcated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)


class Home(ListView):
    model = Idcollection
    template_name = 'documents/indexhome.html'
    context_object_name = 'idcards'


def home2(request):
    idcards = Idcollection.objects.all().order_by('-created_on')[:4]
    idcard2 = Idcollection.objects.all().order_by('-created_on')
    paginatordata = Idcollection.objects.all()
    page = Paginator(paginatordata, 1)

    context = {
        'idcards': idcards,
        'idcard2': idcard2,
        'page': page,
    }
    return render(request, 'documents/indexhome.html', context)


class Detail_on_id(DetailView):
    model = Idcollection
    template_name = 'documents/docdetails.html'
    context_object_name = 'details_on_id'


class Additem(LoginRequiredMixin, CreateView):
    model = Idcollection
    fields = ['idnumber', 'district', 'sector',
              'isfound', 'documentType', 'location']
    # select what to show?
    template_name = 'documents/additem.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Additem, self).form_valid(form)


class Updateitem(LoginRequiredMixin, UpdateView):
    model = Idcollection
    fields = '__all__'
    template_name = 'documents/additem.html'
    success_url = reverse_lazy('home')


class Delete(LoginRequiredMixin, DeleteView):
    model = Idcollection
    fields = '__all__'
    template_name = 'documents/delete.html'
    success_url = reverse_lazy('home')


def search(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # print(f'Q value:{q}')
        data = Idcollection.objects.filter(
            Q(idnumber__icontains=q) | Q(first_name__icontains=q) | Q(second_name__icontains=q))
        # data = Idcollection.objects.filter(Multiple_q)
    else:
        data = Idcollection.objects.all()
    context = {
        'data': data
    }
    return render(request, 'documents/search.html', context)
