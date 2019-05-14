import sys


class Group:

    def __init__(self, name = None, header = None, footer = None , id = None):
        self.name = name
        self.id = id
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "Group: %s %s" % (self.id,self.name)

    def __eq__(self, other):
        return self.name == other.name and ( self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id is None:
            return sys.maxsize
        else:
            return int(self.id)
