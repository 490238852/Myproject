from APP import models

class index():
    def __init__(self):
        pass
    def user(self):
        data = {'username':"zhangsan",'password':123456,'age':22}
        user_obj = models.UserInfo(**data)
        user_obj.save()
class login():
    def __init__(self):
        pass
class logout():
    pass
