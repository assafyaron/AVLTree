#username - meravgilboa1
#id1      - 209383561 
#name1    - merav gilboa 
#id2      - 316595941
#name2    - assaf yaron  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
        """Constructor, you are allowed to add more fields. 

        @type key: int or None
        @type value: any
        @param value: data of your node
        """
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.left:AVLNode = None
                self.right:AVLNode = None
                self.parent:AVLNode = None
                self.height:int = -1
                self.isVirtual:bool = False



        """returns the left child

	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
        def get_left(self):
                if self.isVirtual: # the current node is virtual and has no left child
                        return None
                else:
                        return self.left



        """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
        def get_right(self):
                if self.isVirtual: # the current node is virtual and has no right child
                        return None
                else:
                        return self.right


        """returns the parent

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
        def get_parent(self):
                if self.isVirtual:
                        raise Exception("Tried to access the parent of a virtual node")
                return self.parent # if there is no parent (root), default is None


        """returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
        def get_key(self):
                if self.isVirtual: # if self is virtual it has no key
                        return None
                else:
                        return self.key


        """returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
        def get_value(self):
                if self.isVirtual: # if self is virtual it has no value
                        return None
                else:
                        return self.value

        """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
        def get_height(self):
                return self.height

        """returns the balance factor

	@rtype: int
	@returns: the balance factor of self, 0 if the node is virtual
	"""
        def get_bf(self):
                if self.isVirtual: # if self is virtual, return 0
                        return 0
                else:
                        return self.left.height-self.right.height

        """sets left child

	@type node: AVLNode
	@param node: a node
	"""
        def set_left(self, node):
                if self.isVirtual:
                        raise Exception("Tried to set a left child for a virtual node")
                self.left = node


        """sets right child

	@type node: AVLNode
	@param node: a node
	"""
        def set_right(self, node):
                if self.isVirtual:
                        raise Exception("Tried to set a right child for a virtual node")
                self.right = node


        """sets parent

	@type node: AVLNode
	@param node: a node
	"""
        def set_parent(self, node):
                if not self.isVirtual:
                        self.parent = node


        """sets key

	@type key: int or None
	@param key: key
	"""
        def set_key(self, key):
                if self.isVirtual:
                        raise Exception("Tried to set a key for a virtual node")
                self.key = key


        """sets value

	@type value: any
	@param value: data
	"""
        def set_value(self, value):
                if self.isVirtual:
                        raise Exception("Tried to set a value for a virtual node")
                self.value = value


        """sets the height of the node

	@type h: int
	@param h: the height
	"""
        def set_height(self, h):
                if self.isVirtual:
                        raise Exception("Tried to set height for a virtual node")
                self.height = h

        """changes status of node to virtual

        @returns: no return for function
        """
        def set_virtual(self):
                self.isVirtual = True

        """changes status of node to not virtual

        @returns: no return for function
        """
        def set_not_virtual(self):
                self.isVirtual = False
        
        """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
        def is_virtual(self):
                return self.isVirtual

        """returns whether node is a leaf

        @rtype: bool
        @returns: True if self is a leaf, False otherwise
        """
        def is_leaf(self):
                return self.right.isVirtual and self.left.isVirtual

        """returns whether node is a right or left son

        @pre: self has a father
        @rtype: bool
        @returns: True if self is a inner tree right son, False otherwise
        """
        def is_inner_node_right_son(self):
                if self.parent == None:
                        raise Exception("Tried to check if the root is a right son")
                return self.key > self.parent.key

        ######################################################
        ### NOT OUR CODE USED FOR PRINTING NODES AND TREES ###
        ######################################################

        def display(self):
                if self is None:
                        print("None Tree")
                        return
                lines, *_ = self._display_aux()
                for line in lines:
                        print(line)

        def _display_aux(self):
                """Returns list of strings, width, height, and horizontal coordinate of the root."""
                # No child.
                if self.right.key is None and self.left.key is None:
                        line = '%s' % self.key + "," + '%s' % self.get_height()
                        width = len(line)
                        height = 1
                        middle = width // 2
                        return [line], width, height, middle

                # Only left child.
                if self.right.key is None:
                        lines, n, p, x = self.left._display_aux()
                        s = '%s' % self.key + "," + '%s' % self.get_height()
                        u = len(s)
                        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                        shifted_lines = [line + u * ' ' for line in lines]
                        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

                # Only right child.
                if self.left.key is None:
                        lines, n, p, x = self.right._display_aux()
                        s = '%s' % self.key + "," + '%s' % self.get_height()
                        u = len(s)
                        first_line = s + x * '_' + (n - x) * ' '
                        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                        shifted_lines = [u * ' ' + line for line in lines]
                        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

                # Two children.
                left, n, p, x = self.left._display_aux()
                right, m, q, y = self.right._display_aux()
                s = '%s' % self.key + "," + '%s' % self.get_height()
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
                second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
                if p < q:
                        left += [n * ' '] * (q - p)
                elif q < p:
                        right += [m * ' '] * (p - q)
                zipped_lines = zip(left, right)
                lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
                return lines, n + m + u, max(p, q) + 2, n + u // 2




##############################
        
### NOTICE GLOBAL VARIABLE ###
        
"""
Global variable virtual son for all in need of one
"""
virtualNode = AVLNode(None, None)
virtualNode.set_virtual()

##############################

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

        """
	Constructor, you are allowed to add more fields.  

	"""
        def __init__(self):
                self.root = None
                self.tree_size = 0 



        """searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
        def search(self, key):

                """
                An AVL tree is also a BST, therfore we know keys are located in an orderly fashion.
                Using this and the fact an AVL is mostly balanced, we can implement a binary search on the tree:
                      1. going left if the current key is smaller than the desired one
                      2. going right if the current key is bigger than the desired one
                      3. return None if the key isn't found where it's 'supposed' to be
                """

                # RUNTIME = O(log(n))
                
                currNode = self.root

                # currNode is virtual when we have 'fallen' from the tree
                # currNode is None if the tree has no nodes to begin with
                while currNode.is_virtual() == False or currNode == None:
                        currKey = currNode.get_key()
                        if key == currKey:
                                return currNode
                        elif key < currKey:
                                currNode = currNode.get_left()
                        else:
                                currNode = currNode.get_right()

                # we have fallen from the true
                return None

	
        """returns the new node we wish to insert
        @type key: int
        @type val: any
        @rtype: AVLNode
        @returns: the new node 
        """
        def bst_tree_insert(self, key, val):

                """
                This is a helper function for the insert function.
                First we create the new node, give it virtual children, and set its height.
                Next, we give it a parent, and tell its parent it has a new right or left child.
                Finally return the new node.
                """

                # RUNTIME: O(1)

                designatedParent = self.bst_tree_position(key) # find designated parent
                newNode = AVLNode(key, val) # create new node

                # give the new node virtual children
                newNode.set_left(virtualNode)
                newNode.set_right(virtualNode)
                
                newNode.set_height(0) # leaf height is 0
                newNode.set_parent(designatedParent) # give it a parent
                newNode.set_not_virtual() # make sure it's not virtual

                # give the parent a child
                if key < designatedParent.key:
                        designatedParent.set_left(newNode)
                else:
                        designatedParent.set_right(newNode)

                return newNode


        
        """returns the desired location of a certain node using its key as compass

        @type key: int
        @rtype: AVLNode
        @returns: the node's designated father
        """
        def bst_tree_position(self, key):

                """
                This is a helper function for the insert function.
                Using the exact same logic as search, only with a small difference.
                In case we fall off the tree we can return back to the last node before we fell which
                will be the father of our new node.
                """

                # RUNTIME: O(log(n))

                currNode = self.root
                currParent = None
                while not currNode.is_virtual(): # currNode is virtual when we have fallen from the tree
                        currParent = currNode
                        currKey = currNode.get_key()

                        # keep looking for the desired location in the tree using binary search logic
                        if key < currKey:
                                currNode = currNode.get_left()
                        else:
                                currNode = currNode.get_right()

                # we have fallen from the tree, return the real parent node
                return currParent

        """balances tree according to the need: insertion or deletion
           the rotations to rule them all are defined as sub functions

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: int
        @returns: number of rotations used
        """
        def balance_sub_tree(self, pivot, balanceFactor):

                """
                First, check the balance factor of the given node. Now denote 4 turns to rule them all:
                1. BF = -2, and BF of right son is 1: perform right then left rotation (RL)
                2. BF = -2, and BF of right son is -1: perform left rotation (L)
                3. BF = 2, and BF of left son is -1: perform left then right rotation (LR)
                4. BF = 2, and BF of left son is 1: perfrom right rotation (R)

                Keep track of number of rebalancing operations.
                Raise Exception if we calculated a differnet BF then expected
                """

                # RUNTIME:

        ####################################
        ### nested rotation sub-function ###
        ####################################

                """implements right or left rotation as needed using a boolean indicator

                @type node: AVLNode
                @pre: node is a real pointer to a node in self
                @type clockWise: boolean
                @type isZigZag: boolean
                @returns: doesn't return anything
                """

                def rotation(node:AVLNode, clockWise, isZigZag):
                        """
                        The node we get is a child. We save its parent, and also a pointer to the parent of the whole subtree.
                        Next, we change pointers between the parent and his child.
                        Lastly, update root if needed
                        """
                        
                        # RUNTIME: O(1)

                        # saving variables
                        nonlocal numOfActions
                        parent = node.get_parent() # save child's parent
                        temp = parent.get_parent() # save the parent of this subtree

                        # change pointers between father and child
                        if clockWise:
                                parent.set_left(node.get_right()) 
                                node.get_right().set_parent(parent)
                                node.set_right(parent)
                                parent.set_parent(node)

                        else: # counter clockwise
                                parent.set_right(node.get_left())
                                node.get_left().set_parent(parent)
                                node.set_left(parent)
                                parent.set_parent(node)

                        # set pointers between the parent of the subtree with the his new child
                        node.set_parent(temp)

                        # if the father of the subtree exists and isn't None
                        if temp != None:
                                if node.is_inner_node_right_son():
                                        temp.set_right(node)
                                else:
                                        temp.set_left(node)

                        # else, update the root of the tree
                        else:
                                self.root = node
  
                        # adjusting heights
                        if isZigZag:
                                parent.set_height(parent.get_height()-1)
                                node.set_height(node.get_height()+1)

                        else: # straight rotation
                               parent.set_height(max(parent.get_left().get_height(),parent.get_right().get_height())+1)

                               ## if we need to update the height of node as well as parent
                               possibleNewHeight = max(node.get_left().get_height(), node.get_right().get_height())+1
                               if possibleNewHeight != node.get_height():
                                       node.set_height(possibleNewHeight)
                                       numOfActions += 1

        ###################################

                numOfActions = 0
                if balanceFactor == -2: # balance right subtree

                        # save right child and its BF
                        n1 = pivot.get_right()
                        n1BalanceFactor = n1.get_bf()
                        
                        #       p      =>    p          =>       n2
                        #        \     =>     \         =>      /  \
                        #         n1   =>      n2       =>     p   n1
                        #        /     =>        \      =>            
                        #       n2     =>         n1    =>                    
                        if n1BalanceFactor == 1: # right then left rotation on the child
                                n2 = n1.get_left()
                                rotation(node=n2, clockWise=True, isZigZag=True)
                                rotation(node=n2, clockWise=False, isZigZag=False)
                                numOfActions += 5 # 3 height updates and 2 rotations

                        
                        #       p           =>       n1         
                        #        \          =>      /  \         
                        #         n1        =>     p   n2               
                        #          \        =>                       
                        #           n2      =>                       
                        elif n1BalanceFactor == -1 or n1BalanceFactor == 0:
                                # perform left rotation
                                rotation(node=n1, clockWise=False, isZigZag=False)
                                numOfActions += 2 # updating height of pivot and performing 1 rotation

                        else:
                                raise Exception("Tried to deal with unbalanced right child " + str(n1.get_key()) + "with incorrect Bf")

                elif balanceFactor == 2: # balance left subtree

                        # save right child and its BF
                        n1 = pivot.get_left()
                        n1BalanceFactor = n1.get_bf()
                        
                        #        p      =>         p       =>       n2                  
                        #       /       =>        /        =>      /  \                 
                        #      n1       =>      n2         =>     n1   p                
                        #       \       =>     /           =>                           
                        #        n2     =>    n1           =>                         
                        if n1BalanceFactor == -1: # left then right rotation on the child
                                n2 = n1.get_right()
                                rotation(node=n2, clockWise=False, isZigZag=True)
                                rotation(node=n2, clockWise=True, isZigZag=False)
                                numOfActions += 5 # 3 height updates and 2 rotations

                        #         p       =>       n2                  
                        #        /        =>      /  \                 
                        #      n2         =>     n1   p                
                        #     /           =>                           
                        #    n1           =>                         
                        elif n1BalanceFactor == 1 or n1BalanceFactor == 0:
                                # perform right rotation
                                rotation(node=n1, clockWise=True, isZigZag=False)
                                numOfActions += 2 # updating height of pivot and performing 1 rotation
                        
                        else:
                                raise Exception("Tried to deal with unbalanced left child " + str(n1.get_key()) + "with incorrect Bf")
                        
                else:
                        raise Exception("Tried to correct BF with value >= 3 or <= 3: ",balanceFactor)

                return numOfActions

        
        """inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
        def insert(self, key, val):

                """
                Edge case - tree is empty
                Using our helper functions:
                        1. bst_tree_position - find the new node's designated father
                        2. bst_tree_insert - create the node, give it virtual children, and give it a father
                Now we move up along the tree until:
                        1. we have reached the root
                        2. we have no more need to balance our tree
                Lastly update size.
                """

                # RUNTIME:

                # edge case: tree is empty
                if self.tree_size == 0:
                        self.root = AVLNode(key, val)

                        # give it virtual children
                        self.root.set_left(virtualNode)
                        self.root.set_right(virtualNode)

                        # set height and update size
                        self.root.set_height(0)
                        self.tree_size += 1
                        return 0 # no rebalancing operations

                # initializing variables
                numOfRebalancing = 0
                currChild = self.bst_tree_insert(key, val)
                currParent = currChild.get_parent()

                # keep iterating until we reach the root 
                while currParent != None:

                        # saving current variables
                        balanceFactor = currParent.get_bf()
                        childHeight = currChild.get_height()
                        parentHeight = currParent.get_height()
                        
                        # adjust height if needed
                        if parentHeight == childHeight:
                                currParent.set_height(parentHeight+1) # updating correct height
                                numOfRebalancing += 1 # updating height is also a rebalancing operations
                        else:
                                break # height hasn't changed, hence insertion is complete
                        
                        if (balanceFactor >= 2) or (balanceFactor <= -2): # |BF| >= 2
                                numOfRebalancing += self.balance_sub_tree(currParent, balanceFactor)
    
                        # moving up the tree to the next possible problems
                        currChild = currParent
                        currParent = currParent.get_parent()

                self.tree_size += 1 # update tree size

                return numOfRebalancing              

        """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
        def delete(self, node):

                """
                First, take care of edgecases.
                Next, find the parent of the deleted node using the helper function:
                        1. bst_delete which implements logic of regular BST deletion
                Notice, if the deletion caused us to rebalance, we have height adjustments in the helper function:
                        2. balance_sub_tree
                Else, all height adjustments are max(leftson, rightson)+1, until we reach the root.
                """

		## RUNTIME:

		## edgecase: tree is empty or only a root
                if self.tree_size < 2:
                        self.root = None
                        return 0 # no rebalancing operations have been done
        
		## initializing variables
                numOfRebalancing = 0
                currParent = self.bst_delete(node)

                # keep iterating until we reach the root 
                while currParent != None:
                
                        # saving all heights needed for height adjustment
                        currParentH = currParent.get_height()
                        leftChildH = currParent.get_left().get_height()
                        rightChildH = currParent.get_right().get_height()
                                
                        # computing new height                                          
                        possibleNewHeight = (max(leftChildH, rightChildH)+1) # computing correct height after bst_delete
                        if currParentH != possibleNewHeight:
                                currParent.set_height(possibleNewHeight) # set new height
                                numOfRebalancing += 1 # updating height is also a rebalancing operations

                        # saving current variables
                        balanceFactor = currParent.get_bf()
                                
                        if balanceFactor == 2 or balanceFactor == -2: # |BF| == 2
                                numOfRebalancing += self.balance_sub_tree(currParent, balanceFactor)
                                
                                
                        # moving up the tree to the next possible problems
                        currParent = currParent.get_parent()

                self.tree_size -= 1 # update tree size

                return numOfRebalancing

                        
        """deletes node as usual in BST

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: AVLNode
        @returns: the father of the deleted node
        """
        def bst_delete(self, node):

                """
                Notice 4 types of cases:
                        1. we are wishing to delete the root or the tree is empty - 
                        both cases are taken care of in the delete function
                        2. node is a leaf - dettach from tree and put a virtual son instead
                        3. node has an only right\left child - connect between the child and the parent of deleted node.
                        4. node has 2 children - find the successor using a helper function, interchange between them and repeat
                        phase 1,2, or 3 on the successor since it has no left son, by design.
                """

                # RUNTIME:

                if node.is_virtual():
                        raise Exception("Tried to delete a virtual child")
                
                # initializing variables
                parent = node.get_parent()
                rightSon = node.get_right()
                leftSon = node.get_left()

		## if the node we wish to delete is a leaf just cut the link to it's father
                if node.is_leaf():
                           
                        if node.is_inner_node_right_son():
                                parent.set_right(virtualNode)
                                
                        else:
                                parent.set_left(virtualNode)

                # if the node we wish to delete has only a right son
                elif (leftSon.is_virtual()) and (rightSon.is_virtual() == False):

                        # if the node we wish to delete is the root
                        if self.root.get_key() == node.get_key():
                                self.root = rightSon
                                rightSon.set_parent(None)
                                
                        # if the node we wish to delete is a right son
                        elif node.is_inner_node_right_son():

                                # cut the middle man by extending pointers
                                parent.set_right(rightSon)
                                rightSon.set_parent(parent)

                        else: # symetric case for the other side
                                parent.set_left(rightSon)
                                rightSon.set_parent(parent)

                # if the node we wish to delete has only a left son
                elif (leftSon.is_virtual() == False) and (rightSon.is_virtual()):

                        # if the node we wish to delete is the root
                        if self.root.get_key() == node.get_key():
                                self.root = leftSon
                                leftSon.set_parent(None)
                        
                        # if the node we wish to delete is a right son
                        elif node.is_inner_node_right_son():

                                # cut the middle man by extending pointers
                                parent.set_right(leftSon)
                                leftSon.set_parent(parent)

                        else: # symetric case for the other side
                                parent.set_left(leftSon)
                                leftSon.set_parent(parent)

                else:

                        # if the node we wish to delete has 2 sons
                        nextNode = self.successor(node)

                        # Notice successor has no left son therefore we cannot enter endless recursion
                        self.bst_delete(nextNode)

                        # save left and right son again beacuse we have deleted a node
                        leftSon = node.get_left()
                        rightSon = node.get_right()

                        # change all pointers between the successor and the node we have wish to delete
                        nextNode.set_left(leftSon)
                        leftSon.set_parent(nextNode)
                        nextNode.set_right(rightSon)
                        rightSon.set_parent(nextNode)
                        nextNode.set_parent(parent)
                        nextNode.set_height(max(leftSon.get_height(),rightSon.get_height())+1)

                        # if node we wish to delete is the root it has no parent
                        if parent != None: 
                                if nextNode.is_inner_node_right_son():
                                        parent.set_right(nextNode)
                                else:
                                        parent.set_left(nextNode)

                        # we need to update root
                        else:
                                self.root = nextNode

                return parent

        """return the next node in order by sorting of keys

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: AVLNode
        @returns: the next node in order by key
        """
        def successor(self, node):

                """
                If the node has a right son, then go to it and look for the minimum of this subtree.
                Else, keeping rising up the tree to the left until you have the first turn right,
                your closet ancestor
                """

                # RUNTIME:
                
                if not node.get_right().is_virtual():
                        return self.minimum(node.get_right())
                else:
                        currParent = node.get_parent()
                        currNode = node
                        while (currParent != None) and (currNode.is_inner_node_right_son()):
                                currNode = currParent
                                currParent = currParent.get_parent()
                return currParent
                                

        """return the node with minimum key in the tree

        @type root: AVLNode
        @pre: node is the root of the tree
        @rtype: AVLNode
        @returns: node with the minimum key
        """
        def minimum(self, root):

                """
                Keep going left until we 'fall' off the tree
                """
                
                # RUNTIME:
                
                currNode = root
                while not currNode.get_left().is_virtual():
                        currNode = currNode.get_left()
                return currNode

        """returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
        def avl_to_array(self):

                """
                Create an empty list. Start with minimum node, and set counter to zero.
                Then as long as our counter < size of tree:
                        1. add current node to the list
                        2. call the next in line using successor helper function
                        3. increment counter
                """

		## RUNTIME:
		
                # init empty List
                sortedList = []
		
                # start with minimum node
                currNode = self.minimum(self.root)

		## init counter to count all until we reached all nodes
                cnt = 0

                while cnt < self.tree_size:

                        sortedList.append((currNode.get_key(), currNode.get_value()))
                        currNode = self.successor(currNode)
                        cnt += 1

                return sortedList


        """returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
        def size(self):
                return self.tree_size	

	
        """splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
        def split(self, node):

                """
                First denote all edge cases are taken care of in the code design without special acknowledgment:
                        1. if the node we recieved is the root, we won't enter the while loop beacause it's father
                        is None, and we will just call upon his children as roots. If one of them is virtual than we
                        return a tree with a virtual root which is acceptable as an empty tree
                        2. if we recieved a virtual node we return two empty trees
                Next, we iterate up the tree moving the child and parent pointers, and using the knoweldge,
                of whether our current node is a left or right son we join trees as needed by comparing keys.
                """

                # RUNTIME:

                # intializing variables
                leftTree = AVLTree()
                rightTree = AVLTree()
                returnList = [leftTree, rightTree]
                
                currParent = node.get_parent()
                currChild = node

                # use the current nodes sons as the current leftTree and rightTree roots
                # first make sure they aren't virtual
                if node.get_left().is_virtual():
                         leftTree.root = None
                else:
                        leftTree.root = node.get_left()

                if node.get_right().is_virtual():
                        rightTree.root = None
                else:
                        rightTree.root = node.get_right()

                # split into 2 cases while moving up to the root of the tree:
                #      1. if node is a right child than all his ancestors are smaller than him and belong in leftTree
                #      2. else, node is a left child and all his ancestors belong in rightTree                        
                while currParent != None:

                        # will be used as a temporary joining tree as we are moving towards the root
                        tempTree = AVLTree()

                        if currChild.is_inner_node_right_son():

                                # give tempTree a designated root
                                if currParent.get_left().is_virtual():
                                        tempTree.root = None
                                else:
                                        tempTree.root = currParent.get_left()
                                        tempTree.root.set_parent(None)

                                # dettach tempTree from tree
                                currParent.set_right(virtualNode)

                                # update height
                                currParent.set_height(currParent.get_left().get_height()+1)

                                # join the current subtrees into one using helper function
                                # notice actual_join returns integer which doesn't concern us during split
                                leftTree.actual_join(tempTree, currParent)

                        else: # currChild is inner left son

                                # give tempTree a designated root
                                if currParent.get_right().is_virtual():
                                        tempTree.root = None
                                else:
                                        tempTree.root = currParent.get_right()
                                        tempTree.root.set_parent(None)


                                # dettach tempTree from tree
                                currParent.set_left(virtualNode)

                                # update height
                                currParent.set_height(currParent.get_right().get_height()+1)

                                # join the current subtrees into one using helper function
                                # notice actual_join returns integer which doesn't concern us during split
                                rightTree.actual_join(tempTree, currParent)

                        # move up the tree by one level
                        currChild = currParent
                        currParent = currChild.get_parent()
                                 
                return returnList

	
        """joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
        def join(self, tree2, key, val):

                """
                Create the joinNode and call helper function: actual_join.
                This allows us to avoid duplicating code and using actual_join for the split function as well,
                which uses a join method using an existing node and doesn't create it given a key and a value.
                """

                # RUNTIME:

                # create the joinNode
                joinNode = AVLNode(key, val)
                joinNode.set_height(0)
                joinNode.set_left(virtualNode)
                joinNode.set_right(virtualNode)
                joinNode.set_not_virtual()
                
                return self.actual_join(tree2, joinNode)

        """joins self with joinNode and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type joinNode: AVLNode 
	@param joinNode: The node separting self with tree2
	@pre: all keys in self are smaller than joinNode.key and all keys in tree2 are larger than joinNode.key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
        def actual_join(self, tree2, joinNode):

                """
                First deal with edgecases - 1 of the trees is empty and balance tree if neccesary
                Next, check which has the larger keys, and who is the bigger one
                If the tree with bigger keys is larger:
                        1. go down to the left until you reach the height of the other tree's root
                        or until you reach the other tree's root +1 by design
                        2. connect both trees using the a new node with the key and value given as arguments
                If the tree with smaller keys is larger:
                        1. go down to the right until you reach the height of the other tree's root
                        or until you reach the other tree's root +1 by design
                        2. connect both trees using the a new node with the key and value given as arguments
                """

                # RUNTIME:

                # Save joint trees size
                self.tree_size += tree2.tree_size + 1

                ################################################
                
                # EDGECASES: 1 or both of the trees is empty ##

                if (self.root == None or self.root.is_virtual()) and tree2.root != None:

                        # return-height when one tree is none +1 is 2
                        returnHeight = tree2.root.get_height()+2

                        # connect tree2 to the skeleton of self
                        self.root = tree2.root

                        # join with an empty tree is same is inserting the joinNode to the none empty tree
                        self.insert(joinNode.get_key(),joinNode.get_value())


                        # # connect join node to tree2 on the skeleton of self
                        # self.root = joinNode

                        # # for balance purposes
                        # joinNode.set_height(tree2.root.get_height()+1)
                        
                        # # compare keys between joinNode and other tree
                        # if joinNode.get_key() < tree2.root.get_key():
                        #         joinNode.set_right(tree2.root)
                        # else:
                        #         joinNode.set_left(tree2.root)

                        # # balance tree
                        # balanceFactor = joinNode.get_bf()
                        # if balanceFactor >= 2 or balanceFactor <= -2:
                        #         self.balance_sub_tree(joinNode, balanceFactor)
                        
                        return returnHeight

                elif self.root != None and (tree2.root == None or tree2.root.is_virtual()):
                        
                        # return height when one tree is none +1 is 2
                        returnHeight = self.root.get_height()+2

                        self.insert(joinNode.get_key(),joinNode.get_value())

                        # # for balance purposes
                        # joinNode.set_height(self.root.get_height()+1)
                        
                        # # compare keys between joinNode and other tree
                        # if joinNode.get_key() < self.root.get_key():
                        #         joinNode.set_right(self.root)
                        # else:
                        #         joinNode.set_left(self.root)

                        # # update root
                        # self.root = joinNode

                        # ##balance tree
                        # balanceFactor = joinNode.get_bf()
                        # if balanceFactor >= 2 or balanceFactor <= -2:
                        #         self.balance_sub_tree(joinNode, balanceFactor)

                        return returnHeight

                elif (self.root == None or self.root.is_virtual()) and (tree2.root == None or self.root.is_virtual()):

                        # self is only a root
                        self.root = joinNode

                        return 1 # -1 -(-1) = 0

                ################################################

                # checking which tree has the larger keys
                if self.root.get_key() < tree2.root.get_key():
                        small_key_tree = self
                        big_key_tree = tree2
                else:
                        small_key_tree = tree2
                        big_key_tree = self


                # saving variables
                small_key_treeH = small_key_tree.root.get_height()
                big_key_treeH = big_key_tree.root.get_height()
                
                small_key_root = small_key_tree.root
                big_key_root = big_key_tree.root

                
                # 1st case: both trees are the same height or +1 height difference
                if small_key_treeH - big_key_treeH <= 1 and small_key_treeH - big_key_treeH >= -1:

                        # connect both roots by the joinNode
                        self.root = joinNode
                        joinNode.set_left(small_key_root)
                        joinNode.set_right(big_key_root)
                        joinNode.set_height(max(small_key_treeH,big_key_treeH)+1)

                        # connect the children to their new parent
                        small_key_root.set_parent(joinNode)
                        big_key_root.set_parent(joinNode)

                        if small_key_treeH - big_key_treeH == 0:
                                return 1
                        else:
                                return 2

                # 2nd case: big_key_tree is larger than the small_key_tree
                elif big_key_treeH - small_key_treeH >= 2:

                        # keep going down left in larger tree until:
                        #      1. we reached the height of smaller_key_tree's root
                        #      2. we can't keep going down left
                        #      Notice, in case 2 we will always have height difference +1 to the larger tree by design

                        currNode = big_key_root

                        # update joinNode height
                        joinNode.set_height(min(small_key_treeH,big_key_treeH)+1)

                        while currNode.get_height() != small_key_treeH and not currNode.get_left().is_virtual():

                                # save pointer
                                currNode = currNode.get_left()

                        # connect current node as right son of joinNode and small_key_root as left son
                        temp = currNode.get_parent()
                        temp.set_left(joinNode)

                        ##connect the dots
                        joinNode.set_parent(temp)
                        joinNode.set_left(small_key_root)
                        joinNode.set_right(currNode)
                        small_key_root.set_parent(joinNode)
                        currNode.set_parent(joinNode)

                        # update height
                        joinNode.set_height(max(small_key_treeH,currNode.get_height())+1)

                        ##update root
                        self.root = big_key_root

                        # balance tree and adjust heights

                        currParent = joinNode.get_parent()
                        
                        while currParent != None:
                                        
                                # balance
                                balanceFactor = currParent.get_bf()
                                if balanceFactor >= 2 or balanceFactor <= -2:
                                        self.balance_sub_tree(currParent, balanceFactor)

                                # adjust height
                                currParent.set_height(max(currParent.get_left().get_height(),currParent.get_right().get_height())+1)
                                currParent = currParent.get_parent()

                        return big_key_treeH - small_key_treeH + 1

                # 3rd case: small_key_tree is larger than the big_key_tree
                else:

                        # keep going down right in larger tree until:
                        #      1. we reached the height of bigger_key_tree's root
                        #      2. we can't keep going down right
                        #      Notice, in case 2 we will always have height difference +1 to the larger tree by design

                        currNode = small_key_root

                        # update joinNode height
                        joinNode.set_height(min(small_key_treeH,big_key_treeH)+1)

                        while currNode.get_height() != big_key_treeH and not currNode.get_right().is_virtual():
                                
                                # update height on the way down
                                # if currNode.get_bf <= 0:
                                #         currNode.set_height(currNode.get_height()+big_key_treeH)

                                # save pointer
                                currNode = currNode.get_right()

                        # connect current node as right son of joinNode and small_key_root as left son
                        temp = currNode.get_parent()
                        temp.set_right(joinNode)

                        ##connect the dots
                        joinNode.set_parent(temp)
                        joinNode.set_right(big_key_root)
                        joinNode.set_left(currNode)
                        big_key_root.set_parent(joinNode)
                        currNode.set_parent(joinNode)

                        # update height
                        joinNode.set_height(max(big_key_treeH,currNode.get_height())+1)

                        ##update root
                        self.root = small_key_root

                        # balance tree and adjust heights

                        currParent = joinNode.get_parent()

                        while currParent != None:

                                # balance
                                balanceFactor = currParent.get_bf()
                                if balanceFactor >= 2 or balanceFactor <= -2:
                                        self.balance_sub_tree(currParent, balanceFactor)

                                #adjust heights
                                currParent.set_height(max(currParent.get_left().get_height(),currParent.get_right().get_height())+1)
                                currParent = currParent.get_parent()

                        return small_key_treeH - big_key_treeH + 1


        """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
        def get_root(self):
                return self.root

        

