# Exploring Mars

API Rest feito em Django Rest Framework para controlar e movimentar sondas em um plano cartesiano através de instruções.

## Começando

Para execução do projeto será necessário a instalação do [PYTHON](https://www.python.org/)

## Desenvolvimento

Para iniciar o projeto ou o desenvolvimento de melhorias basta clonar o projeto do GitHub num diretório de sua preferência:

```python
  cd "diretorio de sua preferencia"
  git clone https://github.com/batestin1/django_mars.git
```

## Inicialização

Após o python instalado e o projeto clonado, será necessário criar uma virtual env(`venv`) para instalar as depedências sem conflito com seu sistema operacional.

- `python3 -m venv venv`

Ative sua venv: `source venv/bin/activate`

Agora instalaremos todas as dependências para que nosso projeto consiga rodar.
Instale o `requirements.txt` que encontra-se na raiz do projeto

- `pip install -r requirements.txt`

Crie o banco de dados e as tabelas:

- `python manage.py makemigrations`
- `python manage.py migrate`

Inicie o server

- `python manage.py runserver`

acesse http://127.0.0.1:8000/ e seu projeto deve iniciar com esse cara:

![Django Rest](https://github.com/pedroimpulcetto/exploring_mars/blob/master/python/images/exploringmars.png)

## Features

A principal função desse projeto é a movimentação da sonda no plano cartesiano através de instrução que serão recebidas.

Para inciar, acesse a rota `/cartesian_plan/` e "crie" um plano cartesiano adicionando o Eixo X e Eixo Y, coordenada do ponto superior-direito do plano cartesiano.

Na rota `/probes/` criaremos uma Sonda Lunar com os atributos:

- Eixo X inicial
- Eixo Y inicial
- Direção inicial
- Id do plano cartesiado que deseja usar
  OBS: 'local' é o local final que a sonda chegará após as instruções que serão passadas posteriormente

Um plano cartesiano pode ter N sondas, mas uma sonda só pode estar em um plano cartesiano.

Na rota `/instructions/` coloque a instrução que queira que sonda siga, podendo ser "Move", "Right" ou "Left" e o Id da sonda para qual deve ser essa instrução.
Você pode adicionar quantas instruções forem necessárias.

```python
  cartesian_plan = {
    "id_cartesian_plan": int,
    "axis_x": int,
    "axis_y": int
  }
```

```python
  probes = {
    "id_probe": int,
    "init_x": int,
    "init_y": int,
    "direction": str,
    "instructions": list(),
    "id_cartesian_plan": int
  }
```

```python
  instructions = {
    "id_instruction": int,
    "instruction": str,
    "id_probe": int
  }
```

### Atenção

Se a sondar encontra-se em uma das extremidades do Eixo X ou Eixo Y e você passar uma instrução de "Move" - significando que ela deve seguir em frente - ela irá ignorar essa instrução pois está no fim do plano cartesiano, não podendo ultrapassar esse ponto.
Nesse caso, você deverá passar a instrução de "Right" ou "Left" para alterar a direção e depois passar "Move".
