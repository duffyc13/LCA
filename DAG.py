import networkx as nx
import unittest

def DAG (g, n1, n2):
    
    lca = None
    
    # if graph is empty return nothing
    if (g.order() == 0):
        return lca
        
    # if graph has one node return that node
    if (g.order() == 1):
        return "root"
    
    # if x and y are equal then they are the lca
    if (n1 == n2):
        return n1
    
    predN1 = nx.ancestors(g, n1)
    predN2 = nx.ancestors(g, n2)
    setN1 = set(n1)
    setN2 = set(n2)
    
    # if n1 in set of parent nodes of n2 then return n1
    if bool(predN2.intersection(setN1)):
        return n1 
    
    # if n2 in set of parent nodes of n1 then return n2
    if bool(predN1.intersection(setN2)):
        return n2
    
    # find nodes in n1 ancestry in order
    n1Pred = set()
    tempNode1 = n1
    exit = 0
    while not exit:
        if len(list(g.predecessors(tempNode1))) != 0:
            node = next(g.predecessors(tempNode1))
            n1Pred.add(node)
            tempNode1 = node
        else:
            exit = 1

    # find nodes in n2 ancestry in order
    n2Pred = set()
    tempNode2 = n2
    exit = 0
    while not exit:
        if len(list(g.predecessors(tempNode2))) != 0:
            node = next(g.predecessors(tempNode2))
            n2Pred.add(node)
            tempNode2 = node
        else:
            exit = 1

    # Find common elements in parents 
    commonElements = list(n1Pred.intersection(n2Pred))
    lca = commonElements[-1]

    return lca

    

class DAGUnitTest(unittest.TestCase):
    def test_upper(self):
        
        # test empty
        graph = nx.DiGraph()
        self.assertEqual(None, DAG(graph, "a", "b"))
        
        # test root only graph
        graph.add_node("root")
        self.assertEqual("root", DAG(graph, "a", "b"))
        graph.remove_node("root")
        
        # test n2 an ancestor of n1
        graph.add_edges_from([("root", "1"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
        self.assertEqual("b", DAG(graph, "c", "b"))
        
        # test n2 an ancestor of n1
        graph1 = nx.DiGraph()
        graph1.add_edges_from([("root", "1"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
        self.assertEqual("b", DAG(graph, "b", "d"))
        
        # test LCA 
        graph2 = nx.DiGraph()
        graph2.add_edges_from([("root", "1"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
        self.assertEqual("a", DAG(graph, "e", "c"))
        
if __name__ == '__main__':
    unittest.main()
    
    