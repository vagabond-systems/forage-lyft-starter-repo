import unittest
from car import Car
from battery import Battery
from engine import Engine

class TestCar(unittest.TestCase):
    def setUp(self):
        engine = Engine("V8")
        battery = Battery("Lithium-ion")
        self.car = Car("Model XYZ", engine, battery)
    
    def test_carriganTireServiceWhenWorn(self):
        engine = Engine("V8")
        battery = Battery("Lithium-ion")
        car = Car("Model XYZ", engine, battery)

        tireWear = [0.8, 0.7, 0.95, 0.6]  # Example tire wear array for Carrigan tires
        car.setTireWear(tireWear, "Carrigan")

        self.assertTrue(car.needsTireService())
   
    def test_octoprimeTireServiceWhenWorn(self):
        engine = Engine("V8")
        battery = Battery("Lithium-ion")
        car = Car("Model XYZ", engine, battery)

        tireWear = [0.5, 0.8, 0.6, 1.2]  # Example tire wear array for Octoprime tires
        car.setTireWear(tireWear, "Octoprime")

        self.assertTrue(car.needsTireService())

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
