import mongoengine

class userData(mongoengine.Document):
    userName = mongoengine.StringField(max_length=50)
    passWord = mongoengine.StringField(max_length=100)
    email = mongoengine.StringField(max_length=100)
    phone = mongoengine.StringField(max_length=100)
    userId = mongoengine.IntField(default=0)