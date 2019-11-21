mar = '00'
mbr = '000'
memoria = ['000', '000', '000', '000']
write = False



def insere_mar():
    mar = input('Memory Address Register ')
    return mar

def insere_mbr():
    mbr = input('Memory Buffer Register ')
    return mbr
    
def decod(mar):
    if mar == '00':
        return 0
    elif mar == '01':
        return 1
    elif mar == '10':
        return 2
    elif mar == '11':
        return 3
    
def le_memoria(mbr, memoria):
    linha = decod(mar)
    mbr = memoria[linha]
    return mbr
    
def escreve_memoria(mbr, memoria):
    linha = decod(mar)
    memoria[linha] = mbr
    return memoria

def insere_write():
    write = input('Insira o bit de write ')
    if write == '1':
        write = True
    else:
        write = False
    return write

def processa_memoria(write):
    if write:
        escreve_memoria(mbr, memoria)
    else:        
        print('MBR: {}'.format(le_memoria(mbr, memoria)))
            
            
    
def menu():  
    global mar, mbr, write, memoria, multiplex
    
    opt = input('1- Definir MAR\n2- Definir MBR\n3- Definir bit Write\n')
    
    if opt == '1': mar = insere_mar()
    
    elif opt == '2': mbr = insere_mbr()
    
    elif opt == '3': 
        write = insere_write()
        processa_memoria(write)
        write = False
        

while True: 
    menu()
    print('\nEstado atual:\nMAR: {0}\nMBR: {1}\nMemória: {2:>4}\n{3:>13}\n{4:>13}\n{5:>13}'.format(mar, mbr, memoria[0], memoria[1], memoria[2], memoria[3]))
