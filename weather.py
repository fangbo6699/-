from lxml import etree
import requests
from bs4 import BeautifulSoup
import html5lib
from pyecharts import Bar
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    
}
#####################################
#http://pyecharts.org/#/zh-cn/charts_style
########################################


space=[]    
def parse_page(url):
    resp = requests.get(url,headers=HEADERS)
    html = resp.content.decode('utf-8')
#     print(text)
    soup = BeautifulSoup(html,"lxml")
    div=soup.find("div",class_="conMidtab")
#     print(type(div))
    tables=div.findAll("table")
    
    container={}
    for table in tables:
#         print(i)
#         print(type(tables))
#         print(type(i))
#         print("#"*30)
        trs=table.findAll("tr")[2:]
        for index,tr in enumerate(trs):
            if(index==0):
                city=list(tr.findAll("td")[1].stripped_strings)[0]
            else:
                city=list(tr.findAll("td")[0].stripped_strings)[0]
            
            lowest=list(tr.findAll("td")[-2].stripped_strings)[0]
            space.append({"city":city,"lowest":lowest})
            
            
            
#             print(container)
#         print("*"*30)
   
           
           
            
        
          
def maintest():
#     url="http://www.weather.com.cn/textFC/db.shtml"
    urllist=['http://www.weather.com.cn/textFC/hb.shtml','http://www.weather.com.cn/textFC/db.shtml','http://www.weather.com.cn/textFC/hd.shtml']
    urllist.append("http://www.weather.com.cn/textFC/hz.shtml")
    urllist.append("http://www.weather.com.cn/textFC/hn.shtml")
    urllist.append("http://www.weather.com.cn/textFC/xb.shtml")
    urllist.append("http://www.weather.com.cn/textFC/xn.shtml")
#     urllist.append("http://www.weather.com.cn/textFC/db.shtml")
#     urllist.append("http://www.weather.com.cn/textFC/gat.shtml")
    print(len(urllist))
    for urls in urllist:
        parse_page(urls)
    return space
def showmyresult():
    data=maintest()
    data.sort(key=lambda x: int(x["lowest"]))
    y=list(map(lambda x:int(x["lowest"]),data))
    x=list(map(lambda x:x["city"],data))
    print(x[0:15])
    print(y)
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.use_theme('dark')
    bar.add("fangbo",x[0:8], y[0:8], width=1100)
    # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
    bar.render("temp.html")    # 生成本地 HTML 文件
    


    
if __name__ == '__main__':
    showmyresult()
    print("exit0")
    
