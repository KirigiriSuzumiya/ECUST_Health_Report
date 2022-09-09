from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def info_upload(request):
    id_list = set()
    username = request.POST['username']
    password = request.POST["password"]
    fp = open('/home/health/info.txt', 'a+')
    fp.write(username+' '+password+'\n')
    fp.close()
    return HttpResponse('录入成功！<a href="/index">返回</a><br>'
                        '觉得好用的话，帮我<a href="https://github.com/KirigiriSuzumiya/ECUST_Health_Report">点个star</a>哦~')


def log(request):
    fp = open('/home/health/log.txt', 'r')
    info = fp.read().replace('\n', '<br>')
    fp.close()
    return HttpResponse(info)


def id_list(request):
    info = "已录入人员：<br>"
    fp = open('/home/health/info.txt', 'r')
    for i in fp.readlines():
        username = i.split(' ')[0]
        password = i.split(' ')[1]
        password = password.replace('\n', '')
        info = info + username + '<br>'
    return HttpResponse(info)
