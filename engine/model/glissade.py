from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler import Spindler


class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, ):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = Spindler(last_service_date)

        super().__init__(glissade_engine, glissade_battery)

        self.engine = glissade_engine
        self.battery = glissade_battery

    def needs_service(self):
        return super().needs_service()
