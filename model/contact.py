import sys


class Contact:

    def __init__(self,id = None, firstname = None, lastname = None, company = None, address = None, home = None,
                 mobile_phone = None, work_phone = None,second_phone = None, all_phone_contact = None, email_1 = None,
                 email_2 = None, email_3 = None, all_email_contact = None):
        self.id=id
        self.firstname=firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.second_phone = second_phone
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_email_contact = all_email_contact
        self.all_phone_contact = all_phone_contact

    def __repr__(self):
        return "Contact: %s %s %s %s %s %s" % (self.id,self.firstname,self.lastname , self.address, self.home, self.email_1)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id is None:
            return sys.maxsize
        else:
            return int(self.id)
