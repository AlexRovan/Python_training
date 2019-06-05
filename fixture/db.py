import pymysql
from model.group import Group
from model.contact import Contact

class DB_fixture ():

    def __init__(self,host,database,user,password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        try:
            self.connect_BD = pymysql.connect(host =host,database = database, user = user,password = password, autocommit = True)
        except pymysql.err.InternalError and pymysql.err.OperationalError as ex:
            print(ex)

    def get_group_list(self):
        list=[]
        try:
            cursor = self.connect_BD.cursor()
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id,name,header,footer)=row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        try:
            cursor = self.connect_BD.cursor()
            cursor.execute("select id,firstname,lastname,address,home,mobile,work,email,email2,email3 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname,address,home,mobile,work,email,email2,email3)=row
                list.append(Contact(id=str(id),
                                    firstname=firstname,
                                    lastname=lastname,
                                    address=address,
                                    home=home,
                                    mobile_phone=mobile,
                                    work_phone=work,
                                    email_1=email,
                                    email_2=email2,
                                    email_3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connect_BD.close()