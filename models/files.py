# coding:utf-8

from query import db

'''针对文件记录进行操作的部分'''


def shareFile(fid, fname, description, preview, date, id):
    # 分享模型
    sql = '''
          insert into file (fid,fname,description,preview,date)
          values ('%s','%s','%s','%s','%s');
          insert into upload (id,fid) values ('%s','%s' );
          ''' % (fid, fname, description, preview, date, id, fid)
    db.execute(sql)


def generatingfid(fid):
    # 查看生成的随机id是否已经存在
    sql = 'select * from file where fid="%s";' % fid
    return db.query(sql)


def getSharedModels():
    # 获取所有已经分享的模型
    sql = 'select * from upload natural join (select * from file) as a;'
    return db.query(sql)


def getSharedModelsById(id):
    # 获取某用户分享的所有模型记录
    sql = 'select * from file where fid in (select fid from upload where id="' + id + '");'
    return db.query(sql)


if __name__ == "__main__":
    id=raw_input()
    print getSharedModelsById(id)
