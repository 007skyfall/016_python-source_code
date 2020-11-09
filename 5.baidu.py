#coding:utf-8
import requests
from lxml import etree
import os

class Tieba(object):

    def __init__(self,name):
        self.url = 'https://tieba.baidu.com/f?kw={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) '
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_list_page(self, data):
        data = data.decode().replace('<!--','').replace('-->','')
        # 创建对象
        html = etree.HTML(data)

        # 定位所有帖子节点

        el_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))

        data_list = []
        for el in el_list:
            temp = {}

            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'https://tieba.baidu.com' + el.xpath('./@href')[0]
            data_list.append(temp)
        try:
            next_url = 'http:' + html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')[0]
        except:
            next_url = None

        return data_list,next_url

    def parse_detial_data(self, data):


        # 创建对象
        html = etree.HTML(data)

        img_list = html.xpath('//*[contains(@id,"post_content_")]/img/@src')
        return img_list

    def download(self, img_list):
        if not os.path.exists('python34'):
            os.makedirs('python34')

        for link in img_list:
            print(link)
            data = self.get_data(link)

            filename = 'python34/'  + link.split('/')[-1]
            with open(filename, "wb")as f:
                f.write(data)

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送请求获取响应
            data = self.get_data(next_url)

            # 从响应中提取 帖子标题&链接列表 和 下一页链接
            data_list, next_url = self.parse_list_page(data)

            # 遍历 帖子标题&链接列表
            for data in data_list:
                print(data)
                detail_page = self.get_data(data['link'])
                img_list = self.parse_detial_data(detail_page)
                self.download(img_list)


            # 判断并翻页处理
            if next_url == None:
                break


if __name__ == '__main__':
    tieba = Tieba("李毅")
    tieba.run()