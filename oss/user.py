#coding=utf-8
import connection

#用来创建及与bucket处理
class User():

    def __init__(self,aws_access_key_id,aws_secret_access_key):
        self.conn = connection.get_connect(aws_access_key_id,aws_secret_access_key)

    def getConn(self):
        #创建连接
        return self.conn

    def get_all_buckets(self):
        print "all buckets" #获取所有bukcet列表
        return self.conn.get_all_buckets()

    def create_bucket(self,bucketname):
        print "create bucket" #创建新的bukcet
        self.conn.create_bucket(bucketname)

    def PutObject(self,bucket_name, object_path, localfile):
        print "put object" #从指定路径上传文件到指定bukcet
        bucket = self.conn.get_bucket(bucket_name)
        key = bucket.new_key(object_path)
        key.set_contents_from_filename(localfile)


    def Getobjects(self,bucket_name):
        print "get bucket's all objects"
        bucket = self.conn.get_bucket(bucket_name)
        return bucket.get_all_keys()

    def getobject(self,bucket_name,object_path,local_path):
        print "get object" # 下载object到指定目录
        bucket = self.conn.get_bucket(bucket_name)
        key = bucket.lookup(object_path)
        key.get_content_to_filename(local_path)


