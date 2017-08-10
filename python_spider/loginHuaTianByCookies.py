http://blog.csdn.net/u011659379/article/details/48133121


# 通过外部获得cookies模拟登陆


# -*- coding: utf-8 -*-

import requests as req


def test():
    raw_cookies='_ntes_nnid=89ceffa971d48ba6fd0f427739c9253d,1502369196690; _ntes_nuid=89ceffa971d48ba6fd0f427739c9253d; user-from=plogin; from-page=http://love.163.com/?checkUser=1&vendor=love.pLogin; NTES_SESS=IB0rmn8wBT56SOlKrHZgqE1iMGyaYW7nRECIxjVq99qYDIhtCDuhBvlJTDXSDmu8jdMrrJQzB4T.ie_yU0qf98H9f72WP.L6xmNgFwbBnLzLu5VqJsNK1EkGUBVfG0nilSQ7_WtpdeUHYHm2K3lA9g_cD; S_INFO=1502372540|0|2&10##|wy201505131238; P_INFO=wy201505131238@163.com|1502372540|0|ht|00&99|chq&1502370805&ht#jix&360100#10#0#0|&0|ht|wy201505131238@163.com'
    cookies = {}
    for line in raw_cookies.split(';'):
        key, value = line.split('=', 1)  # 1代表只分一次，得到两个数据
        cookies[key] = value
    testurl = 'https://love.163.com/'
    s = req.get(testurl, cookies=cookies)
    print(s.text)



if __name__ == '__main__':
    test()