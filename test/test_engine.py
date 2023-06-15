import unittest
from forage.engine import Engine
class TestEngine(unittest.TestCase):
    def test_getType(self):
        engine = Engine("V8")
        self.assertEqual(engine.getType(), "V8")

    def test_needsService(self):
        engine = Engine("V8")
        self.assertFalse(engine.needsService(5000))
        self.assertTrue(engine.needsService(100000))
