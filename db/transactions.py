import sqlite3

def votar(numero, cpf):
  data = (
    {"numero":numero, "cpf": cpf}
  )
  voto = sqlite3.connect('tse.db')
  try:
    with voto:
      update = voto.execute('UPDATE eleitor SET ja_votou = True WHERE cpf = (:cpf) AND ja_votou = False', data);
      rowCount = update.rowcount
      if rowCount != 1:
        return False
      voto.execute('INSERT INTO voto VALUES(:numero)', data);
    return True
  except sqlite3.IntegrityError:
    print("Voto não computado!")
  finally:
    voto.close()

def registrar_eleitor(nome, cpf):
  data = (
    {"nome": nome, "cpf": cpf, }
  )

  eleitor = sqlite3.connect('tse.db')
  try:
    with eleitor:
      eleitor.execute('INSERT INTO eleitor VALUES(:nome, :cpf, false)', data)
  except sqlite3.IntegrityError:
    print("Eleitor não registrado")