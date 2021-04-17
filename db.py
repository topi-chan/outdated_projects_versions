from sa2 import *
sql = SqlAlchemyCreate('sqlite:///Pers.db', "Pers")
sql.sql_create_test()

'''
DROP TABLE Salary;

CREATE TABLE Salary (ID INT primary key, datok DATE, sum NUMBER);

INSERT INTO Salary (ID, datok, sum)  VALUES (1, '2020-12-01', 1100);

CREATE TABLE Persons (ID INT primary key, name TEXT, tabnum NUMBER);
'''
