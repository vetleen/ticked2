from django.http import HttpResponse
##from django.template import Context, RequestContext
##from django.template.loader import get_template
##from django.contrib.auth.models import User
##from django.contrib.auth import authenticate, login, logout
##from django.core.context_processors import csrf
##from django.shortcuts import render_to_response, redirect


def view_todos (request):
	return HttpResponse("hello ticked2")
	
