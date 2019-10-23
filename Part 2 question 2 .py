import csv
import math

class Salary:
    __id = "",0
    __name = ""
    __salaryamount = 0

    def __init__(self,id,name,position,salaryamount):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salaryamount = salaryamount

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name

staff = min(4500000)
staff = max(5000000)
officer = min(8500000)
officer = max(8500000)
manager = min(10700000)
manager = max(10700000)

def setsalaryamount(self,salaryamount):
    if salaryamount < staff(min(4500000))
        return False
    elif salaryamount > staff(max(4500000))
        return False
    if salaryamount < officer(min(850000))
        return False
    elif salaryamount > officer(max())
        return False
    if salaryamount < manager(min())
        return False
    elif salaryamount > manager(max())
        return False
    else:
        print("error")


class Position:
    __staff = ""
    __manager = ""
    __officer = ""

    def __init__(self,staff,manager,officer):
        self.__staff = staff
        self.__manager = manager
        self.__officer = officer

    def getstaff(self,staff):
        if staff
            return True
        else:
            False

    def getofficer(self,officer):
        if officer
            return True
        else:
            False

    def getmanager(self,manager):
        if manager
            return True
        else:
            False

    def toString(self):
        return "ID (ID = )",self.getid(), "Name [Name = ]",self.getname(),"Position [Position =]",self.getposition,"]"







