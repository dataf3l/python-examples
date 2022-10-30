#!/QOpenSys/etc/alternatives/python

""" Example program using IBM_DB against Db2"""

import os
import sys
import getpass
import platform
import ibm_db
import ibm_db_dbi
import datetime
from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def index():

    # --------------------------------------------------
    # Database Connection Settings
    # --------------------------------------------------
    database = "dataf4l"
    hostname = "pub400.com"
    userid = "dataf4l"
    password = "xxxxxx"
    port = 50000


    db2conn = ibm_db.connect("*LOCAL","dataf4l","xxxxxx")
    hdbi = ibm_db_dbi.Connection(db2conn)

    if hdbi:
        print("connected")

    # --------------------------------------------------
    # Query 1
    # --------------------------------------------------
    print("\nQuery1 begin")

    # insert into ARC02 (ARC2NID, ARC2MSG) VALUES('4', 'This is a msg')

    my_sql = """select  ARC2NID, ARC2MSG FROM DATAF4L1.ARC02 """
    my_cursor = hdbi.cursor()

    html = "<h1>Chat</h1>\n"
    
    try:
        my_cursor.execute(my_sql)
    except Exception as err:
        print("Error on Execute", err)

    try:
        my_tables = my_cursor.fetchall()
        html += "<ul>\n"
        for (ARC2NID,ARC2MSG) in my_tables:
            html += "<li>%s: %s </li></h1>\n" % (ARC2NID,ARC2MSG)
        html += "</ul>\n"

    except Exception as err:
        print("Error on Fetch", err)

    # --------------------------------------------------
    # Clean up
    # --------------------------------------------------
    if hdbi:
        if hdbi.close():
            print("disconnected")

    html += "<br/><a href='/add'>Add Message</a>\n"
    return html + "<hr/>Generated at " + str(datetime.datetime.now())


@app.route('/add')
def add():
    # connect to the DB
    db2conn = ibm_db.connect("*LOCAL","dataf4l","xxxxxx")
    hdbi = ibm_db_dbi.Connection(db2conn)
    # show a HTML form with 2 fields
    # when the form is submitted, the data is sent to the server
    # the server then adds the data to the DB
    # the server then redirects to the index page
    # --------------------------------------------------
    # Database Connection Settings
    # --------------------------------------------------
    html = "<form action='/create' method='post'>\n"
    html += "NID: <input type='text' name='nid' value=''/><br/>\n"
    html += "MSG: <input type='text' name='msg' value=''/><br/>\n"
    html += "<input type='submit' value='Submit'/>\n"
    html += "</form>\n"
    return html

@app.route('/create', methods=['POST'])
def create():
    # connect to the DB
    db2conn = ibm_db.connect("*LOCAL","dataf4l","xxxxxx")
    hdbi = ibm_db_dbi.Connection(db2conn)
    hdbi.set_option({ ibm_db_dbi.SQL_ATTR_TXN_ISOLATION:
                      ibm_db_dbi.SQL_TXN_NO_COMMIT })

    # get the data from the form
    nid = request.form['nid']
    msg = request.form['msg']

    # sanizite the data, remove bad SQL (todo improve)
    nid = nid.replace("'", "")
    msg = msg.replace("'", "")

    # add the data to the DB
    # insert into ARC02 (ARC2NID, ARC2MSG) VALUES('4', 'This is a msg')
    my_sql = """insert into DATAF4L1.ARC02 (ARC2NID, ARC2MSG) VALUES('%s', '%s')""" % (nid, msg)
    my_cursor = hdbi.cursor()
    try:
        my_cursor.execute(my_sql)
        
    except Exception as err:
        print("Error on Execute", err)
    # commit the transaction
    hdbi.commit()

    if hdbi:
        if hdbi.close():
            print("disconnected")


    # redirect to the index page
    return redirect('/')


app.run(host='0.0.0.0', port=8089)

