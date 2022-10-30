#!/QOpenSys/etc/alternatives/python

""" Example program using IBM_DB against Db2"""

import os
import sys
import getpass
import platform
import ibm_db
import ibm_db_dbi

# --------------------------------------------------
# Database Connection Settings
# --------------------------------------------------
database = "dataf4l"
hostname = "pub400.com"
userid = "dataf4l"
password = "xxxx"
port = 50000
"""
#connect_string = "ATTACH=FALSE;"
connect_string = ""
connect_string += "DATABASE=" + database + ";"
#connect_string += "HOSTNAME=" + hostname + ";"
#connect_string += "PORT=" + str(port) + ";"
#connect_string += "PROTOCOL=TCPIP;"
connect_string += "UID=" + userid + ";"
connect_string += "PWD=" + password + ";"

# connect_string += "PROTOCOL=TCPIP;PORT=" + str(port) + ";"

connect_options = { "SQL_ATTR_INFO_PROGRAMNAME": "JHMTESTHELPERS", # 20 char max
                    "SQL_ATTR_INFO_USERID" : getpass.getuser(),    # 255 char max
                    "SQL_ATTR_INFO_WRKSTNNAME" : platform.node()   # 255 char max
                  }
# --------------------------------------------------
hdbi = None  # Connection Object
# --------------------------------------------------

try:
    
    hdbi = ibm_db_dbi.connect(connect_string,
        host=hostname, database=database,
        user=userid, password=password,
        conn_options=connect_options)
except ibm_db_dbi.Warning as warn:
    print("Connection warning:", warn)
except ibm_db_dbi.Error as err:
    print("connection error:", err)
    sys.exit(1)
"""

db2conn = ibm_db.connect("*LOCAL","dataf4l","xxxx")
hdbi = ibm_db_dbi.Connection(db2conn)

if hdbi:
    print("connected")

# --------------------------------------------------
# Query 1
# --------------------------------------------------
print("\nQuery1 begin")

#my_sql = """select DEPTNO, DEPTNAME FROM TDEPT;"""
#my_sql = """select table_name, table_owner from QSYS2.SYSTABLES where TABLE_SCHEMA like '%' and TYPE = 'T'"""
my_sql = """select DEPTNO, DEPTNAME FROM DATAF4L1.TDEPT"""
my_cursor = hdbi.cursor()

try:
    my_cursor.execute(my_sql)
except Exception as err:
    print("Error on Execute", err)

try:
    my_tables = my_cursor.fetchall()
    for (DEPTNO,DEPTNAME) in my_tables:
        print(DEPTNO,DEPTNAME)

except Exception as err:
    print("Error on Fetch", err)

# --------------------------------------------------
# Clean up
# --------------------------------------------------
if hdbi:
    if hdbi.close():
        print("disconnected")

print("done")
