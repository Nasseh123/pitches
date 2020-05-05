import unittest

from app.modules import Pitch



class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Category class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Pitch=Pitch(1,"THE PITCH","Author Name")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Pitch,Pitch))

    def test_init(self):
        """
          test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_Pitch.id,1)
        self.assertEqual(self.new_Pitch.pitch,"THE PITCH")
        self.assertEqual(self.new_Pitch.author,"Author Name")

