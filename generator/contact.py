import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:path", ["numbers of contact", "path_contact_data"])
except getopt.GetoptError as err:
    print(err)
    sys.usage()
    sys.exit(2)

n = 5
path = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif a == "-path":
        path = a


config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",path)
empty = Contact(firstname="",lastname= "",company="",address="",home="",mobile_phone="",work_phone="", email_1="")


def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters + string.punctuation + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [empty] +[Contact(firstname= random_string("firstname_",15),
                     lastname= random_string("lastname_",30),
                     company= random_string("company_",15),
                     address= random_string("address_",40),
                     home= random_string("home_",10),
                     mobile_phone= random_string("mobile_phone_",10),
                     work_phone= random_string("work_phone_",10),
                     second_phone =random_string("work_phone_",10),
                     email_1=random_string("email_1_",10),
                     email_2=random_string("email_2_",10),
                     email_3=random_string("email_3_",10))
                     for i in range(5)
                     ]

with open(config_path,"w") as f:
    jsonpickle.set_encoder_options("json",indent = 2)
    f.write(jsonpickle.encode(testdata))