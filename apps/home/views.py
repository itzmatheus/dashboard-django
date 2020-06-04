from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse

from apps.files.models import Consulta

@login_required
def index(request):
  
  return render(request, 'home/index.html')

def getDataChart(request):

  '''
    Deve-se desenvolver um gráfico demonstrando a quantidade de consultas, quantidade de
    exames e gasto por consulta, sendo o eixo X a competência (mês e ano) usando​ ​ D3.js​ .
  '''

  SQL_QUERY = '''
    SELECT
      COUNT(con.*) as qtd_consultas,
      COUNT(ex.*) as qtd_exames,
      SUM(ex.valor_exame) as gasto_por_consulta,
      date_part('year', con.data_consulta)::text as ano_consulta,
      date_part('month', con.data_consulta)::text as mes_consulta
    FROM files_consulta con
    JOIN files_exame ex ON ex.numero_guia_consulta=con.numero_guia_consulta
    GROUP BY ano_consulta, mes_consulta
    ORDER BY ano_consulta, mes_consulta
  '''

  cursor = connection.cursor()
  cursor.execute(SQL_QUERY)
  data = dictfetchall(cursor)

  for index in range(len(data)):
    data[index]['data_consulta'] = data[index]['mes_consulta'] + ' / ' + data[index]['ano_consulta']


  context = {
    'rows': data
  }

  return JsonResponse(data, safe=False)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]