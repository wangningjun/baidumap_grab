# -*- coding: utf-8 -*-
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
queryStr = '/geocoder/v2/?address=百度大厦&output=json&ak=tKO0y6ddO7QngaXhLTfkch4rN7EK3Otl'

# 对queryStr进行转码，safe内的保留字符不转换
encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

# 在最后直接追加上yoursk
rawStr = encodedStr + 'hpcrRFNVM6C8ha55dKhil74gv0mK2Bu1'

# md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
# 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0

print (hashlib.md5(urllib.quote_plus(rawStr)).hexdigest())

