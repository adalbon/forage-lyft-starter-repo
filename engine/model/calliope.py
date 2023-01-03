from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler import Spindler


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = Spindler(last_service_date)

        super().__init__(calliope_engine, calliope_battery)

        self.engine = calliope_engine
        self.battery = calliope_battery

    def needs_service(self):
        return super().needs_service()
