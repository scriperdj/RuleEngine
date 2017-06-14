import unittest
from rule_engine import get_string

class TestRuleEngine(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(get_string(), 'ok')

if __name__ == '__main__':
    unittest.main()
