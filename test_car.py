import unittest
from car import Car
from battery import Battery
from engine import Engine

class TestCar(unittest.TestCase):
    def setUp(self):
        engine = Engine("V8")
        battery = Battery("Lithium-ion")
        self.car = Car("Model XYZ", engine, battery)

    def test_getModel(self):
        self.assertEqual(self.car.getModel(), "Model XYZ")

    def test_getEngine(self):
        self.assertIsInstance(self.car.getEngine(), Engine)
        self.assertEqual(self.car.getEngine().getType(), "V8")

    def test_getBattery(self):
        self.assertIsInstance(self.car.getBattery(), Battery)
        self.assertEqual(self.car.getBattery().getType(), "Lithium-ion")

if __name__ == '__main__':
    unittest.main()
