from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, template_name='index.html', context=context)


def detail(request, question_id):
    return HttpResponse('Detail page - question_id : %s' % question_id)

def results(request, question_id):
    return HttpResponse('Result page - question_id : %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote page - question_id : %s' % question_id)