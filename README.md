AVL Tree implementation in python using two classes:
#Assume n = number of nodes

  AVLNode:
    methods (all at O(1)):
      1. init
      2. getters: left and right sons, parent, key, value, height and balance factor
      3. setters: left and right sons, parent, key, value, height, virtual_node and not_virtual
      4. is_virtual()
      5. is_leaf()
      
  AVLTree:
    Methods:
      1. init O(1)
      2. search(key) O(logn)
      3. insert(key, val) O(logn)
      4. delete(node) O(logn)
      5. successor(node) O(logn)
      6. minimum(root) O(logn)
      7. tree_to_array() O(n)
      8. split(node) O(logn)
      9. join(key,val) O(logn)
