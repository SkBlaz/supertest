## this file contains some of the multilayer network analysis network
## algorithms, used in the BioGrid analysis
import networkx as nx
from collections import defaultdict
import numpy as np
import itertools

class multiplex_network:

    def __init__(self,networks,edges,name):
        self.networks = networks
        self.multiedges = edges
        self.name = name

    def print_basic_info(self):
        print("MULTIPLEX OBJECT DESCRIPTION")
        print("Number of layers",len(self.networks))
        print("Number of multiedges",len(self.multiedges))

    def inter_community_influence(self,minclique):

        if self.multiedges == []:
            return {'multiplex_community_percentage' : 0}
        
        communities = {}
        for nid,network in enumerate(self.networks):
            communities[nid] = nx.k_clique_communities(network, minclique)

        partial_mpx_community = 0

        nmpx = 0
        mpx = 0
        
        for k,v in communities.items():

            ## check all communities, accross all networks
            for node in v:
                try:
                    mpx = False
                    
                    ## check individual multiedges
                    for x,y in self.multiedges:
                        if node == x or node == y:
                            mpx = True
                    if mpx:
                        mpx += 1
                    else:
                        mmpx += 1                    
                except:
                    pass

        if mpx > 0:
            return {'multiplex_community_percentage' : nmpx*100/mpx}


    def degree_layerwise_stats(self):

        ## This algorithm computes the layer-wise degree stats        
        all_degrees = [sum(nx.degree(X).values())/len(X) for X in self.networks]
        variance = np.var(all_degrees)
        sd = np.std(all_degrees)
        mean = np.mean(all_degrees)

        ## result object
        result = {'variance' : variance,'sd' : sd,'mean' : mean}
        return result        

    def multiplex_degree_gain(self):

        ## for each multiplex edge, check its degree and compare to layer mean degree
        pass
