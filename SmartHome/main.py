from abc import ABC, abstractmethod

class Controllable(ABC):
#All devices that inherit this class have to define the turn_on(), turn_off() and get_status() functions
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
    
class Appliance(Controllable):
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} turned on.")
        else:
            print(f"{self.name} already turn on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} turned of")
        else:
            print(f"{self.name} already turn off.")

    def get_status(self):
        return f"{self.name} {'turn on' if self.is_on else 'turn off'}"
    
class Light(Appliance):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name}'s level of brightness set like that {self.brightness}")
        else:
            print("level of brightness have to be between 0-100!")

    def get_brightness(self):
        return f"{self.name} brightness: {self.brightness}"

class Thermostat(Appliance):
    def __init__(self, name, temperature=20):
    #default temperature is 20
        super().__init__(name)
        self.temperature = temperature 

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"{self.name} is set as {self.temperature}")

    def get_temperature(self):
        return f"{self.name} temperature: {self.temperature}°C"
    
class SecuritySystem(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.alarm_activated = False 
        self.camera_on = False

    def activate_alarm(self):
        if not self.alarm_activated:
            self.alarm_activated = True
            print(f"{self.name} alarm is activated")
        else:
            print(f"{self.name} alarm is already active.")

    def deactivate_alarm(self):
        if self.alarm_activated:
            self.alarm_activated = False
            print(f"{self.name} alarm is disabled.")
        else:
            print(f"{self.name} alarm is already disable.")

    def turn_on_camera(self):
        if not self.camera_on:
            self.camera_on = True
            print(f"{self.name} cam is turn on")
        else:
            print(f"{self.name} it is already turn on.")

    def turn_off_camera(self):
        if self.camera_on:
            self.camera_on = False
            print(f"{self.name} cam is turn off")
        else:
            print(f"{self.name} cam is already turn off.")
            
def main():
    # Example Devices
    light = Light("Lamp of the living room")
    thermostat = Thermostat("Thermostat of bedroom")
    security_system = SecuritySystem("Home Security System")

    devices = [light, thermostat, security_system]

    while True:
        print("\n--- Smart Home Device Management System ---")
        print("1. List Devices")
        print("2. Turn on the device")
        print("3. Turn off the device")
        print("4. Query Device Status")
        print("5. Make Special Settings of the Device")
        print("6. Exit")
        
        choice = input("Select an options: ")

        if choice == "1":
            print("\n--- Devices ---")
            for idx, device in enumerate(devices, start=1):
                print(f"{idx}. {device.name}")
        
        elif choice == "2":
            device_num = int(input("Enter the num of the device which do you want to turn on: ")) - 1
            devices[device_num].turn_on()

        elif choice == "3":
            device_num = int(input("Enter the num of the device which do you want to turn off: ")) - 1
            devices[device_num].turn_off()

        elif choice == "4":
            device_num = int(input("Enter the num of the device which status you want to query: ")) - 1
            print(devices[device_num].get_status())

        elif choice == "5":
            device_num = int(input("Enter the device num which do you want to set: ")) - 1
            device = devices[device_num]

            if isinstance(device, Light):
                brightness = int(input("Enter a new brightness level: "))
                device.set_brightness(brightness)

            elif isinstance(device, Thermostat):
                temperature = int(input("Enter a new temperature: "))
                device.set_temperature(temperature)

            elif isinstance(device, SecuritySystem):
                print("1. turn on the alarm")
                print("2. turn off the alarm")
                print("3. turn on the cam")
                print("4. turn off the cam")
                security_choice = input("select an options: ")

                if security_choice == "1":
                    device.activate_alarm()
                elif security_choice == "2":
                    device.deactivate_alarm()
                elif security_choice == "3":
                    device.turn_on_camera()
                elif security_choice == "4":
                    device.turn_off_camera()

        elif choice == "6":
            print("Exiting!")
            break

        else:
            print("Invalid selection, please try again!")

if __name__ == "__main__":
    main()