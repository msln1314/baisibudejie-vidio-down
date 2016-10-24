# _*_ coding:utf-8 _*_
import re,urllib.request,random,time
#获取网址源代码
def get_html(url):
    send_headers={
    'Host':'www.budejie.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
    }
    page= urllib.request.Request(url,headers=send_headers)
    numberurl=urllib.request.urlopen(page).read()
    numberurl= numberurl.decode("utf-8")
    return  numberurl    
#下载视频
def download(mp4_url,path):
    path= "".join(path.split())
    urllib.request.urlretrieve(mp4_url,'d:/糗百/%s.mp4'%path)
    print("下载成功%s！"%path)
#匹配获取视频 url
def get_mpl_url(request):
    reg = r' data-mp4="(.*?.mp4)"'
    mpl_url =re.findall(reg,request)
    return  mpl_url
#匹配获取视频名称
def get_name(request):
    reg = re.compile(r'<div class="j-r-list-c-desc">(.*?)</div>',re.S)
    name = re.findall(reg,request)
    return name
#调用函数
def main():
    html =get_html(url)
    mp4_url=get_mpl_url(html)
    mp4_name = get_name(html)
    #处理下载名称有/的异常
    try:
        for x,y in zip(mp4_url,mp4_name):
            if '/' in y:
                continue
            download(x,y)
    except IOError as e:
            print (e)
#获取网址
number=input("请输入要下载的视频的页数：")
number=int(number)
i=1
for i in range(i,number):
        url= "http://www.budejie.com/video/%d"%i
        time.sleep(random.randint(20,30))       
        print("正在打开下载第%d页"%i)
        main()
        i +=1
print("全部下载完成")