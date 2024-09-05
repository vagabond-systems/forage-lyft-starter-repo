import unittest
from engine import Engine
from battery import Battery

class TestEngine(unittest.TestCase):
    def setUp(self):
        # Create an instance of Engine to be used in tests
        self.engine = Engine()

    def test_engine_start(self):
        self.engine.start()
        self.assertTrue(self.engine.is_running, "Engine should be running after start")

    def test_engine_stop(self):
        self.engine.stop()
        self.assertFalse(self.engine.is_running, "Engine should not be running after stop")

class TestBattery(unittest.TestCase):
    def setUp(self):
        # Create an instance of Battery to be used in tests
        self.battery = Battery()

    def test_battery_charge(self):
        self.battery.charge()
        self.assertGreater(self.battery.charge_level, 0, "Battery charge level should be greater than 0 after charging")

    def test_battery_discharge(self):
        self.battery.discharge()
        self.assertLess(self.battery.charge_level, 100, "Battery charge level should be less than 100 after discharging")

if __name__ == '__main__':
    unittest.main()
