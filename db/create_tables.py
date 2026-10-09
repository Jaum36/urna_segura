from connect_db import cursor

cursor.execute('CREATE TABLE eleitor (nome TEXT, cpf TEXT, ja_votou BOOLEAN)')
cursor.execute('CREATE TABLE candidato (nome TEXT, numero INTEGER, partido TEXT)')
cursor.execute('CREATE TABLE vbto (numero_candidato INTEGER)')