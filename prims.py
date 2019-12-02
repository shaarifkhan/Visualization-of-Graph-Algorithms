import networkx as nx
import matplotlib.pyplot as plt
file = open('benchmark/input10.txt',"r")
import re

loop=0
for x in range(3):
    loop= file.readline()

l = []
for x in range(int(loop)+1):
    line=file.readline()
    for t in line.split():
        l.append(t)
pos={}
print(len(l))
for x in range(0,len(l)-1,3):
    pos[int(l[x])]=(float(l[x+1]),float(l[x+2]))
    # print(l[x])
# print(pos)

G=nx.Graph()
# nx.set_node_attributes(G,'coord',pos)
G.add_nodes_from(pos.keys())
# print(pos.keys())
# G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)])
# G.add_edges_from([(0,1)])

# for edges
l=[]
temp =file.read()
for i in (temp.split()):
    l.append(i);
# print(len(l))
from_node=0
to_node=0
for i in range(len(l)-1):
    if(float(l[i])<50 and float(l[i+1])<50):
        from_node=int(l[i])
        to_node=int(l[i+1])
        weight=float(l[i+3])/10000000
        ++i
        print(from_node,to_node,weight)
        G.add_edge(from_node,to_node,weight=weight)
    elif(float(l[i])<50 and float(l[i-1])>50):
        to_node=int(l[i])
        weight=float(l[i+2])/10000000
        print(from_node,to_node,weight)
        G.add_edge(from_node,to_node,weight=weight)


# dijktras path
# print(nx.bellman_ford_path(G, 0, 1, weight='weight'))
# distance,path = nx.single_source_dijkstra(G,0);
# print(path[2])
T=nx.minimum_spanning_tree(G,weight='weight',algorithm='prim')
# sorted(T.edges(data=True))

fig,ax = plt.subplots()
# plt.ax('on')
plt.xlabel('x')
plt.ylabel('y')
nx.draw_networkx(T,pos,ax=ax)
# plt.plot(x,y)
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.savefig("simple_path.png")
plt.show()
