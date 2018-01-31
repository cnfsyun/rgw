#coding=utf-8
from flask import Flask,g,session,render_template,jsonify,request
import user
import requests

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/login')
#登录部分
def login():
    userid = request.args.get('userid')
    password = request.args.get('password')
    key = request.args.get('key')
    key_password = request.args.get('key_password')
    print session.get('userid','none')
    if userid is not None and password is not None and key is not None and key_password is not None:
        session['useid'] = userid
        session['key'] = key
        session['obj'] = key_password
    else:
        session['useid']='test'
        session['password']='fffff'
        session['key'] = 'P5OJ55ZYFMX4AAMGL8T2'
        session['obj']='FdkZtL5wrnapQ7P7fTryy34Lxt0WrdSWUuNiYJhL'
    return jsonify({'good':'Hello World!'})

@app.route("/getallbuckets")
def getUser():
    print session

    userid = request.args.get('userid')
    password = request.args.get('password')

    if 'test' in session.values():
        keys = ''
        obj = ''
        for item in session.items():
            if 'key'in item:
                keys = item[1]
            if 'obj' in item:
                obj = item[1]
        #这个用来保存创建信息
        us = user.User(keys,obj)
        print us.get_all_buckets()
    return jsonify({'result':str(us.get_all_buckets())})

@app.route("/create_bucket")
def createBucket():
    print session

    bucketName = request.args.get('bucketName')


    if 'test' in session.values():
        keys = ''
        obj = ''
        for item in session.items():
            if 'key'in item:
                keys = item[1]
            if 'obj' in item:
                obj = item[1]
        #这个用来保存创建信息
        us = user.User(keys,obj)

        if(bucketName is not None):
            us.create_bucket(bucketName)
        else:
            us.create_bucket("test1")


    return jsonify({'good': 'Hello World!'})

@app.route("/put_object")
def PutObject():
    print session

    bucketName = request.args.get('bucketName')
    object_path = request.args.get('object_path')
    localfile = request.args.get('localfile')

    if 'test' in session.values():
        keys = ''
        obj = ''
        for item in session.items():
            if 'key'in item:
                keys = item[1]
            if 'obj' in item:
                obj = item[1]
        #这个用来保存创建信息
        us = user.User(keys, obj)

        if bucketName is None and object_path is None and localfile is None:
            us.PutObject('test', '/test/oss.test', 'E:\data\WIOT2000_Nov16_ROW')
        else:
            us.PutObject(bucketName, object_path, localfile)

        print us.PutObject(bucketName,object_path,localfile)

    return jsonify({'result':'/test/oss.test'})

@app.route("/check_objects")
def checkobject():
    print session

    bucketName = request.args.get('bucketName')

    if 'test' in session.values():
        keys = ''
        obj = ''
        for item in session.items():
            if 'key'in item:
                keys = item[1]
            if 'obj' in item:
                obj = item[1]
        # 这个用来保存创建信息
        us = user.User(keys, obj)

        if bucketName is None:
            us.Getobjects("mybucket")
        else:
            us.Getobjects(bucketName)

        print us.Getobjects("mybucket")

    return jsonify({'result': str(us.Getobjects("mybucket"))})

@app.route("/get_object")
def getobject():
    print session

    bucketName = request.args.get('bucketName')
    object_path = request.args.get('object_path')
    localfile = request.args.get('localfile')

    if 'test' in session.values():
        keys = ''
        obj = ''
        for item in session.items():
            if 'key'in item:
                keys = item[1]
            if 'obj' in item:
                obj = item[1]
        #这个用来保存创建信息
        us = user.User(keys, obj)

        if bucketName is None and object_path is None and localfile is None:
            us.getobject('test', '/test/oss.test', 'E:\data\WIOT2000_Nov16_ROW')
        else:
            us.getobject(bucketName, object_path, localfile)

        print us.PutObject(bucketName,object_path,localfile)

    return jsonify({'result':'/test/oss.test'})




if __name__ == '__main__':
    app.run()
