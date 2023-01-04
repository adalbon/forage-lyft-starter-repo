import unittest
from engine.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def needs_service_true(self):
        current_mileage = 45000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def needs_service_false(self):
        current_mileage = 20000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
