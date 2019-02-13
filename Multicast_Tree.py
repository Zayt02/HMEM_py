
from collections import defaultdict

class Multicast_Tree :
    def __init__(self , Vertices_set) :
        self.Vertices_set = Vertices_set #set
        #self.Adjacent_matrix = Adjacent_matrix #2d numpy array
        self.Edge_set = defaultdict(set) #dict with key : set
        self.root = 0


    def Vertices_set_add(self , i) :
        self.Vertices_set.add(i)

    def get_Vertices_set(self) :
        return self.Vertices_set

    def add_edge(self , i , j) :
        self.Edge_set[i].add(j)

    def remove_edge(self, i ,j) :
        self.Edge_set[i].discard(j)

    def has_edge(self , i , j) :
        return (j in self.Edge_set[i] )

    def get_Edge_set(self) :
        return self.Edge_set

    def get_nl_set(self) :
        nl = set()

        for i in self.Edge_set :
            if len(self.Edge_set[i]) >=1 :
                nl.add(i)

        return nl

    def child(self , u) :
        l = []
        for i in self.Edge_set[u] :
            l.append(i)
        return l
