
from google.appengine.ext import ndb

class Contact(ndb.Model):
    name = ndb.StringProperty
    phone = ndb.StringProperty
    email = ndb.StringProperty


    def __init__(self, arg):
        super(Contact, self).__init__()
        self.arg = arg
