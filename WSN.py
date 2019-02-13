import numpy as np

class WSN :
    def __init__(self , Tranmission_range , ect , ecr , efs , emp , terminal_nodes_set_M , Coordinate_matrix , Time_slices_set ) :
        self.Coordinate_matrix = Coordinate_matrix #2d numpy array
        self.Tranmission_range = Tranmission_range
        self.ect = ect
        self.ecr  = ecr
        self.efs = efs
        self.emp = emp
        d0 = np.sqrt(self.efs/self.emp) if self.emp != 0 else 0
        self.Time_slices_set = Time_slices_set # normal 2d array
        self.terminal_nodes_set_M = terminal_nodes_set_M
        self.source_node = 0
        self.trans_energy_matrix = np.array([[0 for i in range(len(self.Coordinate_matrix))] for _ in range(len(self.Coordinate_matrix))] )
        #build G
        self.graph_G = np.array([[0 for i in range(len(self.Coordinate_matrix))] for _ in range(len(self.Coordinate_matrix))] )
        for i in range(len(self.Coordinate_matrix)) :
            for j in range(len(self.Coordinate_matrix)) :
                x = np.sqrt((self.Coordinate_matrix[i,0]-self.Coordinate_matrix[j,0])**2 + (self.Coordinate_matrix[i,1] - self.Coordinate_matrix[j,1])**2)
                if (x > 0 and x <= self.Tranmission_range) :
                    self.graph_G[i,j] = 1
                    self.trans_energy_matrix[i,j] = (self.ect + self.efs * x**2) if x < d0 else (self.ect + self.emp * x**4)


    def get_G(self) :
        return self.graph_G

    def has_node_connection(self , i , j) :
        return self.graph_G[i,j]

    def get_number_of_nodes(self) :
        return len(self.Time_slices_set)

    def get_M(self) :
        return self.terminal_nodes_set_M

    def get_time_slices_set (self) :
        return self.Time_slices_set

    def get_time_slices(self , i) :
        return self.Time_slices_set[i]
