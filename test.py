# test.py
# Run tests

import unittest
import example

class TestData(unittest.TestCase):
    '''Validate data'''
    def setUp(self):
        """Get some fake data
        """
        self.dataset = example.fakedataset()
        self.numrows = len(self.dataset)

    def test_number_of_rows(self):
        """Test whether the dataset contains an expected number of rows"""
        self.assertGreaterEqual(self.numrows, 100)

    def test_delivery_status(self):
        """Test whether a column contains an expected number of unique values"""
        expected_number_of_values = 3
        self.assertEqual(len(self.dataset.delivery_status.unique()), expected_number_of_values)

    def test_created_in_delivery_status(self):
        """Test whether a column contains an expected value"""
        self.assertTrue('created' in self.dataset.final_delivery_status.unique())
