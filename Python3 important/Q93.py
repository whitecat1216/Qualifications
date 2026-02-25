# 【問題９３】

import unittest
from unittest.mock import MagicMock

class TestMockExample(unittest.TestCase):
    def test_call_count(self):
        mock_function=MagicMock()
        mock_function()
        mock_function()
        self.assertEqual(mock_function.call_count,2)
if __name__=="__main__":    unittest.main()

    # ②テストが成功する