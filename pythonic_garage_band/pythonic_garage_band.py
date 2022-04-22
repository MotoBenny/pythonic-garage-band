

class Band:
    instances = []

    def __init__(self, name, members):  # this is for the band name
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return tuple(solos)

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:

    def __init__(self, name="Unknown", instrument="Unknown", solo="N/A"):
        self.name = name
        self.instrument = instrument
        self.solo = solo


class Guitarist(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

    def get_instrument(self):
        return self.instrument


class Bassist(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"

    def get_instrument(self):
        return self.instrument


class Drummer(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "rattle boom crash"

    def get_instrument(self):
        return self.instrument


Joan = Guitarist("Joan Jett")
print(Joan.__str__())
