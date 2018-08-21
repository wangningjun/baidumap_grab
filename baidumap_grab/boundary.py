# -*- coding: utf-8 -*-
import urllib2
import json

'''
实现楼宇的串点爬取,给出米制坐标
'''
class Boun_point():

    def __init__(self,title):
        self.title = title


    def boundary(self):

        url = 'http://map.baidu.com/su?wd='+self.title+'&cid=289&type=0&pc_ver=2'

        try:
            json_object = urllib2.urlopen(url)
        except urllib2.HTTPError,e1:
            print e1
            return ''

        data = json.load(json_object)
        try:
            Uid = data['s'][0].split('$')[5]
        except IndexError,e2:
            print e2
            return ''

        uid_url = 'http://map.baidu.com/?reqflag=pcmap&from=webmap&qt=ext&uid='+Uid+'&ext_ver=new&l=18'
        json_udi = urllib2.urlopen(uid_url)
        boundary_data = json_udi.read()



        # print (data['s'][0])
        my_boundary_data = eval('boundary_data')

        my_boundary_data=my_boundary_data.split('|')[2]
        my_boundary_data=my_boundary_data.split(';')[0]

        return my_boundary_data[2:]



if __name__ == '__main__':

    title = '尊宝大厦'
    Bo = Boun_point(title)
    print Bo.boundary()
