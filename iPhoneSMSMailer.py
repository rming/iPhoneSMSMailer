#!/usr/bin/python
#-*- coding:utf-8 -*-
import time
import sqlite3
import smtplib
from email.mime.text import MIMEText

class iPhoneSMSMailer:
    def __init__(self, reviever, smtpConfig):
        self.smtpConfig = smtpConfig
        self.reviever   = reviever
        self.dbFile     = "/var/mobile/Library/SMS/sms.db"
        self.conn       = None

    def loginSMTP(self):
        smtpConf = self.smtpConfig
        s = smtplib.SMTP(smtpConf['server'], smtpConf['port'])
        s.login(smtpConf['email'], smtpConf['pass'])
        return s

    def sendEmail(self, fromNum, smsText, msgType):
        smtp     = self.loginSMTP()
        smtpConf = self.smtpConfig
        if not smsText: smsText = ""
        msgContent = "From: %s\nType: %s\nText: %s" % (fromNum, msgType, smsText)
        msg = MIMEText(msgContent.encode("UTF-8"))
        msg['Subject'] = "New SMS Message"
        msg['From']    = smtpConf['email']
        msg['To']      = self.reviever
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp.quit()

    def getDBConn(self):
        if not self.conn :
            self.conn = sqlite3.connect(self.dbFile)
        return self.conn

    def queryNum(self, handleId, cu):
        self.conn = self.getDBConn()
        queryNumSQL = "select id from handle where ROWID=%d"
        cu.execute(queryNumSQL % handleId)
        res = cu.fetchone()
        if len(res) > 0:
            for k in (range(len(res))):
                return res[k]
        return "UNKNOWN"

    def run(self):
        self.conn = self.getDBConn()
        cu        = self.conn.cursor()
        selectSQL   = "SELECT text,handle_id,service,ROWID,is_from_me,is_read  FROM message WHERE is_from_me=0 AND is_read=0"
        updateSQL   = "UPDATE message SET is_read=1 WHERE is_from_me=0 AND is_read=0 AND ROWID=%d"
        while True:
            cu.execute(selectSQL)
            res = cu.fetchall()
            if len(res) > 0:
                for k in range(len(res)):
                    smsText,handleId,msgType,rowid,__,__  = res[k]
                    if handleId: fromNum  = self.queryNum(handleId, cu) 
                    if smsText : self.sendEmail(fromNum, smsText, msgType)
                    if rowid: 
                        cu.execute(updateSQL % rowid)
                        self.conn.commit()
            time.sleep(20)


if __name__ == "__main__":
    smtpConfig = {
        "email"  : "postmaster@rmingwang.com",
        "pass"   : "",
        "server" : "smtp.mailgun.org",
        "port"   : 587
    }
    reviever  = 'rmingwang@gmail.com'
    SMSMailer = iPhoneSMSMailer(reviever, smtpConfig)
    SMSMailer.run()

