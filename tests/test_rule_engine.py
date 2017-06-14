import unittest
from rule_engine import load_rules

class TestRuleEngine(unittest.TestCase):

    def test_load_rules(self):
        rules = load_rules('rules.json')
        self.assertEqual(type(rules), dict)

if __name__ == '__main__':
    unittest.main()
