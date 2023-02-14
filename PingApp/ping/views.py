from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound
import subprocess
import platform
from . import models

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
    try:
        
        return render(request, 'ping/main.html', {
            'text' : 'text1'
        })
    except:
        return HttpResponseNotFound('<h1>Error finding page </h1>')
    