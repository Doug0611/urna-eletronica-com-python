from time import sleep

def confirm():
    global alt;  
    alt = str(input('\n\033[1;32mDigite "A" pra alterar voto\nDigite "C" para confirma voto\033[m  |- ')).upper()
                
def barra():
    print()
    print('\033[1;37m=-=-=\033[m' * 9)
 
def vencedor(cand_a,cand_b ,cand_c):
    if cand_a == cand_b and cand_a == cand_b > cand_c:
        return '\n\033[1;32mEmpate entre Cand A e Cand B.\033[m'
    elif cand_a == cand_c and cand_a == cand_c > cand_b: 
        return '\n\033[1;32mEmpate entre Cand A e Cand C.\033[m'
    elif cand_b == cand_c and cand_b == cand_c > cand_a:
        return '\n\033[1;32mEmpate entre Cand B e Cand C.\033[m'
    elif cand_a > cand_b and cand_c:
        return '\n\033[1;32mCand A Vencedor!(a).\033[m'
    elif cand_b > cand_a and cand_c:
        return '\n\033[1;32mCand B Vencedor(a)!.\033[m'
    elif cand_c > cand_a and cand_b:
        return '\n\033[1;32mCand C Vencedor(a)!.\033[m'
    else:
        return '\n\033[1;32mEmpate entre os 3 Candidatos a prefeitura.\033[m'
                   
votos = {15: 0, #cand A
         25: 0, #cand B
         30: 0, #cand C
         0: 0}  # voto em branco

eleitores = 0; votos_Validos = 0; votos_Nulos = 0

while True:
    try:
        barra()
        voto = int(input('\033[1;32mCandidatos a eleição para prefeito:\n\n'+
                   '15 - Cand A\n25 - Cand B\n30- Cand C\n0 - Voto em branco\n20210102 - Encerrar  |- \033[m'))
                     
    except:
        print('\n\033[1;31mTente novamente... algo deu errado no processo!\033[m')
        sleep(1)
        continue  
    else:
        if voto == 20210102:
            print('\n\033[1;31mFinalizando votação...\033[m')          
            sleep(1)
            break   
              
        elif voto not in votos:
            print('\n\033[1;31mVocê está votando nulo...\033[m')    
            confirm()                  
            if alt == 'C':
                print('\n\033[1;36mConfirmando voto...\033[m')
                sleep(1)
                votos_Nulos += 1
                eleitores += 1
            else:
                print('\n\033[1;31mCorrigindo voto...\033[m')
                sleep(1)
                continue
           
        elif voto == 15:
            print('\n\033[1;94m[FOTO]\033[m\n\n\033[1;95mCAND A - N° 15\033[m')   
            confirm()
            if alt == 'C':
                print('\n\033[1;36mConfirmando voto...\033[m')
                sleep(1)       
                votos[15] += 1 
                votos_Validos += 1
                eleitores += 1
            else:
                print('\n\033[1;31mCorrigindo voto...\033[m')
                sleep(1)
                continue
                     
        elif voto == 25:
            print('\n\033[1;94m[FOTO]\033[m\n\n\033[1;95mCAND B - N° 25\033[m')   
            confirm()
            if alt == 'C':
                print('\n\033[1;36mConfirmando voto...\033[m')
                sleep(1)       
                votos[25] += 1 
                votos_Validos += 1
                eleitores += 1
            else:
                print('\n\033[1;31mCorrigindo voto...\033[m')
                sleep(1)
                continue         

        elif voto == 30:
            print('\n\033[1;94m[FOTO]\033[m\n\n\033[1;95mCAND C - N° 30\033[m')            
            confirm()
            if alt == 'C':
                print('\n\033[1;36mConfirmando voto...\033[m')
                sleep(1)       
                votos[30] += 1 
                votos_Validos += 1
                eleitores += 1
            else:
                print('\n\033[1;31mCorrigindo voto...\033[m')
                sleep(1)
                continue
        
        elif voto == 0:
            print('\n\033[1;95mVocê está votando em Branco...\033[m')
            confirm()
            if alt == 'C':
                print('\n\033[1;36mConfirmando voto...\033[m')
                sleep(1)       
                eleitores += 1
                votos[0] += 1
            else:
                print('\n\033[1;31mCorrigindo voto...\033[m')
                sleep(1)
                continue           
barra()
print(vencedor(votos[15],votos[25],votos[30]))
print('\nOVERVIEW DAS VOTAÇÕES') 
sleep(1)      
print(f'\n\033[1;32mVotos válidos: \033[m\033[31m{votos_Validos}')
print(f'\033[1;32mVotos branco: \033[m\033[31m{votos[0]}')
print(f'\033[1;32mVotos nulos: \033[m\033[31m{votos_Nulos}')
print(f'\n\033[1;32mVotos do Cand A: \033[m\033[31m{votos[15]}')
print(f'\033[1;32mVotos do Cand B: \033[m\033[31m{votos[25]}')
print(f'\033[1;32mVotos do Cand C: \033[m\033[31m{votos[30]}')
        
           
            
            
    
        