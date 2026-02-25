import unittest

class TestListOperations(unittest.TestCase):
    def test_list_operations(self):
        lst=[1, 2, 3]
        lst.append(8)
        self.assertListEqual(lst, [1, 2, 3, 8])
if __name__=="__main__":
    unittest.main()
    # ②テストが成功する