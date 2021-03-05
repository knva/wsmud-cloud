import os
import time

from splinter import Browser

from wsgameLogin import GetLoginInfo

class WsSimulation():

    def __init__(self,username,password,area,playername):
        self.username=username
        self.password=password
        self.area=area
        self.playername=playername

    def login(self):
        c = GetLoginInfo(self.username, self.password)
        c.getServer()
        u, p = c.getCookie()
        s = str(self.area)
        playername = self.playername

        self.browser = Browser('chrome')
        # 访问 URL
        url = "http://mush.fun"
        self.browser.visit(url)
        self.browser.cookies.add({'u': u})
        self.browser.cookies.add({'p': p})
        self.browser.cookies.add({'s': s})
        self.browser.reload()
        errNum = 0
        while not self.browser.is_text_present('登陆'):
            time.sleep(3)
            errNum = errNum+1
            if errNum >5:
                return False
        try:
            # 找到并点击搜索按钮
            playerlist = self.browser.find_by_css('.role-list')
            for item in playerlist:
                if playername in item.text:
                    item.click()
            btnlist = self.browser.find_by_xpath('//li[@command="SelectRole"]')
            btnlist.click()

            self.browser.evaluate_script("WG.SendCmd('tm 云武神启动')")
        except Exception as e :
            return False
        return True

    def close(self):
        self.browser.windows[0].close()

    def exec_js(self,code,codetype='raid'):
        try:
            if codetype=='ws':
                self.browser.evaluate_script("WG.SendCmd('{}');".format(code))
            else:
                self.browser.evaluate_script("ToRaid.perform('{}');".format(code))
        except Exception as e:
            print(e)

    def get_image(self):
        screenshot_path = self.browser.screenshot(os.getcwd()+'/absolute_path/{}.png'.format(self.playername), full=True)
        return screenshot_path