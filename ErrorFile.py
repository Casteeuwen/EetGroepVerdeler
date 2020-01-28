
class MoreHousesThanPeopleError(BaseException):
    def __init__(self,amteating,amthouses):
        self.message = "YOU HAVE MORE HOUSES THAN EATERS"
    def __str__(self):
        return self.message