# test_blastrewards.py
"""
Tests for BlastRewards module.
"""

import unittest
from blastrewards import BlastRewards

class TestBlastRewards(unittest.TestCase):
    """Test cases for BlastRewards class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlastRewards()
        self.assertIsInstance(instance, BlastRewards)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlastRewards()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
