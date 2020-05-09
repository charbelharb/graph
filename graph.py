# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:27:06 2020

@author: Charbel Harb
"""

## run pip install networkx



import matplotlib.pyplot as plt
import networkx as nx


###################
##Exercice 2 - K5##
###################
labels_5={}
labels_5[0]='N₁'
labels_5[1]='N₂'
labels_5[2]='N₃'
labels_5[3]='N₄'
labels_5[4]='N₅'
#Complete Graph 5
complete_graph_5 = nx.complete_graph(5)
pos_complete_graph_5=nx.spring_layout(complete_graph_5)
nx.draw_networkx_nodes(complete_graph_5,pos_complete_graph_5,
                       nodelist=[0,1,2,3,4],
                       node_color='r',
                       node_size=3000,
                       alpha=0.8)
nx.draw_networkx_edges(complete_graph_5,pos_complete_graph_5,width=1.0,alpha=0.5)
nx.draw_networkx_labels(complete_graph_5,pos_complete_graph_5,labels_5,font_size=30)
plt.axis('off')
plt.show() 

#K5 spanning tree
k5_tree = nx.complete_graph(5)
edges_to_remove = [(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,2),(3,4)]
k5_tree.remove_edges_from(edges_to_remove)
pos_k5 = nx.spring_layout(k5_tree)
nx.draw_networkx_nodes(k5_tree,pos_k5,
                       nodelist=[0,1,2,3,4],
                       node_color='r',
                       node_size=3000,
                       alpha=0.8)
nx.draw_networkx_edges(k5_tree,pos_k5,width=1.0,alpha=0.5)
nx.draw_networkx_labels(k5_tree,pos_k5,labels_5,font_size=30)
plt.axis('off')
plt.show() 

###################################################################################

##############
##Exercice 3##
##############
labels_g = {}
labels_g[0] = 'A'
labels_g[1] = 'B'
labels_g[2] = 'C'
labels_g[3] = 'D'
labels_g[4] = 'E'
# G = {{A,B}, {A,D}, {B,D}, {B,C},{C,E}}
edges_to_add = [(0,1),(0,3),(1,3),(1,2),(2,4)]
graph_g = nx.Graph()
graph_g.add_edges_from(edges_to_add)
pos_g = nx.spring_layout(graph_g)
nx.draw_networkx_nodes(graph_g,pos_g,
                       nodelist=[0,1,2,3,4],
                       node_color='r',
                       node_size=3000,
                       alpha=0.8)
nx.draw_networkx_edges(graph_g,pos_g,width=1.0,alpha=0.5)
nx.draw_networkx_labels(graph_g,pos_g,labels_g,font_size=30)

# Check programmatically if it's a tree, should return False
nx.is_tree(graph_g)

# Calculate programmatically the matrix by node order: A,B,C,D,E
adjency_matrix = nx.adj_matrix(graph_g,[0,1,2,3,4])
print(adjency_matrix.todense())

plt.axis('off')
plt.show() 


##############
##Exercice 4##
##############
labels_k = {}
labels_k[0] = 'A'
labels_k[1] = 'B'
labels_k[2] = 'C'
labels_k[3] = 'D'
labels_k[4] = 'E'
labels_k[5] = 'F'
labels_k[6] = 'G'
graph_k = nx.Graph()

# {A,B}; e=5 
graph_k.add_edge(0,3,weight=5)

# {E,C}; e=5
graph_k.add_edge(4,2,weight=5)

# {D,F}; e=6
graph_k.add_edge(3,5,weight=6)

# {A,B}; e=7
graph_k.add_edge(0,1,weight=7)

# {B,E}; e=7
graph_k.add_edge(1,4,weight=7)

# {B,C}; e=8
graph_k.add_edge(1,2,weight=8)

# {E,F}; e=9
graph_k.add_edge(4,3,weight=9)

# {B,D}; e=9
graph_k.add_edge(1,3,weight=9)

# {E,G}; e=9
graph_k.add_edge(4,6,weight=9)

# {F,G}; e=11
graph_k.add_edge(5,6,weight=11)

# {D,E}; e=15
graph_k.add_edge(3,4,weight=15)

graph_k_mst = nx.minimum_spanning_tree(graph_k)
pos_k_mst = nx.spring_layout(graph_k_mst)
edge_weights = nx.get_edge_attributes(graph_k_mst,'weight')
nx.draw_networkx_nodes(graph_k_mst,pos_k_mst,
                       nodelist=[0,1,2,3,4,5,6],
                       node_color='r',
                       node_size=3000,
                       alpha=0.8)
nx.draw_networkx_edges(graph_k_mst,pos_k_mst,width=1.0,alpha=0.5)
nx.draw_networkx_labels(graph_k_mst,pos_k_mst,labels_k,font_size=30)
nx.draw_networkx_edge_labels(graph_k_mst,pos_k_mst,edge_labels=edge_weights,font_size=20)
plt.axis('off')
plt.show() 


##############
##Exercice 5##
##############
labels_e = {}
labels_e[0] = 'D'
labels_e[1] = 'A'
labels_e[2] = 'B'
labels_e[3]='C'

# Room A(1) + Outside(0) = Twice
# Room B(2) + Outside(0) = Twice
# Room C(3) + Outside(0) = Thrice
# Room A(1) + Room B(2) = Once
# Room A(1) + Room C(3) = Once
# Room B(2) + Room C(3) = Once
euler_edges = [(0,1),(0,1),(0,2),(0,2),(0,3),(0,3),(0,3),(1,2),(1,3),(2,3)]

# C- Solving the problem first way A:
# Adding door between Room C and Outside
# euler_edges.append((0,3))
# 
# Removing door between Room C and outside
#euler_edges.remove((0,3))

graph_euler = nx.MultiGraph()
graph_euler.add_edges_from(euler_edges)
pos_euler = nx.spring_layout(graph_euler)
nx.draw_networkx_nodes(graph_euler,pos_euler,
                       nodelist=[0,1,2,3],
                       node_color='r',
                       node_size=3000,
                       alpha=0.8)
nx.draw_networkx_edges(graph_euler,pos_euler,width=1.0,alpha=0.5)
nx.draw_networkx_labels(graph_euler,pos_euler,labels_e,font_size=30)
ax = plt.gca()
for e in graph_euler.edges:
    print(e)
    edge_color = "0.5"
    #if(e[1] == 3):
        #edge_color ="blue" 
    ax.annotate("",
                xy=pos_euler[e[0]], xycoords='data',
                xytext=pos_euler[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="->", color=edge_color,
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                ),
                                ),
                )
plt.axis('off')
plt.show()
