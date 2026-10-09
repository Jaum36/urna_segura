import sqlite3

def votar(numero):
  data = (
    {"numero":numero}
  )
  trans = sqlite3.connect('tse.db')
  try:
    with trans:
      trans.execute('INSERT INTO vbto VALUES(:numero)', data)
  except sqlite3.IntegrityError:
    print("Não foi possível adicionar duas vezes no Python")

  trans.close()