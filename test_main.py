import unittest
from functools import partial

from main import deep_merge


class TestDeepMerge(unittest.TestCase):
    def test_simple_obj_with_uniq_keys(self):
        self.assertEqual(
            {'a': 1, 'b': 2},
            deep_merge({'a': 1}, {'b': 2}),
        )
        self.assertEqual(
            {'a': 1, 'b': 1},
            deep_merge({'a': 1}, {'b': 1}),
        )

    def test_simple_obj_without_uniq_keys(self):
        self.assertEqual(
            {'a': 2},
            deep_merge({'a': 1}, {'a': 2}),
        )
        self.assertEqual(
            {'a': [1, 2]},
            deep_merge({'a': [1]}, {'a': [2]}),
        )
        self.assertEqual(
            {'a': [1, 2]},
            deep_merge({'a': [1]}, {'a': 2}),
        )
        self.assertEqual(
            {'a': [1, 2]},
            deep_merge({'a': 1}, {'a': [2]}),
        )

    def test_nested_obj(self):
        self.assertEqual(
            {'a': {'b': 2}},
            deep_merge({'a': {'b': 1}}, {'a': {'b': 2}}),
            'Nested objects'
        )
        self.assertEqual(
            {'a': {'b': [1, 2]}},
            deep_merge({'a': {'b': [1]}}, {'a': {'b': 2}}),
            'Nested objects'
        )
        self.assertEqual(
            {'a': {'b': [1, 2]}},
            deep_merge({'a': {'b': [1]}}, {'a': {'b': [2]}}),
            'Nested objects'
        )
        self.assertEqual(
            {'a': {'b': [1, 2]}},
            deep_merge({'a': {'b': 1}}, {'a': {'b': [2]}}),
            'Nested objects'
        )


if __name__ == '__main__':
    unittest.main()
