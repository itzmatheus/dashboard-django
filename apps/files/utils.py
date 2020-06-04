import uuid, csv, datetime
from .models import Consulta, Exame

def validateFormatHeader(header, original_header):
  if header != original_header:
    return False
  return True

def handle_uploaded_file_consult(f):

  header_consultas = ['numero_guia_consulta', 'cod_medico', 'nome_medico', 'data_consulta', 'valor_consulta']

  id = uuid.uuid4()
  pathFile = './tmp_files/%s.csv'%str(id)
  with open(pathFile, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)


  with open(pathFile, 'r') as csvfile:
    fileRead = list(csv.reader(csvfile, delimiter=';'))
    header_valido = validateFormatHeader(fileRead[0], header_consultas)
    if not header_valido:
      raise NameError('Preencha o header corretamente: ' + str(', '.join(header_consultas)))
    for row in fileRead[1:]:
      consulta = Consulta()
      consulta.numero_guia_consulta = row[0]
      consulta.cod_medico = row[1]
      consulta.nome_medico = row[2]
      consulta.data_consulta = row[3]
      consulta.valor_consulta = row[4]
      consulta.save()

def handle_uploaded_file_exam(f):

  header_exames = ['numero_guia_consulta', 'descricao', 'valor_exame']

  id = uuid.uuid4()
  pathFile = './tmp_files/%s.csv'%str(id)
  with open(pathFile, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)


  with open(pathFile, 'r') as csvfile:
    fileRead = list(csv.reader(csvfile, delimiter=';'))
    header_valido = validateFormatHeader(fileRead[0], header_exames)
    if not header_valido:
      raise NameError('Preencha o header corretamente: ' + str(', '.join(header_consultas)))
    for row in fileRead[1:]:
      exame = Exame()
      exame.numero_guia_consulta = row[0]
      exame.descricao = row[1]
      exame.valor_exame = row[2]
      exame.save()