import random
import string
from model.group import Group
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:path", ["numbers of groups", "path_group_data"])
except getopt.GetoptError as err:
    print(err)
    sys.usage()
    sys.exit(2)

n = 5
path = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif a == "-path":
        path = a


config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",path)


def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters + string.punctuation + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="",header="",footer="")]+[
            Group(name=random_string("name_", 10),
                  header=random_string("header_", 20),
                  footer=random_string("footer_", 20))
            for i in range(n)]


with open(config_path,"w") as f:
    jsonpickle.set_encoder_options("json",indent=2)
    f.write(jsonpickle.encode(testdata))