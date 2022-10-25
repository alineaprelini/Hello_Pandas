import pandas as pd 

#importando csv
cad = pd.read_csv('20220906_...183_...._NEW.csv', encoding = 'latin-1', delimiter = ';')

#Inclusão de colunas
cad['Provedor_Codigo'] = 793
cad['Estipulante_Codigo'] = 793
cad['Subestipulante_Codigo'] = 793


#Alterando tipo de dado 
#cad['DataNascimento'] = cad['DataNascimento'].astype(str) 
cad['Telefone2'] = cad['Telefone2'].fillna(0).astype(int) #float para int 
cad['Telefone'] = '/' + cad['Telefone'].astype(str) #Adicionando string '/' para concatenar na proxima etapa


#Concatenar Colunas 
cad['Telefone3'] = cad.Telefone2.astype(str) + cad.Telefone.astype(str)

#Alterar data 
from pandas.core import apply
def data(a):
  a = str(a)
  b = a[6:8] + '/' + a[4:6] + '/' + a[0:4]
  return b

cad['DataNascimento'] = cad['DataNascimento'].apply(data)



#Validando o cpf 
def ver_cpf(cpf):
    if cpf == '':
        return ''
    # Limpeza de pontos, ífen e barra
    cpf = str(cpf)
    cpf = cpf.strip()
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')
    cpf = cpf.replace('/','')
    dig = len(cpf) # Tamanho da string
    cpf_1 = cpf # String para cálculo
    # Colocar uma condicional
    cpf_2 = '{:0>11}'.format(cpf) # Tentativa zeros á esquerda
    cpf_3 = '{:0<11}'.format(cpf) # Tentativa zeros á direita

###############################################################################################################################
    def algoritmo(cpf_):
        soma_1 = 0
        soma_2 = 0
        rest_1 = 0
        rest_2 = 0

        # Primeiro dígito verificador
        for i in range(9):
            soma_1 += (int(cpf_[i]) * (10 - i))
            #print((cpf_[i]), ' X ', 10- i, ' = ' ,(int(cpf_[i]) * (10 - i)))
            #print('soma = ', soma_1)
        rest_1 = soma_1 % 11




        if ((rest_1 <= 1) and (int(cpf_[9]) == 0)) or ((11 - rest_1) == int(cpf_[9])):

            # Segundo dígito verificador

            for y in range(10):
                soma_2 += int(cpf_[y]) * (11 - y)
                #print((cpf_[y]), ' X ', 11 - y, ' = ' ,(int(cpf_[y]) * (10 - y)))
                #print('soma = ', soma_2)

            rest_2 = soma_2 % 11


            if ((rest_2 <= 1) and (int(cpf_[10]) == 0)) or ((11 - rest_2) == int(cpf_[10])):

                return True

            else:

                return False

        else:
            return False

###############################################################################################################################
    #teste cpf_1

    if not (dig < 11):
        if algoritmo(cpf_1) == True:

            return cpf_1

    # teste cpf_2
    if algoritmo(cpf_2) == True:

        return cpf_2

    # teste cpf_3
    elif algoritmo(cpf_3) == True:

        return cpf_3

    else:

        return(' ')

#conversão de dados (cpf)
cad['CPF'].fillna(value = 0, inplace = True)
cad['CPF'] = cad['CPF'].astype(int)

cad['CPF'] = cad['CPF'].apply(ver_cpf)

#Condicionais para Column EstadoCivil 
cad.loc[cad['EstadoCivil'] == 1 , 'EstadoCivil'] = 'Solteiro'
cad.loc[cad['EstadoCivil'] == 2 , 'EstadoCivil'] = 'Casado'
cad.loc[cad['EstadoCivil'] == 3 , 'EstadoCivil'] = 'Divorciado'
cad.loc[cad['EstadoCivil'] == 4 , 'EstadoCivil'] = 'Viuvo'
cad.loc[cad['EstadoCivil'] == 5 , 'EstadoCivil'] = 'Separado'
cad.loc[cad['EstadoCivil'] == 6 , 'EstadoCivil'] = 'União Estavel'





#exportando csv 
cad.head(2)
#Exportar o arquivo
cad.to_csv('...._CM.csv', index = False)
