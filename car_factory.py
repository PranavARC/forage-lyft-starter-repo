from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(tire_wear))
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTires(tire_wear))

    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTires(tire_wear))

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(tire_wear))

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), CarriganTires(tire_wear))
