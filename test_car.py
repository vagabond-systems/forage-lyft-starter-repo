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

      def test_spindlerBatteryServiceAfterThreeYears(self):
        engine = Engine("V8")
        battery = Spindler("Lithium-ion")
        car = Car("Model XYZ", engine, battery)

        current_year = datetime.now().year
        future_year = current_year + 3
        car.advanceTime(future_year)  # Advances time by three years

        self.assertTrue(car.getBattery().needsService())
if __name__ == '__main__':
    unittest.main()
