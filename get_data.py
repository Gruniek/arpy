#!/usr/bin/env python
# -*- coding: latin-1 -*-
# https://pypi.python.org/pypi/pyserial
# python setup.py install

import sys
import serial #python-serial 
import time
import datetime
import MySQLdb as mdb

con = mdb.connect('HOST', 'USER', 'PASSWORD', 'DATABASE')
cur = con.cursor()


port  = sys.argv[1]
speed = sys.argv[2]

ser = serial.Serial(port, speed)
while 1 :
        datenow  = datetime.datetime.today()

        char = ser.readline()
        data = char.split("-")

        unxt = int(time.time())

        print "- nb     = ", data[0]
        print "- mod    = ", data[1]
        print "- date   = ", datenow
        print "- UnixT  = ", unxt
        print "- com1   = ", data[2]
        print "- com2   = ", data[3]
        print "- com3   = ", data[4]

        print "- var1   = ", data[5]
        print "- var2   = ", data[6]
        print "- var3   = ", data[7]
        print "- var4   = ", data[8]
        print "- var5   = ", data[9]
        print "- var6   = ", data[10]
        print "- var7   = ", data[11]
        print "- var8   = ", data[12]
        print "- var9   = ", data[13]
        print "- var10  = ", data[14]
        print "- var11  = ", data[15]
        print "- var12  = ", data[16]
        print "- var13  = ", data[17]
        print "- var14  = ", data[18]
        print "- var15  = ", data[19]
        print "- var16  = ", data[20]
        print "- var17  = ", data[21]
        print "- var18  = ", data[22]
        print "- var19  = ", data[23]
        print "- var20  = ", data[24]


        cur.execute ("UPDATE `database` SET `date`='%s', `unixtime`='%s', `online`='1', `var1`='%s', `var2`='%s', `var3`='%s' , `var4`='%s' , `var5`='%s' , `var6`='%s', `var7`='%s', `var8`='%s' , `var9`='%s' , `var10`='%s', `var11`='%s', `var12`='%s', `var13`='%s' , `var14`='%s' , `var15`='%s', `var16`='%s', `var17`='%s', `var18`='%s' , `var19`='%s' , `var20`='%s' WHERE `id`='%s' " % (datenow, unxt, data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[0]))

        con.commit()


        print "add"
        cur.execute ("INSERT INTO `datalog` (`id`, `date`, `unixtime`, `var1`, `var2`, `var3`, `var4`, `var5`, `var6`, `var7`, `var8`, `var9`, `var10`, `var11`, `var12`, `var13`, `var14`, `var15`, `var16`, `var17`, `var18`, `var19`, `var20`) VALUES (%s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s,%s , %s, %s, %s, %s)", (data[0], datenow, unxt, data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24]))
        con.commit()

#       cur.execute ("SELECT command FROM `command` WHERE `id`='%s'" % (data[0]))
#       test = cur.fetchone()
#
#       con.commit()
#
#       if not test[0]:
#               print "no command"
#       else:
#               print "SEND COMMAND -> ", test[0]
#               ser.write(test[0])
#               
#               vide = ""
#               cur.execute ("UPDATE `command` SET `command`='%s' WHERE `id`='%s' " % (vide, data[0]))
#               con.commit()
