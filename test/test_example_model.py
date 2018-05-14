import unittest
from app import example

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
