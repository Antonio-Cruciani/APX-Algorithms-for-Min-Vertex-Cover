import copy 
import itertools
import time
import sys
import matplotlib.pyplot as plt


#Struttura dati per grafo (Lista di adiacenza)
class Graph:

    def __init__(self, vertices, is_undirected=True):
        self.__v = vertices  # numero di vertici
        self.__edge_list = []  # salva gli archi e gli eventuali pesi (non serve)
        self.__is_undirected = is_undirected # Valore = True per grafi non diretti
        #self.__adj_matrix = None 
        self.__adj_list = None # Lista di adiacenza
        self.__vertici = []#Insieme dei vertici che sono collegati da nodi (non disconnessi)
        self.__covers = [] #Insieme dei nodi coperti 
        
    # Metodo che permette di aggiungere un nuvo aro al grafo
    def add_edge(self, u, v, w=None):
        self.__edge_list.append([u, v, w if w else 1])
        # Se G non è un Digrafo, 
        # copia gli archi nella direzione opposta
        if self.__is_undirected:
            self.__edge_list.append([v, u, w if w else 1])

    # Metodo che costruisce la lista di adiacenza
    def make_adjacency_list(self):
        adj_list = {key: [] for key in range(self.__v)}
        for edge in self.__edge_list:
            # Dove edge[1] è  la destinazione ed un eventuale edge[2] il peso
            edge_val = {edge[1]} 
            adj_list[edge[0]].append(edge_val)
        self.__adj_list = adj_list
        vertici = list()
        for keyvalue in self.__adj_list.items():
            if len(keyvalue[1])!=0: 
                vertici.append(keyvalue[0])
        self.__vertici = vertici
        
    # Metodo che ritorna la lista dei vertici
    def get_vertex_list(self):
        vertici = list()
        
        adj_list = self.get_adj_list()
        for key in range(self.__v):
            if len(adj_list[key])!=0: 
                vertici.append(key)
               
        self.__vertici = vertici
        
    #Metodo che inizializza il cover di tutti i nodi a falso
    def set_false_cover_list(self):
        vertici = list()
        adj_list = self.get_adj_list()
        for key in range(self.__v):

            if(len(adj_list[key])!=0):
                vertici.append([key])
                
        for i in range(0,len(vertici)):
            vertici[i].append("False")
        self.__covers=vertici
        #print vertici
    # Metodo che ritorna la lista dei nodi coperti    
    def get_cover_list(self):
        return self.__covers
    
    #Metodo che marca il nodo scelto e marca gli archi
    def cover(self,lista_nodi):
        #print self.__covers
        for i in lista_nodi:
            self.__covers[i]="True"
            
        return self.__covers
    
    #Il seguente metodo ritorna la lista di adiacenza 
    def get_adj_list(self):
        return self.__adj_list
    
    #Il seguente metodo permette di eliminare un nodo dalla lista di adiacenza
    def remove_edge(self,u):
        del self.__adj_list[u]
        adj={key:[]for key in range(self.__v)}
        #print adj
        for k, v in self.__adj_list.items():
            for h in v:
                if not(u in h):
                    #print "chiave=",k,"valore=", v
                    #print h
                    adj[k].append(h)
                    #print adj[k]
        #print " stampo adj"
        #print adj
        #print type(adj)
        self.__adj_list = adj
        #print self.__adj_list
        
    # Metodo che ritorna la lunghezza della lista definita sul nodo u
    # Ovvero metodo che permette di calcolare il grado del nodo u
    def get_lenvalues(self,u):
        return len(self.__adj_list[u])
    def get_vertex_list(self):
        return self.__vertici
    
    # Metodo che ritorna la chiave della lista di adiacenza che ha il maggior numero di valori nella lista
    # Ovvero, il nodo con grado maggiore.
    def get_key_max_degree(self):
        l = 0
        k = 0
        for keyvalue in self.__adj_list.items():
            key, value = keyvalue[0], keyvalue[1]
            #print key,value,len(value)
            if len(value) >= l:
                l = len(value)
                k = key
        return k
        #return self.__adj_list[max(len(self.__adj_list))]

    # Metodo che ritorna il grado del nodo di grado massimo
    def get_value_max_degree(self):
        l = 0
        k = 0
        for keyvalue in self.__adj_list.items():
            value = keyvalue[1]
            #print key,value,len(value)
            if len(value) >= l:
                l = len(value)
        return l
        
    #Metodo che ritorna due nodi qualsiasi connessi tra di loro
    def get_node(self):
        for keyvalue in self.__adj_list.items():
            if len(keyvalue[1])!=0:
                #print keyvalue[1]
                return keyvalue[0],keyvalue[1][0]
    
