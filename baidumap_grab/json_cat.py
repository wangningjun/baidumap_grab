# -*- coding:utf-8 -*-
import pandas as pd


class LocaDiv(object):
    def __init__(self, loc_all):
        self.loc_all =loc_all

    # 定义函数,以0.1度为间距分隔总区域
    def lat_all(self):
        lat_left = float(self.loc_all.split(',')[0])
        lat_right = float(self.loc_all.split(',')[2])
        lat_list = []
        for i in range(0,int((lat_right-lat_left+0.0001)/0.1)):
            lat_list.append(lat_left+i*0.1)
        lat_list.append(lat_right)

        return lat_list

    def lng_all(self):
        lng_low = float(self.loc_all.split(',')[1])
        lng_high = float(self.loc_all.split(',')[3])
        lng_list = []
        for i in range(0, int((lng_high - lng_low+0.0001)/0.1)):
            lng_list.append(lng_low+i*0.1)
        lng_list.append(lng_high)

        return lng_list

    def is_com(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ba_list=[]
        for i in range(len(l1)):
            a = str(l1[i])
            for j in range(len(l2)):
                b = str(l2[j])
                ba = b+' '+a
                ba_list.append(ba)
        print ba_list
        return ba_list

    def is_row(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ls_com_v = self.is_com()
        ls = []
        for n in range(0, len(l1) - 1):
            for i in range(len(l1)*n, len(l2)+(len(l2))*n-1):
                a = ls_com_v[i]
                b = ls_com_v[i +len(l2)]
                c = ls_com_v[i + len(l2) + 1]
                d = ls_com_v[i+1]

                ab = a + ',' + b +','+ c +','+ d +','+a
                ls.append(ab)

        return ls

if __name__ == '__main__':
    loc = '30.00,120.00,30.50,120.50'
    Loc2use = LocaDiv(loc).is_row()
    pd.DataFrame(Loc2use).to_csv('grid.csv',index=False,header=False)


    print Loc2use