import numpy as np
from collections import defaultdict
import random

from Multicast_Tree import Multicast_Tree as mt
from Graph import Graph as GG
import Cal as cal

class HMEM :

    def __init__(self,G,trans_energy_matrix,ect,ecr,efs,emp,Time_slices_set,terminal_set) :
         self.G = G
         self.trans_energy_matrix = trans_energy_matrix
         self.Time_slices_set = Time_slices_set
         self.terminal_set = terminal_set
         self.source_node = 0
         self.ect = ect
         self.ecr  = ecr
         self.efs = efs
         self.emp = emp
         sett = set()
         sett.add(self.source_node)
         self.T = mt(sett)
         self.B = defaultdict(list)


    def build_T(self) :
        sett = set()
        sett = {self.source_node}
        T = mt(sett)
        l = np.trim_zeros(self.terminal_set)
        for u in l :

            #build G'
            g = GG(self.trans_energy_matrix, self.ect , self.ecr , self.efs , self.emp ,self.G)
            for i in range(len(self.G)) :
                for j in range(len(self.G)) :
                    """if T.has_edge(i,j) :
                        g.weighted_matrix[i,j] = 0
                        g.weighted_matrix[j,i] = 0 #no connection"""
                    if self.G[i,j] :
                        g.set_edge(i,j,T,self.Time_slices_set)

            #find_shortest_path Pu
            v = random.choice(list(T.get_Vertices_set()))
            Pu = cal.find_shortest_path(u , v , g.get_graph())


            #add path Pu to current Tree
            for i in range(len(Pu) - 1) :
                T.add_edge(Pu[i+1],Pu[i])
                if Pu[i+1] in T.get_Vertices_set() :
                    for j in range(i+1) :
                        T.Vertices_set_add(Pu[j])
                    break
        return T

    def build_B(self) :
        B = defaultdict(list)
        for u in self.T.get_nl_set() :

            B[u] = cal.MHS([self.Time_slices_set[x] for x in self.T.child(u)] )

        return B

    def total_energy(self , T , B) :
        sums = 0
        for u in self.T.get_nl_set() :
            max_energy = 0
            for v in T.child(u) :
                if self.trans_energy_matrix[u][v] > max_energy :
                    max_energy = self.trans_energy_matrix[u][v]
            sums+= len(B[u])*max_energy + self.ecr
        return sums

    def build(self):
        self.T = HMEM.build_T(self)
        self.B = HMEM.build_B(self)
        self.Energy = HMEM.total_energy(self ,self.T , self.B)
