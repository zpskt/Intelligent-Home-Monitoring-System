from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader



# 定义一个名为 index 的视图函数，用于处理根路径的请求
def index(request):
   pass

# 定义一个名为 detail 的视图函数，用于处理特定问题详情页的请求
# 参数 request 是 Django 传入的 HTTP 请求对象，question_id 是问题的唯一标识符
def detail(request, question_id):
    pass

# 定义一个名为 results 的视图函数，用于处理特定问题结果页的请求
# 参数 request 是 Django 传入的 HTTP 请求对象，question_id 是问题的唯一标识符
def results(request, question_id):
    pass

# 定义一个名为 vote 的视图函数，用于处理特定问题投票页的请求
# 参数 request 是 Django 传入的 HTTP 请求对象，question_id 是问题的唯一标识符
def vote(request, question_id):
    pass
