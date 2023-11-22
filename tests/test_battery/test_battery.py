
import unittest
from abc import ABCMeta, abstractmethod
from battery import Battery


class TestBattery(unittest.TestCase):
    def test_needs_service_abstract_method(self):
        """Concrete subclass implementing the needs_service method"""
        class ConcreteBattery(Battery, metaclass=ABCMeta):
            @abstractmethod
            def needs_service(self):
                pass

        with self.assertRaises(TypeError):
            ConcreteBattery()

        """Subclass that provides a concrete implementation"""
        class ImplementedBattery(ConcreteBattery):
            def needs_service(self):
                return False

        implemented_battery = ImplementedBattery()
        result = implemented_battery.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
