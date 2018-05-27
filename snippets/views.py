# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
@csrf_exempt
def snippet_list(request):
	"""
	This is for listing all the snippets or 
	for creating new snippet
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=404)

def snippet_detail(request, pk):
	"""This method is for retrieving, Updating 
	   and for deleting the snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		print 'in except clause'
		return HttpResponse(status = 404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JsonResponse(serializer.data, status=201)
	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		return JsonResponse(serializer.errors, status=404)
	if request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)

