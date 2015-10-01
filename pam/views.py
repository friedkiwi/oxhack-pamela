from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Device
from oxpam import settings
import datetime
import time
from .forms import RegisterMacForm



# Create your views here.

def index(request):
    return render(request, 'pam/index.html', {})

def config(request):
    return render(request, 'pam/config.js', {})

def devices(request):

    returned_list = []

    devices_available = Device.objects.filter(show_in_overview=True, currently_in_space=True)

    for device in devices_available:
        if device.description != "":
            returned_list.append(device.description)
        else:
            t = iter(device.mac_address)
            returned_list.append('-'.join(a+b for a,b in zip(t, t)))

    return HttpResponse(json.dumps(returned_list))

@csrf_exempt
def update_devices(request):
    auth_key = request.POST["auth"]
    devices_list = request.POST["data"]



    devices_list = devices_list.replace(":", "")
    devices_array = devices_list.split(",")

    if (auth_key != settings.AUTH_STRING):
        return HttpResponseForbidden()

    devices_registered = Device.objects.all()

    for device in devices_registered:
        device.currently_in_space = False
        device.save()

    for device_submitted in devices_array:
        found = False
        device_found = Device
        for device_stored in devices_registered:
            if device_stored.mac_address == device_submitted:
                found = True
                device_found = device_stored
                break

        if not found:
            d_to_reg = Device(last_seen=datetime.datetime.fromtimestamp(time.time()).isoformat(), currently_in_space=True, mac_address=device_submitted)
            d_to_reg.save()
        else:
            device_found.currently_in_space = True
            device_found.save()


    return HttpResponse("ok")

def add_name(request):
    if (request.method == 'POST'):
        form = RegisterMacForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            device = Device.objects.filter(mac_address=cd["mac_address"]).first()


            if device:
                if cd["hide_on_animation"]:
                    device.show_in_overview = False
                device.description = cd["display_name"]

                device.save()
                return HttpResponseRedirect('/')
            else:
                return render(request, 'pam/add_name.html', {'form': form, 'exists': False })

    else:
        form = RegisterMacForm()

    return render(request, 'pam/add_name.html', {'form': form, 'exists': True })
