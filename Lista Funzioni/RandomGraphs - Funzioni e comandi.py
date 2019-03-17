import random
import math



#Funzione che simula il lancio di una moneta con probabilità che esca Testa (Head) = p
def flip(p):
    return 'H' if random.random() < p else 'T'

n = [50,100,500,1000]
psqrt= [1/math.sqrt(i) for i in n]
plog =[math.log(i)/i for i in n]
pinv = [1.0/i for i in n]
pun = [0.5 for i in n]
V = [i for i in range(0,len(n))]
E_sqrt = [[] for i in range(0,len(n))]
E_log = [[] for i in range(0,len(n))]
E_inv = [[] for i in range(0,len(n))]
E_un = [[] for i in range(0,len(n))]
E_inv_bf = []
pinv_bf =[]




#Grafi con p = 1/sqrt(n) (per diversi valori di n)
z = 0
index_E_sqrt=[]

for k in n:
    
    index_E_sqrt.append([k,psqrt[z]])
    for i in range(0,k):
        #print i
        for j in range(i+1,k):
            if i!=j:
                HT = flip(psqrt[z])
                if HT == 'H':
                    if not([j,i] in E_sqrt[z]) and i<j:
                        E_sqrt[z].append([i,j])
    
    z+=1
             

#Grafi con p = log(n)/n (per diversi valori di n)
z = 0
index_E_log=[]
for k in n:
    index_E_log.append([k,plog[z]])
    for i in range(0,k):
        #print i
        for j in range(0,k):
            if i!=j:
                HT = flip(plog[z])
                if HT == 'H':
                    if not([j,i] in E_log[z]) and i<j:
                        E_log[z].append([i,j])
    
    z+=1

#Grafi con p = 0.5 (per diversi valori di n)
z = 0
index_E_un=[]
for k in n:
    index_E_un.append([k,pun[z]])
    print "k=",k
    for i in range(0,k):
        #print i
        for j in range(0,k):
            if i!=j:
                HT = flip(pun[z])
                if HT == 'H':
                    if not([j,i] in E_un[z])and i<j:
                        E_un[z].append([i,j])
    #print z
    z+=1
             

path_sqrt ='RandomGraphs/sqrt/'



#Creazione file dei grafi per sqrt
a = 0
for i in range(0,len(n)):
    lista =list()
    for j in E_sqrt[a]:
        lista.append(j[0])
        lista.append(j[1])
    nome_file_sqrt ='input_'+str(n[i])+'.txt'
    outF = open(path_sqrt+nome_file_sqrt, "w")
    outF.write(str(n[i]))
    outF.write(" ")
    outF.write(str(len(E_sqrt[i])))
    outF.write("\n")
    
    s = map(str, lista) 
    
    for line in range(0,len(s),2):
            outF.write(s[line])
            outF.write(" ")
            outF.write(s[line+1])
            outF.write("\n")
    outF.close()
    a+=1

#Creazione file dei grafi per log
path_log='RandomGraphs/log/'
a = 0
for i in range(0,len(n)):
    lista =list()
    for j in E_log[a]:
        lista.append(j[0])
        lista.append(j[1])
    nome_file_log ='input_'+str(n[i])+'.txt'
    outF = open(path_log+nome_file_log, "w")
    outF.write(str(n[i]))
    outF.write(" ")
    outF.write(str(len(E_log[i])))
    outF.write("\n")
    
    s = map(str, lista) 
    
    for line in range(0,len(s),2):
            outF.write(s[line])
            outF.write(" ")
            outF.write(s[line+1])
            outF.write("\n")
    outF.close()
    a+=1

#Creazione file dei grafi per inv
path_inv='RandomGraphs/inv/'
a = 0
for i in range(0,len(n)):
    lista =list()
    for j in E_inv[a]:
        lista.append(j[0])
        lista.append(j[1])
    nome_file_inv ='input_'+str(n[i])+'.txt'
    outF = open(path_inv+nome_file_inv, "w")
    outF.write(str(n[i]))
    outF.write(" ")
    outF.write(str(len(E_inv[i])))
    outF.write("\n")
    
    s = map(str, lista) 
    
    for line in range(0,len(s),2):
            outF.write(s[line])
            outF.write(" ")
            outF.write(s[line+1])
            outF.write("\n")
    outF.close()
    a+=1

#Creazione file dei grafi per un
path_un='RandomGraphs/un/'
a = 0
for i in range(0,len(n)):
    lista =list()
    for j in E_un[a]:
        lista.append(j[0])
        lista.append(j[1])
    nome_file_un ='input_'+str(n[i])+'.txt'
    outF = open(path_un+nome_file_un, "w")
    outF.write(str(n[i]))
    outF.write(" ")
    outF.write(str(len(E_un[i])))
    outF.write("\n")
    
    s = map(str, lista) 
    
    for line in range(0,len(s),2):
            outF.write(s[line])
            outF.write(" ")
            outF.write(s[line+1])
            outF.write("\n")
    outF.close()
    a+=1

#Grafi con p = 1/n (per diversi valori di n)
z = 0
index_E_inv_bf=[]
#for k in n:
#index_E_inv_bf.append([20,pinv[z]])
for i in range(0,20):
        #print i
    for j in range(0,20):
        if i!=j:
            HT = flip(0.5)
            if HT == 'H':
                if not([j,i] in E_inv_bf):
                    E_inv_bf.append([i,j])
    
#Creazione file di un grafo di 20 nodi con p =1/2 per testare l'lagoritmo di Brute Force
path_inv='RandomGraphs/un/bf/'
a = 0
lista = []
    
for j in E_inv_bf:
    lista.append(j[0])
    lista.append(j[1])
nome_file_inv ='input_'+str(20)+'.txt'
outF = open(path_inv+nome_file_inv, "w")
outF.write(str(20))
outF.write(" ")
outF.write(str(len(E_inv_bf)))
outF.write("\n")
    
s = map(str, lista) 
    
for line in range(0,len(s),2):
        outF.write(s[line])
        outF.write(" ")
        outF.write(s[line+1])
        outF.write("\n")
outF.close()


