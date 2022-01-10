from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from django import forms

from orders.forms import Contact_usForm
from.models import Order

# Create your views here.


class CreateOrder(CreateView):

    model = Order
    fields = '__all__'
    template_name = "orders/orders.html"
    success_message = ("was created successfully")
    success_url = reverse_lazy("home")


def contactus(request):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))
    if request.method == "POST":
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Contact_usForm()
    context = {
        "form": form
    }
    return render(request, "orders/contact_us.html", context)
