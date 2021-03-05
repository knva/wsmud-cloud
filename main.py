from flask import Flask, request
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


    app.run(host='0.0.0.0',port='21035')