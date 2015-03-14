import os


"""
Clear the database
"""
os.system( "tribe/manage.py flush" )

"""
A mock user class just for creating test data
"""
class User:

    def __init__(self, email, password, name):
            self.email = email
            self.password = password
            self.name = name



dad = User("otis.redding@eircom.net", "password", name="Otis")
mam = User("cjepsen@gmail.com", "password", name="Carly Rae")
kid1 = User("alan@yahoo.com", "password", name="Al")
kid2 = User("pearse@yahoo.com", "password", name="Pearse")
kid3 = User("raymond@yahoo.com", "password", name="Ray")



os.system( "http POST http://localhost:8000/api/users/  email="+dad.email+" password="+dad.password+" name="+dad.name ) 

"""
Invite mommy and all the kids
"""
os.system( "http -a "+dad.email+":"+dad.password+" POST http://localhost:8000/api/invited_users/  email="+mam.email)
os.system( "http -a "+dad.email+":"+dad.password+" POST http://localhost:8000/api/invited_users/  email="+kid1.email)
os.system( "http -a "+dad.email+":"+dad.password+" POST http://localhost:8000/api/invited_users/  email="+kid2.email)
os.system( "http -a "+dad.email+":"+dad.password+" POST http://localhost:8000/api/invited_users/  email="+kid3.email)

"""
Then mommy and the kids sign up
"""
os.system( "http POST http://localhost:8000/api/users/  email="+mam.email+" password="+mam.password+" name='"+mam.name+"'")
os.system( "http POST http://localhost:8000/api/users/  email="+kid1.email+" password="+kid1.password+" name="+kid1.name)
os.system( "http POST http://localhost:8000/api/users/  email="+kid2.email+" password="+kid2.password+" name="+kid2.name)
os.system( "http POST http://localhost:8000/api/users/  email="+kid3.email+" password="+kid3.password+" name="+kid3.name)


"""
Create some tasks
"""

