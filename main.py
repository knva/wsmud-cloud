import os

from flask import Flask, request, send_from_directory, Response
import gExport
from wsgameSimulation import WsSimulation
if __name__ == '__main__':
    app = Flask(__name__)
    gExport._init()
    @app.route('/login',methods=["POST"])
    def login():
        username = request.form.get("usernmae", type=str, default=None)
        password = request.form.get("password", type=str, default=None)
        area = request.form.get("area", type=str, default=None)
        pname = request.form.get("pname", type=str, default=None)
        if username ==None or password==None or area ==None or pname==None:
            return '参数不完整'
        if gExport.get_val(pname,None)!=None:
            gExport.get_val(pname, None).close()

        wss =WsSimulation(username,password,area,pname)
        if wss.login():
            gExport.set_val(pname,wss)
            return '登陆成功'
        else:
            return '登陆失败'

    @app.route('/exec',methods=["POST"])
    def exec_raid():
        exec_data = request.form.get("exec")
        pname = request.form.get("pname", type=str, default=None)
        ctype = request.form.get("ctype", type=str, default='raid')
        if pname ==None or ctype==None:
            return '参数不完整'
        wss = gExport.get_val(pname,None)
        if wss==None:
            return "未登录"
        else:
            wss.exec_js(exec_data,ctype)
            return "已执行"


    def return_img_stream(img_local_path):
        """
        工具函数:
        获取本地图片流
        :param img_local_path:文件单张图片的本地绝对路径
        :return: 图片流
        """
        import base64
        img_stream = ''
        with open(img_local_path, 'r') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream)
        return img_stream


    def get_image(uri):

        mdict = {
            'jpeg': 'image/jpeg',
            'jpg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif'
        }
        mime = mdict[uri.split('.')[-1]]
        if not os.path.exists(uri):
            # Res 是我自己定义的返回类，raw方法将数据组成字典返回
            return None
        with open(uri, 'rb') as f:
            image = f.read()
        return Response(image, mimetype=mime)


    @app.route('/getimg',methods=['GET'])
    def getimage():
        pname = request.args.get("pname", type=str, default=None)
        if pname == None:
            return '参数不完整'
        wss = gExport.get_val(pname, None)
        if wss == None:
            return "未登录"
        else:
            imgpath = wss.get_image()
            return get_image(imgpath)
    app.run(host='0.0.0.0',port='21035')