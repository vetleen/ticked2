from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect

from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from TODOs.models import Todo

##def view_todos(request):
##    template = "base.html"
##    return render_to_response(template)
def view_todos (request, page_number=1):
    if not request.user.is_authenticated():
        return redirect(newUserView)
    page_number = int(page_number)
    #Creates a list of all un-ticked todos:
    allTODOs = request.user.todo_set.all()
    unTickedTodos=[]
    for TODO in reversed(allTODOs):
        if TODO.todoIsTicked == False:
            unTickedTodos.append(TODO)
    #Creates a list of the TODOs that will be shown:
    number_of_todos = int(len(unTickedTodos))
    todos_per_page = 9 #this can be set freely
    stop_point = int(page_number)*int(todos_per_page)
    start_point = int(stop_point)-(int(todos_per_page)-int(1))
    if number_of_todos < stop_point:
            stop_point = number_of_todos
    if stop_point == 0:
        stop_point = 1
    count=0
    todos_to_send = []
    page_number=int(page_number)
    for TODO in unTickedTodos:
            count=count+1
            if count >= start_point and count <= stop_point:
                    todos_to_send.append(TODO)
    #What links to other todo/x/ will be provided?:
    if number_of_todos != 0: #to avoid dividing by 0 when there are 0 todos in unticked_todos!
        number_of_pages_possible = int((number_of_todos/todos_per_page)+1)
    if number_of_todos == 0: #this fakes the preceding if, by adding 1 to the pages possible var even if it is 0
        number_of_pages_possible = 1
    previous_page = None
    next_page = None
    if page_number > 1:
            previous_page = (page_number - 1)
    if page_number < number_of_pages_possible:
            next_page = (page_number + 1)
    #The response:
    c = {'TODOs': todos_to_send, 'currentpage': page_number, 'lastpage': number_of_pages_possible, 'nextpage': next_page, 'previouspage': previous_page}

    c.update(csrf(request))
    template = "todos.html"
    return render_to_response(template, c, context_instance=RequestContext(request))



def tickedTodosView(request, page_number=1):
    return HttpResponse("tickedTodosView")
def addTodoView(request):
    return HttpResponse("tickedTodosView")
def editTodoView(request, todoId):
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
