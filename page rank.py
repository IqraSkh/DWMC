#Page rank
import networkx as nx 
G=nx.barabasi_albert_graph(60,41) 
pr=nx.pagerank(G,0.4) 
print(pr)