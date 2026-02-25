#[問題92]
import unittest

from unittest.mock import MagicMock

class TestMockExample(unittest.TestCase):
    def test_mock(self):
        mock_function=MagicMock(return_value=62)
        result=mock_function()
        self.assertEqual(result,62)
if __name__=="__main__":
    unittest.main()

    # ②テストが成功する