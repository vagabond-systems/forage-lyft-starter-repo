class TestBattery(unittest.TestCase):
    def test_getType(self):
        battery = Battery("Lithium-ion")
        self.assertEqual(battery.getType(), "Lithium-ion")

    def test_needsService(self):
        battery = Battery("Lithium-ion")
        self.assertFalse(battery.needsService(2))
        self.assertTrue(battery.needsService(5))
 if __name__ == '__main__':
    unittest.main()
