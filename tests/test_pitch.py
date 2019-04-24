import unittest
from app.models import Pitch, User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Chiri = User(username = 'Chiri',password = '1234', email = 'chiri@gmail.com')
        self.new_pitch = Pitch(pitch_category = 13452, pitch ='I’m not a photographer, but I can picture me and you together.', user = self.user_Shiko)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.category.id,13452)
        self.assertEquals(self.new_pitch.pitch,'Review for movies')
        self.assertEquals(self.new_pitch.user,self.user_Shiko)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
    
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(13452)
        self.assertTrue(len(got_pitches) == 1)
