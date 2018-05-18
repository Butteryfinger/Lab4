# Lab 5

# Code's done
# Check time comp
# Generator iteration

class Node:
    def __init__(self, key, val):
        self._key = key
        self._val = val
        self._left = None
        self._right = None

    def set_children(self, l, r):
        self._left = l
        self._right = r

    def data(self):
        return self._key, self._val

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def leftmost(self, v):
        left = v.left_child()
        if left == None:
            return v
        else:
            return self.leftmost(left)
    

    def insert(self, key, val): # O(h) h = längsta gren
        '''
        Public interface method to insert a key and value to the search tree.
        '''
        self.root = self.__insert(self.root, key, val)

    def __insert(self, v, key, val):
        '''
        Internal method to recursively decide where to insert a new node.
        Warning! This method has a bug, it does not behave according to specification!
        '''
        if v != None:
            v_key, x = v.data() # Ignoring x actually
            left = v.left_child()
            right = v.right_child()
            if key == v_key:
                v._val = val
            elif key < v_key:
                left = self.__insert(left, key, val)
            else:
                right = self.__insert(right, key, val)
            v.set_children(left, right)
            return v
        else:
            return Node(key, val)


    def find(self, key): # O(h)
        return self._find(self.root, key)
        

    def _find(self, v, key):
        cur_key, cur_val = v.data()
        left = v.left_child()
        right = v.right_child()
        if cur_key == key:
            return cur_val
        elif key < cur_key:
            if left == None:
                  raise KeyError("Key not present in tree")
            return self._find(left, key)
        else:
            if right == None:
                  raise KeyError("Key not present in tree")
            return self._find(right, key)
	

    def remove(self, key): # O(h) antingen en löv eller fortsätter från den löven neråt för ersättning tills den når slutet
        if self.root == None:
            print("Tree's empty")
        self._remove(self.root, key, None, None)
        

    """
    förklaring:
    Löv, tas bort enkelt
    Löv en barn ersätts direkt av dess enda barn
    Löv med 2 barn mest vänstra grenen av sitt högra barn sådan man
    kan hålla värdet så nära den som tas bort
    """

    def _remove(self, v, key, parent, direction):
        cur_key, o = v.data()
        left = v.left_child()
        right = v.right_child()
        if cur_key == key:
            # fall för löv ersättning
            if right != None:
                nrep_key = self.leftmost(right)
                nkey, nval = nrep_key.data()
                if parent == None:
                    self._remove(self.root, nkey, None, None)
                else:
                    self._remove(parent, nkey, v, "Right")
                v._key = nkey
                v._val = nval 
            elif left != None:
                parent.set_children(left, None) # Bugfixed
            else:
            # fall för ensam löv
                if parent == None:
                    self.root = None
                elif direction == "Right":
                    parent._right = None
                else:
                    parent._left = None
        elif cur_key < key:
            if right == None:
                raise KeyError("Key not present in tree")
            self._remove(right, key, v, "Right")
        else:
            if left == None:
                raise KeyError("Key not present in tree")
            self._remove(left, key, v, "Left")
       
       

    def size(self): # O(totala antal inputs) 
        return self.__size(self.root)
        

    def __size(self, v):
        left = v.left_child()
        right = v.right_child()
        if left != None:
            if right != None:
                return 1 + self.__size(left) + self.__size(right)
            return 1 + self.__size(left)
        if right != None:
            return 1 + self.__size(right)
        else:
            return 1

    def __iter__(self):
        return self.Gen(self.root)

    def Gen(self, v):
        if v:
            yield from self.Gen(v.left_child())
            yield v._key, v._val
            yield from self.Gen(v.right_child())


    def __str__(self):
        return str(self.root)

    def __getitem__(self, key):
        return self._find(self.root, key)

    def __setitem__(self, key, val):
        self.root = self.__insert(self.root, key, val)

"""
	O <-
       / \
      O   O <-
     /   / \   
    O   O   O

"""
        
def main():
    credits = BinarySearchTree()
    credits.insert('DA3001', 7.5)
    credits.insert('DA2004', 5)
    credits.insert('DA2003', 10)
    credits.insert('DA2004', 10) # Replacement check
    credits.insert('DA3020', 6)
    credits.insert('DA3015', 6)
    credits["DA1030"] = 20
    credits["DA1025"] = 12
    credits["DA1018"] = 12
    credits["DA1014"] = 12
    credits["DA1016"] = 12
    credits["DA1017"] = 12
    n = credits.size()          # size check
    print(n, "size check")
    hp = credits.find('DA2004') # find check
    print(hp, "find check")

    for course, hp in credits: # Iteration check
        print(course, hp)

    credits.remove('DA1014') # removal check
    m = credits.size()          # size check + removal

    print(m)

    for course, hp in credits: # Iteration check
        print(course, hp)

    credits.remove("DA3001") # Root removal
    print("")
    for course, hp in credits: # Iteration check
        print(course, hp)

if __name__ == '__main__':
    main()    
