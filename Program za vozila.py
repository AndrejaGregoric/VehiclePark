


def input_is_float(value):
    """ Simple check if input is float. """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Vehicle:
    def __init__(self, brand, model, driven_km, last_servis):
        self.brand = brand
        self.model = model
        self.driven_km = driven_km
        self.last_servis = last_servis

    def edit_driven_km(self):
        km = raw_input('New value for km: ')
        if input_is_float(value=km):
            self.driven_km = km
        else:
            print 'Value insterted is not valid.'

    def edit_service_date(self):
        edit_t = raw_input('Write new date (dd.mm.yyyy): ')
        self.last_servis = edit_t


class VehiclePark:
    def __init__(self):
        self.lst = []

    def add_vehicle(self):
        b = raw_input('Write vehicle brand: ')
        m = raw_input('Write vehicle model: ')
        km = raw_input('Write amount of kilometers that vehicle has done: ')
        ls = raw_input('Write date of the last service (dd.mm.yyyy): ')
        v = Vehicle(brand=b, model=m, driven_km=km, last_servis=ls)
        self.lst.append(v)

    def del_vehicle(self):
        select = raw_input('Which vehicle would you like to delete (write index): ')
        # check if really integer
        del(self.lst[int(select)-1])

    def print_park(self):
        for index, vehicle in enumerate(self.lst):
            print "{}) {}, {}. {} km driven so far. Last service date: {}".format(index+1, vehicle.brand, vehicle.model, vehicle.driven_km, vehicle.last_servis)
        if not self.lst:
            print "No vehicles in park yet."


# Ask user what would he like to do with database

def main():
    print "Welcome to the Vehicle Manager program."

    vp = VehiclePark()

    while True:
        print ""  # empty line
        print "Please pick one of the following options:"
        print "1) See a list of all the company vehicles."
        print "2) Add new vehicle."
        print "3) Edit the kilometers done for the chosen vehicle."
        print "4) Edit the last service date for the chosen vehicle."
        print '5) Delete vehicle.'
        print "6) Quit the program."
        print ""

        choice = raw_input("Which option would you like to choose? (1, 2, 3, 4, 5, 6) ")
        print "your choice: {} {}".format(choice, type(choice))

        if choice == "1":
            vp.print_park()
        elif choice == "2":
            vp.add_vehicle()
        elif choice == "3":
            vp.print_park()
            index = raw_input('Which vehicle would you like to edit(write index): ')
            vhc = vp.lst[int(index)-1]
            vhc.edit_driven_km()
        elif choice == "4":
            vp.print_park()
            index = raw_input('Which vehicle would you like to edit(write index): ')
            vhc = vp.lst[int(index)-1]
            vhc.edit_service_date()
        elif choice == "5":
            vp.del_vehicle()
        elif choice == "6":
            print "Thank you for using the Vehicle Manager. Have a nice day!"
            # TODO: save_to_disk(vehicles) !!!!
            break
        else:
            print "I'm sorry, but I didn't understand your choice. Please type in just a letter, either 1, 2, 3, " \
                  "5 (in progress) or 6. "

    with open("vehicles.csv", "w+") as v_file:
        for vhc in vp.lst:
            v_file.write(vhc.brand + ',' + vhc.model + '\n')


if __name__ == "__main__":
    main()
