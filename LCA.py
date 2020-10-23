import unittest

class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def lca(root, n1, n2): 
      
     
    if root is None: 
        return None
  
     
    if(root.data > n1 and root.data > n2): 
        return lca(root.left, n1, n2) 
  
    
    if(root.data < n1 and root.data < n2): 
        return lca(root.right, n1, n2) 
  
    return root 

class LCAUnitTest(unittest.TestCase):
    def test_upper(self):
        root = Node(20) 
        root.left = Node(8) 
        root.right = Node(22) 
        root.left.left = Node(4) 
        root.left.right = Node(12) 
        root.left.right.left = Node(10) 
        root.left.right.right = Node(14)
        
        n1 = 10 ; n2 = 14
        t = lca(root, n1, n2) 
        self.assertEqual(12, t.data) 
        
        n1 = 14 ; n2 = 8
        t = lca(root, n1, n2) 
        self.assertEqual(8, t.data) 
        
        n1 = 10 ; n2 = 22
        t = lca(root, n1, n2) 
        self.assertEqual(20, t.data) 
    
    
if __name__ == '__main__':
    unittest.main()