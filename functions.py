#Função 'Ler'.
def ler() -> str:
    '''Esta função extrai todo o arquivo como uma string.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis_todos = arquivo.read()
        arquivo.close()
    return perfis_todos

#Função 'Criar'.
#matricula, nome, data de nascimento, faixa, ultima graduação, sexo, plano, status