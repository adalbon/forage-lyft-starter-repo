import unittest
from datetime import date
from battery.nubbin import Nubbin

class TestNubbin(unittest.TestCase):
    def needs_service_true(self):
        current_date = date.fromisoformat("2023-01-04")
        last_service_date = date.fromisoformat("2018-01-04")
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def needs_service_false(self):
        current_date = date.fromisoformat("2023-01-04")
        last_service_date = date.fromisoformat("2022-01-04")
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())