import unittest
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire

class test_OctoprimeTire(unittest.TestCase):
    def test_CarriganTire_should_be_serviced(self):
        tires_array = (0.65, 0.7, 0.85, 0.8)
        tire = OctoprimeTire(tires_array)
        self.assertTrue(tire.needs_service())

    def test_CarriganTire_should_not_be_serviced(self):
        tires_array = (0.6, 0.7, 0.85, 0.8)
        tire = OctoprimeTire(tires_array)
        self.assertFalse(tire.needs_service())


class test_CarriganTire(unittest.TestCase):
    def test_CarriganTire_should_be_serviced(self):
        tires_array = (0.4, 0.8, 0.95, 0.1)
        tire = CarriganTire(tires_array)
        self.assertTrue(tire.needs_service())

    def test_CarriganTire_should_not_be_serviced(self):
        tires_array = (0.4, 0.7, 0.85, 0.1)
        tire = CarriganTire(tires_array)
        self.assertFalse(tire.needs_service())




if __name__ == '__main__':
    unittest.main()
