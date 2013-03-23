from django.http import HttpResponse
##from django.template import Context, RequestContext
from django.template.loader import get_template
##from django.contrib.auth.models import User
##from django.contrib.auth import authenticate, login, logout
##from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect


##def view_todos (request):
##    return HttpResponse("hello ticked2")
##    
def view_todos(request):
    template = "base.html"
    return render_to_response(template)

def tickedTodosView(request, page_number=1):
    return HttpResponse("tickedTodosView")
def addTodoView(request):
    return HttpResponse("tickedTodosView")
def tickTodoView(request, todoId):
    return HttpResponse("tickedTodosView")
def unTickTodoView(request, todoId):
    return HttpResponse("tickedTodosView")
def deleteTodoView(request, todoId):
    return HttpResponse("tickedTodosView")
def loginView(request):
    return HttpResponse("tickedTodosView")
def logoutView(request):
    return HttpResponse("tickedTodosView")
def newUserView(request):
    return HttpResponse("tickedTodosView")
def createUserView(request):
    return HttpResponse("tickedTodosView")
