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
    # 获取某个分享的文件的作者和文件的相关信息
    sql = '''
        select f.fid,f.fname,f.description as fdes,f.preview,f.date,f.type,us.description as udes,us.id,us.image as uImage
        from file as f,upload as u ,user as us
        where f.fid=u.fid and u.fid='%s' and us.id=u.id;''' % fid
    return db.get(sql)


def getUploadType(fid):
    # 删除分享，获取上传用户名和上传类型
    sql = '''select type,id from file as f,upload as up where up.fid=f.fid and up.fid='%s';''' % fid
    return db.get(sql)


def removeSharedRecord(fid):
    sql = '''
        delete upload,file from upload,file
        where file.fid=upload.fid and upload.fid='%s';''' % fid
    return db.execute(sql)


if __name__ == "__main__":
    id = raw_input()
    print getUploadType(id)
