# coding:utf-8

from query import db

'''针对文件记录进行操作的部分'''


def shareFile(fid, fname, description, preview, date, id):
    sql = '''
          insert into file (fid,fname,description,preview,date)
          values ()
          ''' % (fid, fname, description, preview, date, id)


def generatingfid(fid):
    sql = 'select * from file where fid="%s";' % (fid)
    return db.query(sql)
