# API Voa Campeão

## Requisitos funcionais:
- Python 3.7
- Django 2.*
- NodeJs
- ReactJs
- MySQL Server 5.7
## Como rodar:
- Clone este projeto em sua máquina.
- Crie um BD local com o nome: voa_campeao. 
- No arquivo ```settings.py``` mude a senha e o usuário para suas configurações e salve as modificações.
- Entre no projeto do backend e rode as seguintes instruções via terminal:
```python
python manage.py makemigrations
python manage.py migrate
```
Esses comandos vão criar a estrutura do BD.
Agora é possível rodar o projeto, use:
```python
python manage.py runserver
```
(Obs.: se você estiver em ambiente Linux, rode os comandos substituindo python por python3)

## Funcionalidades da Release:

- CRUD de viagem
- CRUD de usuário
- CRUD de patrocínio 

## Rotas registradas:

- http://localhost:8000/ (raiz do projeto)
- http://localhost:8000/usuarios
- http://localhost:8000/viagens
- http://localhost:8000/viagensop 
- http://localhost:8000/patrocinios

## Developers:

- Camila Nunes 
- Elivelton Rodrigues
- Helton Vasconcelos
- Thiago Costa
