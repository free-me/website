import mongoengine

# Create your models here.

class StudentModel(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    age = mongoengine.IntField(default=0)

class HostList(mongoengine.Document):
    host = mongoengine.StringField(max_length=15)
    port = mongoengine.IntField(default=0)
    appName = mongoengine.StringField(max_length=500)
    url = mongoengine.StringField(max_length=500)