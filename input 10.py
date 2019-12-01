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
for x in range(0,29,3):
    pos[l[x]]=(float(l[x+1]),float(l[x+2]))
# print(pos)

G=nx.DiGraph()
# nx.set_node_attributes(G,'coord',pos)
G.add_nodes_from(pos.keys())
# print(G.nodes())

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
        G.add_edge(from_node,to_node)
    elif(float(l[i])<50 and float(l[i-1])>50):
        to_node=int(l[i])
        weight=float(l[i+2])/10000000
        print(from_node,to_node,weight)
        G.add_edge(from_node,to_node)


pos=nx.spring_layout(G)
# print(G.nodes())
fig,ax = plt.subplots()
# plt.ax('on')
plt.xlabel('x')
plt.ylabel('y')
nx.draw_networkx(G,pos,ax=ax)
# plt.plot(x,y)
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.savefig("simple_path.png")
plt.show()
# l=[]
# temp =file.read()
# for i in (temp.split()):
#     l.append(i);
# print(l)
# from_node=0
# to_node=0
# for i in range(100):
#     if(float(l[i])<50 and float(l[i+1])<50):
#         from_node=int(l[i])
#         to_node=int(l[i+1])
#         weight=float(l[i+3])/10000000
#         ++i
#         print(from_node,to_node,weight)
#     elif(float(l[i])<50 and float(l[i-1])>50):
#         to_node=int(l[i])
#         weight=float(l[i+2])/10000000
#         print(from_node,to_node,weight)

