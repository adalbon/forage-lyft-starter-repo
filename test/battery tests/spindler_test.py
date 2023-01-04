import unittest
from datetime import date
from battery.spindler import Spindler


class TestBattery(unittest.TestCase):
    def needs_service_true(self):
        current_date = date.fromisoformat("2023-01-04")
        last_service_date = date.fromisoformat("2019-01-04")
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def needs_service_false(self):
        current_date = date.fromisoformat("2023-01-04")
        last_service_date = date.fromisoformat("2021-01-04")
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