#Funzione che legge i parametri di input dal file input.txt e costruisce l'istanza G=(V,E)      
def get_input_param(path = None):
    vertices=list()
    if(path == None):
        source = 'input.txt'
    else:
        source = path
        #print path
    with open(source,'r') as f:
        #j=0
        i=0
        for line in f:
            #print line
            k=list()
            j=0
            for word in line.split():
                if j == 0 and i ==0:
                    n = int(word)
                    G = Graph(n)
                elif j == 1 and i == 0:
                    m = int(word)
                else: 
                    if word != line.split():
                        k.append(int(word)) 

                j+=1
            if i>0:
                if len(k)>0:
                    G.add_edge(int(k[0]),int(k[1]))
            i+=1
        G.make_adjacency_list()
        G.get_vertex_list()
        G.set_false_cover_list()
        return G
# Funzione che scrive i risultati sul file output.txt o su un file output riguardante una classe di grafo random  
def write_on_file_results(solution,Greedy = False, Matching = False, Bforce = False,path= None,d=None):
    if(Greedy == False and Matching == False and Bforce == False and path== False and d==None):
        return -1
    if(Greedy == True and Matching == False and Bforce == False and path== None and d==None):
        outF = open("OutputGreedy.txt", "w")
    if(Matching == True and Greedy == False and Bforce == False and path== None and d==None):
        outF = open("OutputMatching.txt", "w")
    if(Matching == False and Greedy == False and Bforce == True and path== None and d==None):
        outF = open("OutputBruteForce.txt", "w")
    if(Greedy == False and Matching == False and Bforce == False and path != None and d!=None):
        return -1
    if(Greedy == True and Matching == False and Bforce == False and path != None and d!=None):
        outF = open(path+"OutputGreedy_"+d, "w")
    if(Matching == True and Greedy == False and Bforce == False and path != None and d!=None):
        outF = open(path+"OutputMatching_"+d, "w")
    if(Matching == False and Greedy == False and Bforce == True and path != None and d!=None):
        outF = open(path+"OutputBruteForce_"+d, "w")
    s = map(str, solution) 
    k = [str(len(solution))]
    
    textList =k+s
    #print textList
    for line in textList:
        outF.write(line)
        outF.write("\n")
    outF.close()    
   


 # Funzione che ritorna l'inseme delle parti di una lista
def get_power_set(s):
    power_set=[[]]
    for elem in s:
    # iterate over the sub sets so far
        for sub_set in power_set:
              # add a new subset consisting of the subset at hand added elem
            power_set=power_set+[list(sub_set)+[elem]]
    power_set.pop(0)
    return power_set

# print sorted solutions
def get_sorted_solutions(lista):
    h = sorted(lista, key=lambda x: x[1])
    for i in range(0,4):
        print li[i][0:2]
# Funzione che stampa le soluzioni dei due algoritmi: greedy e matching
def print_solutions(lista_1,lista_2):
    n =['50','100','500','1000']

    print "+n----------Greedy------------Matching-------------+"
    for i in range(0,4):
            print n[i],"----------",lista_1[i][1],"------------",lista_2[i][1],"-------------|"
    print "+---------------------------------------------------+"

def GreedyMinVertexCover(source = None):
    G= get_input_param(source)
    G.get_adj_list()
    S = list()
    start = time.time()
    while len(G.get_adj_list())!=0:
            k = G.get_key_max_degree()
            #print k
            #print G.get_adj_list()
            if G.get_lenvalues(k) != 0:
                S.append(k)
            else:
                break
            G.remove_edge(k)
            #print G.get_adj_list()
    stop = time.time()
    duration = stop-start
    print "Il min Vertex Cover è =",S,"La sua cardinalità è =",len(S),"L'algoritmo Greedy Min Vertex Cover ha impiegato = ",duration
    return S,duration

    def Matching(source = None):
    
    G = get_input_param(source)
    
    S =list()
    
    start=time.time()
    while G.get_lenvalues(G.get_key_max_degree()) !=0:
        #print G.get_adj_list()
        u,v1 = G.get_node()
        
        v = list(v1)
        p = int(v[0])

        G.remove_edge(u)
        G.remove_edge(p)
        S.append(u)
        S.append(p)
    stop = time.time()
    duration = stop-start
    print "Il min Vertex Cover è =",S," La sua cardinalità è =",len(S),"L'algoritmo Matching Min Vertex Cover ha impiegato = ",duration
    return S,duration

def MinVertexCoverExhaustive(source = None):
    G = get_input_param(source)
    #Generazione dell'insieme delle parti 
    ps = get_power_set(G.get_vertex_list())
    j=0
    k= float("inf")
    start = time.time()
    for i in ps:
        grafo=get_input_param(source)
        #print grafo.get_adj_list()
        #i.remove_edge(u)
        #print ps[j]
        for c in ps[j]:
            grafo.remove_edge(c)
            
        grafo.cover(ps[j])
        
        if grafo.get_value_max_degree() == 0:
            
            if k>len(ps[j]):
                k=len(ps[j])
                index = j
        j+=1
    stop = time.time()
    duration = stop-start
    print "Il min Vertex Cover è =",ps[index],"La sua cardinalità è =",k," Il tempo impiegato dall'algoritmo esaustivo è =",duration
    return ps[index],duration
 

   
          
