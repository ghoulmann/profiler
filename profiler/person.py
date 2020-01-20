from profiler.profile import Profile
from profiler.device import Device
from random import randint
class Person(Profile):
    def __init__(self):
        Profile.__init__(self)
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.name = self.first_name + " " + self.last_name
        self.address = self.fake.address()
        self.ssn = self.fake.ssn()
        self.zip = self.address[:5]
        self.street = self.getLocation("street")
        self.state = self.getLocation("state")
        self.city = self.getLocation("city")
        self.phone = self.fake.phone_number()
        self.position = self.fake.job()
        self.employer = self.fake.company() + ", " + self.fake.company_suffix()
        #self.device = Device(self)
        self.devices = randint(0, 3)
        self.inventory = {}
        for i in range(self.devices):
            self.inventory['device' + str(i)] = Device(self)
        del(self.fake)
    def getLocation(self, part):
        split_address = self.address[:-6].split("\n")
        if part == "street":
            return split_address[0]
        elif part == "citystate":
            return split_address[1]
        elif part == "state":
            citystate = split_address[1].split(', ')
            return citystate[1]
        elif part == "city":
            citystate = split_address[1].split(',')
            return citystate[0]
        else:
            pass
    def __str__(self):

        #print(self.__dict__)
        for k,v in self.__dict__.items():
            print(k, v, sep=": ")
        for k, v in self.inventory.items():
            print(k.upper())
            print("\t" + v.hostname)
            print("\t" + v.ipv4)
            if v.wireless_device == True:
                print("\t" + v.ssid)
            print("\t" + v.user_name)
            print("\t" + v.password)
