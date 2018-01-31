#coding=utf-8
import boto
import boto.s3.connection

def get_connect(aws_access_key_id,aws_secret_access_key):
    cn = boto.connect_s3(aws_access_key_id,aws_secret_access_key,host ='192.168.60.29', port = 7480,is_secure=False, calling_format =boto.s3.connection.OrdinaryCallingFormat())
    #cn = 'connect'
    return cn