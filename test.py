# test.py
# Run tests

import unittest
import example

class TestData(unittest.TestCase):
    '''Tests to validate data quality'''
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

class TestModel(unittest.TestCase):
    '''Tests to validate model results'''
    def setUp(self):
        """Get some fake data to run models on
        """
        self.dataset = example.fakedataset()

    def test_delivery_status_model_results(self):
        """Test whether scores are within an expected list of values"""
        delivery_status_scores = self.dataset['delivery_status'].apply(example.fake_delivery_status_model)
        valid_scores = [-1, 0, 1, 2]
        valid_score_count = sum([s in valid_scores for s in delivery_status_scores])
        is_delivery_status_model_valid = valid_score_count == len(self.dataset)
        self.assertTrue(is_delivery_status_model_valid)
