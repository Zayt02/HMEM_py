from WSN import WSN
import numpy as np
from HMEM import HMEM
from write_data import write as wd

def initialize_WSN() :
    file = open('test_data\\test1(uniform).txt' , 'r')

    Node = file.readline()
    node = int(''.join([x for x in Node[33:36]]))
    Tranmission_range = int(file.readline().strip())
    e = [float(x) for x in file.readline().strip().split()]
    ect,ecr = e[:2]
    efs,emp = e[2:]
    terminal_nodes_set_M = [int(x) for x in file.readline().strip().split()]
    Coordinate_matrix = np.array([[0 , 0] for _ in range(node)])
    Time_slices_set = [[] for _ in range(node)]

    for i in range(node) :
        l = [x for x in file.readline().strip().split()]
        Coordinate_matrix[i, 0] = float(l[0])
        Coordinate_matrix[i, 1] = float(l[1])
        Time_slices_set[i] = [int(x) for x in l[2:]]

    return WSN(Tranmission_range , ect , ecr , efs , emp , terminal_nodes_set_M , Coordinate_matrix , Time_slices_set)

if __name__ == '__main__':
    wsn = initialize_WSN()
    # print(wsn.graph_G,'\n',wsn.trans_energy_matrix)
    hmem1 = HMEM(wsn.get_G(),wsn.trans_energy_matrix , wsn.ect , wsn.ecr ,wsn.efs ,wsn.emp , wsn.get_time_slices_set() , wsn.get_M())
    hmem1.build()

    for _ in range(10) :
        print('Lan lap thu :',_)
        hmemx = HMEM(wsn.get_G(),wsn.trans_energy_matrix , wsn.ect , wsn.ecr ,wsn.efs ,wsn.emp , wsn.get_time_slices_set() , wsn.get_M())
        hmemx.build()
        if hmemx.Energy < hmem1.Energy :
            hmem1 = hmemx
    print('Tong nang luong la:',hmem1.Energy)
    for u in hmem1.B :
        print(u,hmem1.B[u])
    x = []
    i = -1
    for u in hmem1.T.get_Edge_set() :
        if hmem1.T.get_Edge_set()[u] != set() :
            x.append([])
            i+=1
            for v in hmem1.T.get_Edge_set()[u] :
                x[i].append([wsn.Coordinate_matrix[u] , wsn.Coordinate_matrix[v]])

    wd.show(wsn.Coordinate_matrix , x, wsn.get_M())
