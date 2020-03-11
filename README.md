# Gerador de Arvore Binaria e AVL

Este algoritmo faz parte de uma série de trabalhos realizados na cadeira de estruturas de dados II do curso de Ciência da Computação, ministrado na Universidade Federal do Pampa (UNIPAMPA).

<p align="center">
  <img width="300" height="200" src="https://user-images.githubusercontent.com/57903394/76466646-d2d3ed00-63c6-11ea-96b2-10c4b1fb7c2e.png">
</p>

## Objetivo do código

O algoritmo carrega dados que compunham perfis de estudantes, esses dados estão contidos em documentos .txt e localizados em um diretório informado pelo usuário. Tais dados atendem as seguintes variaveis em uma estrutura: Matricula, Nome, Curso, E-mail e Telefone.
O código organiza esses perfis em uma arvore, seja binária ou AVL, onde a chave de cada folha é igual a matricula armazenada na estrutura de dados. Ou seja, cada estudante representa uma folha, e a identificação de cada folha é igual a matricula do respectivo estudante.

Além de permitir a visualização da arvore criada, o código também aceita dois tipos de busca:

<ul style="list-style-type:disc;">
  <li>Uma busca onde os ID a serem pesquisados estão contidos em um arquivo .txt</li>
  <li>Uma busca "pseudo aleatória", onde o usuário entra com x quantidade de buscas que deseja fazer e o código procura IDs aleatórios x vezes.</li>
</ul>


## Entradas

O usuário deve fornecer, no momento de rodar o código, o nome do diretório que se encontra os dados a serem inseridos na arvore, para isso usa-se da seguinte sintaxe:

`python Binario.py Diretorio` ou `python AVL.py Diretorio`

O arquivo *buscas.txt* contém os IDs a serem pesquisados de acordo com o primeiro tipo de busca. É possivel edita-lo adicionando os IDs desejados, desde que cada ID esteja em uma linha distinta.

## Saídas

Todas as saídas são impressas no terminal onde o código esta sendo exacutado. Independe do tipo de busca realizado, o código deve retornar o perfil do estudante que deu match com o ID pesquisado.

<p align="center">
    <img width="300" height="400" src="https://user-images.githubusercontent.com/57903394/76466839-28a89500-63c7-11ea-8843-31a797eda6c8.png">
</p>

# Considerações

Apesar de cumprir com suas funções, tem-se como objetivo criar uma interface gráfica para que as operações - como a busca e inserção na arvore - possam ser melhor visualizadas. 

# Observações

Para gerar os dados a serem utilizados por este algoritmo, é possivel utilizar o seguinte [Gerador de dados aleatórios](https://github.com/Laltany/Gerador_dados)
