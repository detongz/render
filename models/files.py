# coding:utf-8

from query import db

'''针对文件记录进行操作的部分'''


def shareFile(fid, fname, description, preview, date, id):
    # 分享模型
    sql = '''
          insert into file (fid,fname,description,preview,date)
          values ('%s','%s','%s','%s','%s');
          insert into upload (id,fid) values ('%s','%s');
          ''' % (fid, fname, description, preview, date, id, fid)
    db.execute(sql)


def shareFileImg(fid, fname, description, preview, date, id):
    # 分享图片文件
    sql = '''
          insert into file (fid,fname,description,preview,date,type)
          values ('%s','%s','%s','%s','%s','pic');
          insert into upload (id,fid) values ('%s','%s');
          ''' % (fid, fname, description, preview, date, id, fid)
    db.execute(sql)


def generatingfid(fid):
    # 查看生成的随机id是否已经存在
    sql = 'select * from file where fid="%s";' % fid
    return db.query(sql)


def getSharedModels():
    # 获取所有已经分享的模型
    sql = 'select * from upload natural join (select * from file) as a order by date desc;'
    return db.query(sql)


def getSharedModelsById(id):
    # 获取某用户分享的所有模型记录
    sql = 'select * from file where fid in (select fid from upload where id="' + id + '") order by date desc;'
    return db.query(sql)


def getCertainFile(fid):
    sql = '''
        select f.fid,f.fname,f.description as fdes,f.preview,f.date,us.description as udes,us.image as uImage
        from file as f,upload as u ,user as us
        where f.fid=u.fid and u.fid='%s' and us.id=u.id;''' % fid
    return db.get(sql)


if __name__ == "__main__":
    id = raw_input()
    print getCertainFile(id)
