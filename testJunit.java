import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class testJunit 
{
	//~ Constructor ........................................................
	@Test
	public BinaryTree testConstructor() {
		BinaryTree tree = new BinaryTree();
		tree.root = new Node(20); 
        tree.root.left = new Node(8); 
        tree.root.right = new Node(22); 
        tree.root.left.left = new Node(4); 
        tree.root.left.right = new Node(12); 
        tree.root.left.right.left = new Node(10); 
        tree.root.left.right.right = new Node(14);
        return tree;
	}

	
	//~ Public Methods ........................................................

    // ----------------------------------------------------------
    /**
     * Check that the methods work for empty tree
     */
    @Test
    public void testEmptyTree()
    {
    	BinaryTree tree = new BinaryTree();
    	int n1 = 10, n2 = 14; 
    	Node t = tree.lca(tree.root, n1, n2);
    	assertEquals("Checking height of null height tree", null, t);
    }
    
    /**
     * Check that the methods work for populated tree 
     */
    @Test
    public void testNoCommonAncestor()
    {
    	BinaryTree tree = testConstructor();
    	int n1 = 10, n2 = 14; 
    	Node t = tree.lca(tree.root, n1, n2);
    	assertEquals("Checking height of null height tree", 12, t.data);
    }
    
}
