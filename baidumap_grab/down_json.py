# -*- coding:utf-8 -*-
import json
import os
import urllib2
import sys
import time
import boundary

reload(sys)

sys.setdefaultencoding('utf8')
# 定义类，首先400条数据的抓取及json数据解析
class BaiDuPOI(object):
    # 构造函数，传入检索类型及
    def __init__(self, itemy, loc):
        self.itemy = itemy
        self.loc = loc
        # 生成20页子页码

    def urls(self):
        api_key = 'your key'
        sn = 'your sn'
        urls = []
        for pages in range(0, 10):
            url = 'http://api.map.baidu.com/place/v2/search?query=' + self.itemy + '&bounds=' + self.loc + '&page_size=20&page_num=' + str(
                pages) + '&output=json&ak=' + api_key
            urls.append(url)
        return urls
    # 对20页子页码进行解析，并提取出宾馆名称、经纬度，返回一个列表
    def baidu_search(self):
        json_sel = []
        for url in self.urls():
            json_obj = urllib2.urlopen(url)
            data = json.load(json_obj)

            for item in data['results']:
                jname = item["name"]
                jlat = item["location"]["lat"]
                jlng = item["location"]["lng"]
                js_sel = jname + ',' + str(jlat) + ',' + str(jlng)
                json_sel.append(js_sel)
        return json_sel

class LocaDiv(object):
    def __init__(self, loc_all):
        self.loc_all =loc_all

    # 定义函数,以0.05度为间距分隔总区域
    def lat_all(self):
        lat_left = float(self.loc_all.split(',')[0])
        lat_right = float(self.loc_all.split(',')[2])
        lat_list = []
        for i in range(0,int((lat_right-lat_left+0.0001)/0.05)):
            lat_list.append(lat_left+i*0.05)
        lat_list.append(lat_right)

        return lat_list

    def lng_all(self):
        lng_low = float(self.loc_all.split(',')[1])
        lng_high = float(self.loc_all.split(',')[3])
        lng_list = []
        for i in range(0, int((lng_high - lng_low+0.0001)/0.05)):
            lng_list.append(lng_low+i*0.05)
        lng_list.append(lng_high)

        return lng_list

    def is_com(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ab_list=[]
        for i in range(len(l1)):
            a = str(l1[i])
            for j in range(len(l2)):
                b = str(l2[j])
                ab = a+','+b
                ab_list.append(ab)
        return ab_list

    def is_row(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ls_com_v = self.is_com()
        ls = []
        for n in range(0, len(l1) - 1):
            for i in range(len(l1)*n, len(l2)+(len(l2))*n-1):
                a = ls_com_v[i]
                b = ls_com_v[i + len(l2) + 1]
                ab = a + ',' + b
                ls.append(ab)

        return ls



# 实例化类，打印出数据。
def main():
    star_time = time.time()

    baidu_ak = 'tKO0y6ddO7QngaXhLTfkch4rN7EK3Otl'
    loc = '30.00,120.00,30.50,120.50'
    scene = '美食'
    Loc2use = LocaDiv(loc).is_row()
    nums = 0

    for i in range(len(Loc2use)):

        baidu = BaiDuPOI(scene, Loc2use[i])

        results = baidu.baidu_search()

        for ax in results:

            title = ax.split(',')[0]

            # Boun = boundary.Boun_point(title)
            # boun_point=Boun.boundary()  #不取串点

            # ax=ax+boun_point


            # print ax
        #csv写入方式一
            doc = open('baidu_poi.csv','a')

            doc.write(ax)
            doc.write('\n')
            doc.close()
            nums +=1
            if nums%200==0:
                print(nums)

        #csv写入方式二


        # with open('baidu_poi.csv','a') as doc:
        #     for ax in results:
        #         doc.write(ax)
        #         doc.write('\n')



    end_time = time.time()

    print ('时间花费%2f:'%(end_time-star_time))

if __name__ == '__main__':

    main()