from config import dbInfo
import pymysql

def Connect():
  conn = pymysql.connect(
    user    = dbInfo['user'], 
    passwd  = dbInfo['password'], 
    host    = dbInfo['host'], 
    db      = dbInfo['database'], 
    charset = dbInfo['charset']
  )
  
  return conn