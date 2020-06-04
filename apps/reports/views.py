import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.files.models import Consulta

@login_required
def index(request):

  nameDoctor = request.GET.get('nome_medico')
  date = request.GET.get('periodo')

  consultas_queryset = Consulta.objects.extra(select={
    'gasto_por_consulta': 'SELECT SUM(e.valor_exame) FROM files_exame e WHERE e.numero_guia_consulta=files_consulta.numero_guia_consulta',
    'quantidade_exames': 'SELECT COUNT(e.*) FROM files_exame e WHERE e.numero_guia_consulta=files_consulta.numero_guia_consulta'}
  ).order_by('-gasto_por_consulta')

  if nameDoctor:
    consultas_queryset = consultas_queryset.filter(nome_medico=nameDoctor)

  if date:
    dateFormatted = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    consultas_queryset = consultas_queryset.filter(data_consulta=dateFormatted)

  page = request.GET.get('page', 1)

  paginator = Paginator(consultas_queryset, 10)
  try:
    consultas = paginator.page(page)
  except PageNotAnInteger:
    consultas = paginator.page(1)
  except EmptyPage:
    consultas = paginator.page(paginator.num_pages)

  context = {
    'consultas': consultas
  }

  return render(request, 'reports/index.html', context)