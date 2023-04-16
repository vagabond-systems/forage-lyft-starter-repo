import unittest

from tire.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensors = [1,1,0,0]
        tire = CarriganTires(sensors=sensors)
        self.assertTrue(tire.need_service())


    def test_tires_should_not_be_serviced(self):
        sensors = [0,0,0,0.5]
        tire = CarriganTires(sensors=sensors)
        self.assertFalse(tire.need_service())