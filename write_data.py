import matplotlib.pyplot as plt

class write :
    def show (nodes_pos,nodes_in_tree,terminal_nodes_set_M) :

        fig = plt.figure(figsize=(11,11))

        for l in nodes_in_tree :
            for x , y in l :
                plt.plot([x[0],y[0]],[x[1] , y[1]],'b-')

        for i in range(len(nodes_pos)) :
            if i in terminal_nodes_set_M :
                plt.plot(nodes_pos[i][0],nodes_pos[i][1],'ko')
            else :
                plt.plot(nodes_pos[i][0],nodes_pos[i][1],'ro')

        #plt.axis([0, 20, 0, 20])
        fig.suptitle('Result with uniform distribution' , fontsize = 16)
        plt.show()
        fig.savefig('result\\result(uniform).png', bbox_inches='tight')
        plt.close(fig='result\\result(uniform).png.png')
