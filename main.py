class Captains():

    def __init__(self, name, content_golem):
            self.name = name
            self.content_golem = content_golem

    def __str__(self):
        return str(self.name) or str(self.content_golem)


    def IsContentGolem(self, name):
        if name.content_golem >= 30000:
            return True










