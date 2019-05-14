import sys


class Contact:

    def __init__(self,id = None, firstname = None, lastname = None, company = None, address = None, home = None, mobile_phone = None, work_phone = None, email = None):
        self.id=id
        self.firstname=firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email

    def __repr__(self):
        return "Contact: %s %s %s" % (self.id,self.firstname,self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id is None:
            return sys.maxsize
        else:
            return int(self.id)
