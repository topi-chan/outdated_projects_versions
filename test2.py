#You asked to implement the registration system that has following requirements.
# When new registration occurs, a new user sends to the system a request with his
# name. If such name does not exists in the system database, it is inserted into
# the database, and the user gets the response OK, confirming that registration is
# successful. Otherwise, if the name already exists in the database, the system
# makes up a new user name, then sends it to the user as a prompt and inserts the
# prompt into the database. The new name is formed by the following rule: numbers,
# starting with 1 and incrementing, are appended one after another to name
# (name1, name2, ...), among these numbers the least i is found so that namei does
# not yet exist in the database.
from sa2 import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db1 = SqlAlchemyCreate('sqlite:///User_Base.db', "Users")
db1.sql_create_test()

Base = declarative_base()


class Users(Base):

    __tablename__ = "Users"

    user_name = Column(String)
    id = Column(Integer, primary_key=True)


db_engine = create_engine('sqlite:///User_Base.db')
Session = sessionmaker(bind=db_engine)
session = Session()
k = int(input())
if (k >= 1 and k<= 1000000) is False:
    quit()
#for x in range (k)
while True:
    log = input("Please enter username (empty line to quit): ")
    if log == "": quit()
    lookup = session.query(Users).filter(Users.user_name == log).one_or_none()
    if lookup is None:
        user = Users(user_name=log)
        session.add(user)
        print("OK")
    else:
        lookup = session.query(Users.contains(log))
        print(lookup)
        userd = int(lookup.user_name[-1])
        usern = str(log+"{}").format(str(userd+1))
        # except:
        #     user = Users(user_name=log+"1")
        #     session.add(user)
        #     print(log+"1")
    session.commit()
#    q = session.query(Users.user_name).filter(Users.user_name==log)
