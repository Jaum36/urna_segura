import PySimpleGUI as sg
import db.transactions 
import hashlib, hmac

numeroVotado = 0
cpf = ''
hCPF = ''
nome = ''
estadoInterface = 'login'

with open('C:/Users/joaov/Downloads/secret_key.txt', encoding = 'utf-8') as file:
  key = bytes(file.read(), 'utf-8')

def calculoCPF(cpf):
  return True

layoutVoto = [[sg.Text('Coloque o número do seu candidato')],
          [sg.Input(key='-VOTACAO-',justification='center', enable_events=True)],
          [sg.Text(key=('-OUTPUT-'))], 
          [sg.Button('Confirmar', size=(10), key=('-CONFIRMAR-'), enable_events=True)]]

layoutLogin = [[sg.Text('Coloque seu nome:')],
          [sg.Input(key='-NOME-',justification='center', enable_events=True)],
          [sg.Text('Coloque o seu CPF:')],
          [sg.Input(key=('-CPF-'),justification='center', enable_events=True)],
          [sg.Button('Confirmar', size=(10), key=('-CONFIRMAR-'), enable_events=True)]]

window = sg.Window("URNA ELETRONICA", layoutVoto, disable_minimize = True)
login = sg.Window("IDENTIFICAÇÃO DO ELEITOR", layoutLogin)

while estadoInterface == 'login':
  event, values = login.read()

  if event == sg.WINDOW_CLOSED:
    break

  if event == '-CPF-' and len(values['-CPF-']) > 11:
    login['-CPF-'].update(values['-CPF-'][:-1])

  if event == '-CONFIRMAR-' and values['-CPF-'] != '' and values['-NOME-'] != '':
    cpf = values['-CPF-'].encode()
    nome = values['-NOME-']
    login.close()
    estadoInterface = 'voto'

    hCPF = hmac.new(key, cpf, hashlib.sha256)
    db.transactions.registrar_eleitor(nome, hCPF.hexdigest())

while estadoInterface == 'voto':
  event, values = window.read()

  if event == sg.WINDOW_CLOSED:
    break

  if event  == '-VOTACAO-' and values['-VOTACAO-'] and values['-VOTACAO-'][-1] not in ('0123456789'):
    window['-VOTACAO-'].update(values['-VOTACAO-'][:-1])
    window['-OUTPUT-'].update('Apenas números são permitidos.')

  elif event == '-VOTACAO-' and len(values['-VOTACAO-']) > 2:
     window['-VOTACAO-'].update(values['-VOTACAO-'][:-1])

  elif event == '-CONFIRMAR-' and (values['-VOTACAO-'] != ''):
      window['-CONFIRMAR-'].update(disabled=True)
      window['-VOTACAO-'].update(disabled=True)
      numeroVotado = values['-VOTACAO-']
      db.transactions.votar(numeroVotado, hCPF.hexdigest())
      window['-OUTPUT-'].update('VOCÊ VOTOU NO CANDIDATO COM NÚMERO: ' + values['-VOTACAO-'])

window.close()