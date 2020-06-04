from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm

from .utils import handle_uploaded_file_consult, handle_uploaded_file_exam

@login_required
def importConsultFile(request):

  context = {
    'erro' : ''
  }

  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      try:
        handle_uploaded_file_consult(request.FILES['file'])
        return HttpResponseRedirect('/')
      except Exception as e:
        context['erro'] = 'Erro ao processar arquivo, por favor, tente novamente! %s'%(e)
  else:
    form = UploadFileForm()

  context['form'] = form

  return render(request, 'consult/index.html', context)

@login_required
def importExamFile(request):

  context = {
    'erro' : ''
  }

  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      try:
        handle_uploaded_file_exam(request.FILES['file'])
        return HttpResponseRedirect('/')
      except Exception as e:
        context['erro'] = 'Erro ao processar arquivo, por favor, tente novamente! %s'%(e)
  else:
    form = UploadFileForm()

  context['form'] = form

  return render(request, 'exam/index.html', context)
