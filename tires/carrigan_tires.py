from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)
    
    def needs_service(self):
        return max(self.tire_wear) >= 0.9
