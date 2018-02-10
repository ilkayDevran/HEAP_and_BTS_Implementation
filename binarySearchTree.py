from __future__ import division

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Tree():

    def __init__(self):
        self.root = None

    def Inorder_Tree_Walk(self, node):

        if node is not None:
            self.Inorder_Tree_Walk(node.left)
            print node.key,
            self.Inorder_Tree_Walk(node.right)

    def Tree_search(self, key, node=None):
        if node is None:
            node = self.root

        if self.root.key == key:
            #print "Key is at the ROOT! (From search method)"
            return self.root

        else:
            if node.key == key:
                #print "Key EXISTS! (From search method)"
                return node

            elif key < node.key and node.left is not None:
                #print "left"
                return self.Tree_search(key, node=node.left)

            elif key > node.key and node.right is not None:
                #print "right"
                return self.Tree_search(key, node=node.right)

            else:
                #print "Key does NOT exist! (From search method)"
                return None

    def Tree_Minimum(self, node=None):  #Running time O(h), h- height of tree

        if node is None:
            node = self.root

        while node.left is not None:
            node = node.left
        #print "Minimum key is:",node.key
        return node

    def Tree_Maximum(self,node=None):

        if node is None:
            node = self.root

        while node.right is not None:
            node = node.right
        #print "Maximum key is:",node.key
        return node

    def Tree_Successor(self,key,node=None):

        if node is None:
            node = self.Tree_search(key)
            current = node

        if node.right is not None:
            return self.Tree_Minimum(node=node.right)

        parent_node = node.parent
        while parent_node is not None and node is parent_node.right:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node == None:
            print str(key)+' is the largerst key no-successor exists'
            return current
        else:
            return parent_node

    def Tree_Predecessor(self,key,node=None):

        if node is None:
            node = self.Tree_search(key)
            current = node

        if node.left is not None:
            return self.Tree_Maximum(node=node.left)

        parent_node = node.parent
        while parent_node is not None and node is parent_node.left:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node == None:
            print str(key)+' is the largerst key no-predecessor exists'
            return current
        else:
            return parent_node

    def Tree_Insert(self,key,node=None): #insert method

        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(key)

        else:

            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    #print "left"
                    return
                else:
                    # return self.add_node(key,node = self.root.left)
                    return self.Tree_Insert(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    #print "right"
                    return
                else:
                    # return self.add_node(key,node = self.root.right)
                    return self.Tree_Insert(key, node=node.right)

    def Tree_Delete(self, key, node=None):
        # search for the node to be deleted in tree
        if node is None:
            node = self.Tree_search(key)  # return the node to be deleted

        # root has no parent node
        if self.root.key == node.key:  # if it is root
            parent_node = self.root
        else:
            parent_node = node.parent

        '''case 1: The node has no chidren'''
        if node.left is None and node.right is None:
            if key <= parent_node.key:
                parent_node.left = None
            else:
                parent_node.right = None
            return

        '''case 2: The node has children'''
        ''' if it has a single left node'''
        if node.left is not None and node.right is None:
            if node.left.key < parent_node.key:
                parent_node.left = node.left
            else:
                parent_node.right = node.left

            return

        '''if it has a single right node'''
        if node.right is not None and node.left is None:
            if node.key <= parent_node.key:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
            return

        '''case 3: if it has two children'''
        '''find the node with the minimum value from the right subtree.
           copy its value to thhe node which needs to be removed.
           right subtree now has a duplicate and so remove it.'''
        if node.left is not None and node.right is not None:
            min_value = self.Tree_Minimum(node)
            node.key = min_value.key
            min_value.parent.left = None
            return

    def Tree_max_path_length(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(self.Tree_max_path_length(node.left), self.Tree_max_path_length(node.right))

    def Tree_min_path_length(self,node):
        if node is None:
            return 0
        else:
            return 1 + min(self.Tree_min_path_length(node.left), self.Tree_min_path_length(node.right))

    def Tree_ratio_length(self):
        return self.Tree_min_path_length(self.root)/self.Tree_max_path_length(self.root)

def CREATE_BST(list):
    t = Tree()
    for i  in range(len(list)):
        t.Tree_Insert(list[i])

    print "\n---TREE INFO---\n"

    print "INORDER WALK: ",
    t.Inorder_Tree_Walk(t.root)


    print "\nSEARCH for "+str(list[0])+"\t-->",
    if t.Tree_search(list[0]) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"
    print "SEARCH for " + str(list[5]) + "\t-->",
    if t.Tree_search(list[5]) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"
    print "SEARCH for " + str(list[0]*2) + "\t-->",
    if t.Tree_search(list[0]*2) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"


    print "Minimum key in the Tree: " + str(t.Tree_Minimum().key)
    print "Maximum key in the Tree: " + str(t.Tree_Maximum().key)

    print "Successor of " + str(list[4]) + " is", t.Tree_Successor(list[4]).key
    print "Predecessor of "+ str(list[4]) + " is", t.Tree_Predecessor(list[4]).key

    print "Delete root " + str(list[0]) + ":",
    t.Tree_Delete(list[0])
    t.Inorder_Tree_Walk(t.root)

    print "\nHeight of the Tree: " + str(t.Tree_max_path_length(t.root))
    print "Depth of the Tree: " + str(t.Tree_min_path_length(t.root))
    print "Ration Depth/Height: " + str(t.Tree_ratio_length())

    print "\n"

def generateRandomArray(length,rng):
	from random import randint
	List=[randint(0,length) for i in range(rng)]
	return List

def main():
    CREATE_BST(generateRandomArray(30, 100))
    CREATE_BST(generateRandomArray(50, 1000))
    CREATE_BST(generateRandomArray(100, 500))

if __name__ == '__main__':
    main()