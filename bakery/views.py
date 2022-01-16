from django.shortcuts import render
# Create your views here.
from bakery.models import Destination, SpecialOffers


def home(request):

    offers = SpecialOffers.objects.all()

    return render(request, "bakery/index.html", {'offers': offers})
