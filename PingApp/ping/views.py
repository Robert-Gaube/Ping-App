from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound
import subprocess
import platform
from .models import Setup

def ping(ip):
    try:
        output = subprocess.check_output(
            'ping' + (' -n 1 -w 200 ' if platform.system() == 'Windows' else ' -c 1 ') + ip, shell=True
        )
        if b"Reply from " + bytes(ip, encoding='utf8') + b': bytes=32' in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def index(request):
    setups = Setup.objects.all()
    list = []
    for setup in setups:
        ip = getattr(setup, 'ip')
        name = getattr(setup, 'name')
        ping_status = ping(ip)
        list.append({'name' : name, 'ip' : ip, 'ping_status' : ping_status})

    print(list)
    return render(request, 'ping/main.html', {
        'list' : list
    })
    
def create(request):
    list = []

    with open('ping\\data\\data.txt', 'r') as file:
        for line in file.readlines():
            words = line.split(' ')
            words[1] = words[1].replace('\n', '')
            list.append(f'{words[0]} with ip: {words[1]} inserted succesfully')
            setup = Setup(name=words[0], ip=words[1])
            setup.save()
    return render(request, 'ping/create.html', {
        'list' : list
    })