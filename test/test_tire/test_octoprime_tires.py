import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensors = [1,1,1,1]
        tire = OctoprimeTires(sensors=sensors)
        self.assertTrue(tire.need_service())
        #assert battery
        
    def test_tires_should_not_be_serviced(self):
        sensors = [0,0,0,0.5]
        tire = OctoprimeTires(sensors=sensors)
        self.assertFalse(tire.need_service())
        #assert battert
        