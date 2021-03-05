# 云武神项目

## 特性
1.使用了splinter 进行模拟登陆

2.使用了falsk进行正向http请求

3.可以直接调用raid.js进行操作


## todo:
1:创建反向ws进行数据回传


## 使用:

```cmd
python3 venv venv
pip install -r requirement.txt
python main.py
```

## 关于chrome浏览器驱动

https://splinter.readthedocs.io/en/latest/drivers/chrome.html


## http api
---

/login  [post]

username 账号

password 密码

area 区

pname 角色名

返回 
成功/失败

---

/getimg [GET] 

pname 角色名


返回网页图片


---

/exec [POST]

pname 角色名

exex 流程代码

ctype ws或者raid  ws为原生指令 raid为raidjs
