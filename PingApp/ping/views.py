from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound
import subprocess
import platform
from .models import Setup

NO_ENTRIES_PER_COL = 22

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
    return render(request, 'ping/index.html')

def all(request):
    setups = Setup.objects.all()
    no_setups = setups.count()
    cols = []
    list = []

    counter = 0
    for setup in setups:
        if counter == NO_ENTRIES_PER_COL:
            counter = 0
            cols.append(list)
            list = []
        ip = getattr(setup, 'ip')
        name = getattr(setup, 'name')
        uefi = getattr(setup, 'uefi')
        if uefi:
            list.append({'name' : name, 'ip' : ip, 'ping_status' : 'Uefi'})
        else:    
            ping_status = ping(ip)
            list.append({'name' : name, 'ip' : ip, 'ping_status' : ping_status})
        counter = counter + 1
        
    cols.append(list)
    return render(request, 'ping/main.html', {
        'cols' : cols
    })
    
def online(request):
    setups = Setup.objects.all()
    no_setups = setups.count()
    cols = []
    list = []

    counter = 0
    for setup in setups:
        if counter == NO_ENTRIES_PER_COL:
            counter = 0
            cols.append(list)
            list = []
        ip = getattr(setup, 'ip')
        name = getattr(setup, 'name')
        uefi = getattr(setup, 'uefi')
        if uefi:
            continue
        else:    
            ping_status = ping(ip)
            if ping_status:
                list.append({'name' : name, 'ip' : ip, 'ping_status' : ping_status})
                counter = counter + 1
        
    cols.append(list)
    return render(request, 'ping/main.html', {
        'cols' : cols
    })
    
def offline(request):
    setups = Setup.objects.all()
    no_setups = setups.count()
    cols = []
    list = []

    counter = 0
    for setup in setups:
        if counter == NO_ENTRIES_PER_COL:
            counter = 0
            cols.append(list)
            list = []
        ip = getattr(setup, 'ip')
        name = getattr(setup, 'name')
        uefi = getattr(setup, 'uefi')
        if uefi:
            continue
        else:    
            ping_status = ping(ip)
            if not ping_status:
                list.append({'name' : name, 'ip' : ip, 'ping_status' : ping_status})
                counter = counter + 1
        
    cols.append(list)
    return render(request, 'ping/main.html', {
        'cols' : cols
    })

def uefi(request):
    setups = Setup.objects.all()
    no_setups = setups.count()
    cols = []
    list = []

    counter = 0
    for setup in setups:
        if counter == NO_ENTRIES_PER_COL:
            counter = 0
            cols.append(list)
            list = []
        ip = getattr(setup, 'ip')
        name = getattr(setup, 'name')
        uefi = getattr(setup, 'uefi')
        if uefi:
            list.append({'name' : name, 'ip' : ip, 'ping_status' : 'Uefi'})
            counter = counter + 1
        
    cols.append(list)
    return render(request, 'ping/main.html', {
        'cols' : cols
    })

def create(request):
    list = []

    with open('ping\\data\\data.txt', 'r') as file:
        for line in file.readlines():
            words = line.split(' ')
            words[1] = words[1].replace('\n', '')
            setup = Setup(name=words[0], ip=words[1])
            try:
                setup.save()
                list.append(f'{words[0]} with ip: {words[1]} inserted succesfully')
            except:
                list.append(f'{words[0]} with ip: {words[1]} was not inserted because it already exists')
                
                
    return render(request, 'ping/create.html', {
        'list' : list
    })