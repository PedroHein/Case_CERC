# coding: utf-8 
# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(0, 20):  # Começando em 0 (cabeçalho)
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(0, 20):
    print(data_list[i][-2]) # sample[-2]

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Extrai uma coluna específica de uma lista de listas.
    Argumentos:
        data: Lista de listas.
        index: Índice da coluna a ser extraída.
    Retorna:
        Uma lista contendo os valores da coluna especificada.
    """
    column_list = [] # Cria/Inicializa a lista vazia
    for row in data:
        column_list.append(row[index])  # Adiciona o valor da coluna à lista
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1048575, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for row in data_list:  # Agora percorre todas as linhas
    if row[-2] == "Male": # Se for "Male", incrementa male
        male += 1
    elif row[-2] == "Female": # Se for "Female", incrementa female
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 665437 and female == 198247, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Conta a quantidade de ocorrências de cada gênero na lista de dados.
    Argumentos:
        data_list: Lista de listas contendo os dados.
    Retorna:
        Lista contendo a contagem de gêneros [Masculino, Feminino].
    """
    male = 0
    female = 0
    for row in data_list:  # Agora percorre todas as linhas
        if row[-2] == "Male": # Se for "Male", incrementa male
            male += 1
        elif row[-2] == "Female": # Se for "Female", incrementa female
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 665437 and count_gender(data_list)[1] == 198247, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Determina o gênero mais frequente na lista de dados.
    Argumentos:
        data_list: Lista de listas contendo os dados.
    Retorna:
        Uma string indicando o gênero mais comum ("Male", "Female" ou "Equal").
    """
    answer = ""
    male, female = count_gender(data_list)
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
# Listando todos os valores da coluna -3 (terceira coluna a partir do final)
# Usando um set para armazenar valores distintos da coluna -3 (User_Type)
print("\nTAREFA 7: Crie um gráfico similar para user_types")

def count_user_type(data_list):
    """
    Conta a quantidade de ocorrências de cada tipo de usuário dinamicamente.
    Argumentos:
        data_list: Lista de listas contendo os dados. 
    Retorna:
        Uma tupla contendo: (lista de tipos de usuários, lista de contagens correspondentes)
    """
    user_types = sorted(set(row[-3] for row in data_list))  # set para valores únicos e sorted para ordenar
    user_count = {user_type: 0 for user_type in user_types} # conta as ocorrências de cada tipo
    for row in data_list:
        user_count[row[-3]] += 1
    return user_types, [user_count[ut] for ut in user_types]

types, quantity = count_user_type(data_list) # obtendo os valores

# Gráfico
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Type')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque na coluna 'Gender' há valores nulos que são contabilizados quando verificamos quantas linhas tem no dataset (len(data_list))"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
# trip_duration_list = column_to_list(data_list, 2)
# min_trip = 0.
# max_trip = 0.
# mean_trip = 0.
# median_trip = 0.

trip_duration_list = [float(x) for x in column_to_list(data_list, 2)]  # Convertendo os valores para float

# Mínimo
min_trip = sorted(trip_duration_list)[0]  # Ordena e pega o primeiro (mínimo)

# Máximo
max_trip = sorted(trip_duration_list)[-1]  # Ordena e pega o último (máximo)

# Média
mean_trip = sum(trip_duration_list) / len(trip_duration_list)  # Soma todos os valores e divide pelo tamanho da lista

# Mediana
trip_duration_list.sort()  # Ordena a lista
n = len(trip_duration_list) # Tamanho da lista
if n % 2 == 1:  # Se o tamanho for ímpar
    median_trip = trip_duration_list[n // 2]  # Pega o elemento central
else:  # Se for par
    median_trip = (trip_duration_list[n // 2 - 1] + trip_duration_list[n // 2]) / 2  # Média dos dois centrais

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 885, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 624, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(row[-5] for row in data_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 578, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = input("Resposta: ").strip().lower()

if answer == "no":
    print("Desisti!")
elif answer == "yes":
    def count_items(column_list):
        types = list(set(column_list))
        counts = [column_list.count(item) for item in types]
        return types, counts
    try:
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
        column_list = column_to_list(data_list, -2)
        types, counts = count_items(column_list)
        print("\nTAREFA 12: Imprimindo resultados para count_items()")
        print("Tipos:", types, "Counts:", counts)
        assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
        assert sum(counts) == 1048575, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
        print("Você passou no desafio!!")
    except NameError:
        print("Erro: A variável 'data_list' não foi definida.")
