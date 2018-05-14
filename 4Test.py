import unittest
import binarysearchtree as b

# Fråga om vad bugen ska göra

class TestTree(unittest.TestCase):

    def testcreatetree(self):
        Tree = b.BinarySearchTree()
        self.assertIsInstance(Tree, b.BinarySearchTree)
    
    def testinserttree(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        self.assertIsInstance(Tree, b.BinarySearchTree)
        self.assertEqual(Tree.find("DA3018"), 7.5)

    def testchildren(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        Tree["DA2004"] = 5
        Tree["DA3020"] = 6
        self.assertIsNotNone(Tree["DA2004"])
        self.assertIsNotNone(Tree["DA2004"])

    def testsize(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        Tree["DA2004"] = 5
        Tree["DA3020"] = 6
        self.assertEqual(Tree.size(), 3)

    def testGenerator(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        Tree["DA2004"] = 5
        Tree["DA3020"] = 6
        fill = []
        for a, c in Tree:
            fill.append(a)
        self.assertEqual(fill[0], "DA2004")
        self.assertEqual(fill[1], "DA3018")
        self.assertEqual(fill[2], "DA3020")

    def testremove(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        Tree["DA2004"] = 5
        Tree["DA3020"] = 6
        Tree["DA3019"] = 6
        Tree.remove("DA3019")
        self.assertEqual(Tree.size(), 3)

    def testremoveroot(self):
        Tree = b.BinarySearchTree()
        Tree.insert('DA3018', 7.5)
        Tree["DA2004"] = 5
        Tree["DA3020"] = 6
        Tree["DA3019"] = 6
        Tree.remove("DA3018")
        self.assertEqual(Tree.size(), 3)

    #def Bug(self):

"""
"""

if __name__ == "__main__":
    unittest.main()
