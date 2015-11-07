# coding:utf-8

from query import db

'''针对文件记录进行操作的部分'''


def shareFile(fid, fname, description, preview, date, id):
    sql = '''
          insert into file (fid,fname,description,preview,date)
          values ('%s','%s','%s','%s','%s');
          insert into upload (id,fid) values ('%s','%s' );
          ''' % (fid, fname, description, preview, date, id,fid)
    db.execute(sql)


def generatingfid(fid):
    sql = 'select * from file where fid="%s";' % fid
    return db.query(sql)
