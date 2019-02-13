
import Cal as cal

class Graph :
    def __init__ (self ,trans_energy_matrix , ect , ecr , efs , emp , Adjacent_matrix) :
        self.ect = ect
        self.ecr = ecr
        self.efs = efs
        self.emp = emp
        self.trans_energy_matrix = trans_energy_matrix
        self.weighted_matrix = Adjacent_matrix #2d numpy array

        """#set infinity for all '0' in Adjacent_matrix
        for l in self.weighted_matrix :
            for i in l :
                if i == 0 :
                    i = len(self.weighted_matrix)**2 * (self.es + self.er)"""

    def set_edge (self , i , j , T , Time_slices_set) :
        if j not in T.get_Vertices_set() :
            self.weighted_matrix[i,j] = self.trans_energy_matrix[i,j] + self.ecr
        else :
            #Time_slices_set is a normal 2d array            if T.child(j) != [] :
            c1 = [Time_slices_set[x] for x in T.child(j)]
            c2 = c1.copy()
            c2.append(Time_slices_set[i])
            self.weighted_matrix[i,j] = abs(len(cal.MHS(c2)) - len(cal.MHS(c1))) * self.trans_energy_matrix[i,j] + self.ecr

    def get_graph(self) :
        return self.weighted_matrix
