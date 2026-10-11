## Disciplina: REDES II
## Data de entrega: 22/10/2026

## O que foi feito até agora no projeto:
- Interface do registro do Eleitor e da votação
- Funções de votar e registrar o eleitor
- hmac-SHA256 no CPFquando vai ao banco
- Verificação de duplicidade para evitar que um mesmo eleitor vote duas vezes

## Observações
- O banco é local, vc precisa rodar os arquivos `connect_db.py` e `create_tables.py` para que o banco seja criado e as tabelas sejam criadas respectivamente.
- Versão Python utilizada: Python 3.11.15
- Libs externas: PySimpleGUI (todas as outras bibliotecas são nativas do python)