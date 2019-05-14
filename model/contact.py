
class Contact:

    def __init__(self,id =None, firstname = None, lastname = None, company = None, address = None, home = None, mobile_phone = None, work_phone = None, email = None):
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
        return "Contact: %s %s %s %s " % (self.id,self.firstname,self.lastname,self.address)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address and self.id == other.id
