import random
from server.models import Vehicle

class ToggleVehicleStatus:
    vehicles = random.sample(population=list(Vehicle.objects.all()), k=3)

    for vehicle in vehicles:
        vehicle.toggle_status()