import unittest
from main import *
class TestGenBinTree(unittest.TestCase):

    def test_tree_height_0(self):
        """Тест для дерева высотой 0"""
        result = gen_bin_tree(0, 7)
        tree = {7: []}
        self.assertEqual(result, tree)

    def test_tree_height_1(self):
        """Тест для дерева высотой 1"""
        result = gen_bin_tree(1, 7)
        tree = {7: [{21: []}, {3: []}]}
        self.assertEqual(result, tree)

    def test_tree_height_2(self):
        """Тест для дерева высотой 2"""
        result = gen_bin_tree(2, 7)
        tree = {7: [{21: [{63: []}, {17: []}]}, {3: [{9: []}, {-1: []}]}]}
        self.assertEqual(result, tree)

    def test_tree_height_3(self):
        """Тест для дерева высотой 3"""
        result = gen_bin_tree(3, 7)
        tree = {7: [{21: [{63: [{189: []}, {59: []}]}, {17: [{51: []}, {13: []}]}]}, {3: [{9: [{27: []}, {5: []}]}, {-1: [{-3: []}, {-5: []}]}]}]}
        self.assertEqual(result, tree)

    def test_tree_height_4(self):
        """Тест для дерева высотой 4"""
        result = gen_bin_tree(4, 7)
        tree = {7: [{21: [{63: [{189: [{567: []}, {185: []}]}, {59: [{177: []}, {55: []}]}]}, {17: [{51: [{153: []}, {47: []}]}, {13: [{39: []}, {9: []}]}]}]}, {3: [{9: [{27: [{81: []}, {23: []}]}, {5: [{15: []}, {1: []}]}]}, {-1: [{-3: [{-9: []}, {-7: []}]}, {-5: [{-15: []}, {-9: []}]}]}]}]}
        self.assertEqual(result, tree)

if __name__ == '__main__':

    unittest.main()