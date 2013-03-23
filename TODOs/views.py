from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from TODOs.models import Todo

def view_todos (request, page_number=1):
    if not request.user.is_authenticated():
        return redirect(newUserView)
    #make sure data passed is proper Type
    page_number = int(page_number)
    
    #finds all un-ticked todos:
    allTODOs = request.user.todo_set.all()
    unTickedTodos=[]
    for TODO in (allTODOs):
        if TODO.todoIsTicked == False:
            unTickedTodos.append(TODO)

    #finds start-point and stop_point for next bit of code:
    number_of_todos = int(len(unTickedTodos))
    todos_per_page = 9 #this can be set freely
    stop_point = int(page_number)*int(todos_per_page)
    start_point = int(stop_point)-(int(todos_per_page)-int(1))
    if number_of_todos < stop_point:
            stop_point = number_of_todos
    if stop_point == 0:
        stop_point = 1
    count=0
    
    #adds exactly 9 todos numbered from start_point to stop_point to todos_to_send
    todos_to_send = []
    for TODO in unTickedTodos:
            count=count+1
            if count >= start_point and count <= stop_point:
                    todos_to_send.append(TODO)
                    
    #What links to other todo/x/ will be provided?:
    number_of_pages_possible = int(((number_of_todos-1)/todos_per_page)+1)
    if number_of_pages_possible <= 0:
        number_of_pages_possible = 1
    previous_page = None
    next_page = None
    if page_number > 1:
            previous_page = (page_number - 1)
    if page_number < number_of_pages_possible:
            next_page = (page_number + 1)

    #respond to request:
    c = {'TODOs': todos_to_send, 'currentpage': page_number, 'lastpage': number_of_pages_possible, 'nextpage': next_page, 'previouspage': previous_page}
    c.update(csrf(request))
    template = "todos.html"
    return render_to_response(template, c, context_instance=RequestContext(request))

def tickedTodosView(request, page_number=1):
    if not request.user.is_authenticated():
        return redirect(newUserView)
    #make sure data passed is proper Type
    page_number = int(page_number)
    
    #finds all un-ticked todos:
    allTODOs = request.user.todo_set.all()
    unTickedTodos=[]
    for TODO in (allTODOs):
        if TODO.todoIsTicked == True:
            unTickedTodos.append(TODO)

    #finds start-point and stop_point for next bit of code:
    number_of_todos = int(len(unTickedTodos))
    todos_per_page = 9 #this can be set freely
    stop_point = int(page_number)*int(todos_per_page)
    start_point = int(stop_point)-(int(todos_per_page)-int(1))
    if number_of_todos < stop_point:
            stop_point = number_of_todos
    if stop_point == 0:
        stop_point = 1
    count=0
    
    #adds exactly 9 todos numbered from start_point to stop_point to todos_to_send
    todos_to_send = []
    for TODO in unTickedTodos:
            count=count+1
            if count >= start_point and count <= stop_point:
                    todos_to_send.append(TODO)
                    
    #What links to other todo/x/ will be provided?:
    number_of_pages_possible = int(((number_of_todos-1)/todos_per_page)+1)
    if number_of_pages_possible <= 0:
        number_of_pages_possible = 1
    previous_page = None
    next_page = None
    if page_number > 1:
            previous_page = (page_number - 1)
    if page_number < number_of_pages_possible:
            next_page = (page_number + 1)

    #respond to request:
    c = {'TODOs': todos_to_send, 'currentpage': page_number, 'lastpage': number_of_pages_possible, 'nextpage': next_page, 'previouspage': previous_page}
    c.update(csrf(request))
    template = "todos.html"
    return render_to_response(template, c, context_instance=RequestContext(request))

def addTodoView(request):
    if not request.user.is_authenticated():
        output = "You need to be logged in to do that"
        return HttpResponse(output)
    if request.method == 'POST':
        if request.POST['headline'] or request.POST['bodytext']:
            headline = request.POST['headline']
            bodytext = request.POST['bodytext']
            newTodo = Todo(headLine=headline, bodyText=bodytext, owner=request.user)
            newTodo.save()
        else:
            output = "This should not happen: request method is POST, but neither headline or bodytext is found.."
            return HttpResponse(output) 
        return redirect(view_todos)
    else:
        c = {}
        c.update(csrf(request))        
        template="addtodo.html"
        return render_to_response(template, c)
    
def editTodoView(request, todoId):
    if not request.user.is_authenticated():
        output = "You need to be logged in to do that"
        return HttpResponse(output)
    todoToEdit = Todo.objects.get(id=todoId)
    if request.method == 'POST':
        if todoToEdit.owner == request.user:
            if request.POST['headline'] or request.POST['bodytext']:
                if request.POST['headline']:
                    headline = request.POST['headline']
                    todoToEdit.headLine = headline
                if request.POST['bodytext']:
                    bodytext = request.POST['bodytext']
                    todoToEdit.bodyText = bodytext
                todoToEdit.save()
            else:
                output = "This should not happen: you seem to have come here from the edit-form, but neither headline or bodytext is found.."
                return HttpResponse(output) 
            return redirect(view_todos)
    else:
        TODOs = request.user.todo_set.all()    
        c = {'TODO': todoToEdit}
        c.update(csrf(request))        
        template="edittodo.html"
        return render_to_response(template, c)
    
def tickTodoView(request, todoId):
    #can add errormessage if Todo dosen't exist...
    if not request.user.is_authenticated():
        output = "You must be logged in to do that..."
        return HttpResponse(output)

    todoToTick = Todo.objects.get(id=todoId)
    if todoToTick.owner == request.user:
        todoToTick.todoIsTicked = True
        todoToTick.save()
        return redirect(view_todos)
    else:
        output = "Sneaky, Sneaky, not allowed.."
        return HttpResponse(output)
    
def unTickTodoView(request, todoId):
    #can add errormessage if Todo dosen't exist...
    if not request.user.is_authenticated():
        output = "You must be logged in to do that..."
        return HttpResponse(output)
    todoToUnTick = Todo.objects.get(id=todoId)
    if todoToUnTick.owner == request.user:
        todoToUnTick.todoIsTicked = False
        todoToUnTick.save()
        return redirect(tickedTodosView)
    else:
        output = "It seems that caused the server to try to tick someone elses TODO.."
        return HttpResponse(output)
def deleteTodoView(request, todoId):
    #can add errormessage if Todo dosen't exist...
    if not request.user.is_authenticated():
        output = "You must be logged in to delete a TODO"
        return HttpResponse(output)
    todoToDelete = Todo.objects.get(id=todoId)
    if todoToDelete.owner == request.user:
        todoToDelete.delete()
        return redirect(view_todos)
    else:
        output = "It seems that caused the server to try to delete someone elses TODO.."
        return HttpResponse(output) 

## Users, logins etc. 
def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(view_todos)
        else:
            output = "a 'disabled account' error message"
            return HttpResponse(output)
    else:
        output = "user/password invalid"
        return HttpResponse(output)

def logoutView(request):
    logout(request)
    return redirect(view_todos)

def newUserView(request):
    c = {}
    c.update(csrf(request))
    template = "newuser.html"
    return render_to_response(template, c)

def createUserView(request):
    #Still need to validate that username is unique and fail properly if it isn't....
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(view_todos)
        else:
            output = "a 'disabled account' error message: this should not happen when creating a new user and logging him in..."
            return HttpResponse(output)
    else:
        output = "user/password invalid: this should not happen when creating a new user and logging him in..."
        return HttpResponse(output)    
    return redirect(view_todos)
