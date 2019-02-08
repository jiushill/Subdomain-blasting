#author:九世
#time:2019/2/1

import requests
import threading
import os
import time
import socket
import re
from selenium import webdriver

dict=[]
port=[]
found_domain=[]
lock=threading.BoundedSemaphore(100)

class Rkst:
    def __init__(self,headers):
        self.headers=headers

    def jiekou(self,url,data):
        try:
            rqt=requests.post(url=url,headers=self.headers,data=data)
            jso=rqt.json()['data']
            if len(jso)>0:
                for r in jso:
                    ip=self.sok(r['domain'])
                    title=self.title(r['domain'])
                    op=self.port_scan(r['domain'])
                    if '' in op:
                        pass
                    if '80' in op:
                        self.jietu(url='http://{}'.format(r['domain']))
                    elif '443' in op:
                        self.jietu(url='https://{}'.format(r['domain']))
                    print('[+] 查询到的域名：{} IP地址：{} {} 端口：{}'.format(r['domain'],ip,title,op))
                    print('[+] 查询到的域名：{} IP地址：{} {} 端口：{}'.format(r['domain'],ip,title,op),file=open('save.txt','a'))
            else:
                print('[-] 无数据')
        except Exception as r:
            print('[-] 神奇的报错冒了出来：{}'.format(r))

        lock.release()
    def shenc(self,file):
            for k in file.readlines():
                qc="".join(k.split('\n'))
                yield qc

    def port_read(self,file):
        for p in file.readlines():
            qc2="".join(p.split('\n'))
            yield qc2

    def one_domain(self,url):
        for q in dict:
            urls=q+'.'+url
            ip=self.sok(urls)
            if ip:
                title=self.title(urls)
                op=self.port_scan(str(urls).replace('http://','').replace('https://',''))
                if '' in op:
                    pass
                if '80' in op:
                    self.jietu(url='http://{}'.format(urls))
                elif '443' in op:
                    self.jietu(url='https://{}'.format(urls))
                print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls,ip,title,op))
                print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op),file=open('save.txt','a'))

        lock.release()
    def two_domain(self,url):
        for v in dict:
            for v2 in dict:
                urls=v+'.'+v2+'.'+url
                ip = self.sok(urls)
                if ip:
                    title = self.title(urls)
                    op = self.port_scan(str(urls).replace('http://', '').replace('https://', ''))
                    if '' in op:
                        pass
                    if '80' in op:
                        self.jietu(url='http://{}'.format(urls))
                    elif '443' in op:
                        self.jietu(url='https://{}'.format(urls))
                    print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op))
                    print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op), file=open('save.txt', 'a'))

        lock.release()
    def san_domain(self,url):
        for u in dict:
            for u1 in dict:
                for u2 in dict:
                    urls=u+'.'+u1+'.'+u2+'.'+url
                    ip = self.sok(urls)
                    if ip:
                        title = self.title(urls)
                        op = self.port_scan(str(urls).replace('http://', '').replace('https://', ''))
                        if '' in op:
                            pass
                        if '80' in op:
                            self.jietu(url='http://{}'.format(urls))
                        elif '443' in op:
                            self.jietu(url='https://{}'.format(urls))
                        print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op))
                        print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op), file=open('save.txt', 'a'))

        lock.release()
    def si_domain(self,url):
        for s in dict:
            for s1 in dict:
                for s2 in dict:
                    for s3 in dict:
                        urls=s+'.'+s1+'.'+s2+'.'+s3+'.'+url
                        ip = self.sok(urls)
                        if ip:
                            title = self.title(urls)
                            op = self.port_scan(str(urls).replace('http://', '').replace('https://', ''))
                            if '' in op:
                                pass
                            if '80' in op:
                                self.jietu(url='http://{}'.format(urls))
                            elif '443' in op:
                                self.jietu(url='https://{}'.format(urls))
                            print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op))
                            print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op),file=open('save.txt', 'a'))


        lock.release()
    def wu_domain(self,url):
        for b in dict:
            for b1 in dict:
                for b2 in dict:
                    for b3 in dict:
                        for b4 in dict:
                            urls=b+'.'+b1+'.'+b2+'.'+b3+'.'+b4+'.'+url
                            ip = self.sok(urls)
                            if ip:
                                title = self.title(urls)
                                op = self.port_scan(str(urls).replace('http://', '').replace('https://', ''))
                                if '' in op:
                                    pass
                                if '80' in op:
                                    self.jietu(url='http://{}'.format(urls))
                                elif '443' in op:
                                    self.jietu(url='https://{}'.format(urls))
                                print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op))
                                print('[+] 爆破到的域名：{} IP地址：{} {} 端口：{}'.format(urls, ip, title, op),file=open('save.txt', 'a'))
        lock.release()
    def sok(self,domain):
        try:
            s=socket.getaddrinfo(domain,None)
            return str(s[0][4]).replace("'",'').replace('0','').replace('(','').replace(')','').replace(",",'')
        except:
            pass

    def title(self,domain):
        try:
            url='http://{}'.format(domain)
            url2='https://{}'.format(domain)
            rqt=requests.get(url=url,headers=self.headers,timeout=1)
            if rqt:
                zz=re.findall('<title>.*</title>',rqt.content.decode('utf-8'))
                if 'Server' in rqt.headers:
                    r=rqt.headers
                    server=r['Server']
                else:
                    server=None
                return '标题：{} web环境：{}'.format(str(zz[0]).replace('<title>','').replace('</title>',''),server)
            else:
                rq2=requests.get(url=url2,headers=self.headers,timeout=1)
                zz = re.findall('<title>.*</title>', rq2.content.decode('utf-8'))
                if 'Server' in rqt.headers:
                    r=rqt.headers
                    server=r['Server']
                else:
                    server=None
                return '标题：{} web环境：{}'.format(str(zz[0]).replace('<title>', '').replace('</title>', ''),server)
        except:
            return None
            pass

    def port_scan(self,host):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            for z in port:
                s.connect(('{}'.format(host),int(z)))
                return '{}/open '.format(z)
        except:
            return ''
            pass

    def jietu(self,url):
        brower = webdriver.Chrome()
        brower.get(url)
        brower.save_screenshot('img/{}.png'.format(str(url).replace('https://','').replace('http://','')))
        brower.close()

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    jkl='http://sbd.ximcx.cn/DomainServlet'
    print('九世版子域名查询_何安圻')
    user=input('查询的域名：')
    print('[@] 接下来设置爆破模式，输入1为爆破一级域名，输入2为爆破二级域名，输入3位爆破三级域名，输入4为爆破四级域名，输入5位爆破5级域名，输入all为全开 注意：此模式很慢')
    xw=input('设置爆破模式：')
    data={'domain': '{}'.format(user)}
    obj=Rkst(headers=headers)

    print('[*] 接口查询模式')
    lock.acquire()
    t=threading.Thread(target=obj.jiekou,args=(jkl,data))
    t.start()


    if os.path.exists('file/one.txt'):
        print('[@] 找到了神奇的爆破字典')
    else:
        print('[-] 找不到字典= =#')
        print('[-] 退出程序...')
        exit()

    if os.path.exists('file/port.txt'):
        print('[@] 找到了port.txt')
    else:
        print('[-] 找不到port.txt')
        print('[-] 退出程序...')
        exit()

    dk=open('file/one.txt','r')
    for r in obj.shenc(dk):
        dict.append(r)

    dk2=open('file/port.txt','r')
    for v in obj.port_read(dk2):
        port.append(v)

    print('[*] 爆破模式')
    if xw=='1':
        lock.acquire()
        s=threading.Thread(target=obj.one_domain,args=(user,))
        s.start()

    elif xw=='2':
        lock.acquire()
        s2 = threading.Thread(target=obj.two_domain, args=(user,))
        s2.start()

    elif xw=='3':
        lock.acquire()
        s3 = threading.Thread(target=obj.san_domain, args=(user,))
        s3.start()

    elif xw=='4':
        lock.acquire()
        s4 = threading.Thread(target=obj.si_domain, args=(user,))
        s4.start()

    elif xw=='5':
        lock.acquire()
        s5 = threading.Thread(target=obj.wu_domain, args=(user,))
        s5.start()

    elif xw=='all':
        lock.acquire()
        s = threading.Thread(target=obj.one_domain, args=(user,))
        s.start()

        lock.acquire()
        s2 = threading.Thread(target=obj.two_domain, args=(user,))
        s2.start()

        lock.acquire()
        s3 = threading.Thread(target=obj.san_domain, args=(user,))
        s3.start()

        lock.acquire()
        s4 = threading.Thread(target=obj.si_domain, args=(user,))
        s4.start()

        lock.acquire()
        s5 = threading.Thread(target=obj.wu_domain, args=(user,))
        s5.start()