from django.shortcuts import render,HttpResponse
from blog.models import TextInfo,BlockInfo,Images
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    xxrj=getxxrj();sb= getsb();zj=getzj()
    return render(request,'index.html',{'xxrj':xxrj,'sb':sb,'zj':zj})


# def info(request):
#     xxrj = getxxrj();sb = getsb();zj = getzj()
#     return render(request,'info.html',{'xxrj':xxrj,'sb':sb,'zj':zj})


def list(request,number=None):
    '''所有文章信息查询集，总列表'''
    text = TextInfo.objects.all()
    xxrj = getxxrj();sb = getsb();zj = getzj()
    pag = Paginator(text,5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist=pag.page_range[ye.number:ye.number+4]
    if number == None:
        ye_on=0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet':ye_next,'y_on':ye_on,
                                             'url':'/getnumber/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number-1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request,'list.html',{'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall,
                                           'ylist': ylist,'ynxet':ye_next,
                                           'y_on':ye_on,'url':'/getnumber/'})
def xxrjadd(request,number=None):
    '''学习日记查询集，学习日记列表'''
    xxrj = getxxrj();sb = getsb();zj = getzj()
    text_xuexi = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=7))
    pag = Paginator(text_xuexi, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_xxrj/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_xxrj/'})
def suibi(request,number = None):
    '''随笔查询集，随笔列表'''
    xxrj = getxxrj();sb = getsb();zj = getzj()
    text_suibi = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=5))
    pag = Paginator(text_suibi, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_sb/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_sb/'})
def zaji(request,number = None):
    '''杂记查询集'''
    xxrj = getxxrj();sb = getsb();zj = getzj()
    text_zaji = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=6))
    pag = Paginator(text_zaji, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    print(yall)
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_zj/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_zj/'})
def list_redis(request,number = None):
    '''redis列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_redis=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=1))
    pag = Paginator(test_redis, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_redis/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_redis/'})
def list_numpy(request,number = None):
    '''numpy列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_numpy=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=10))
    pag = Paginator(test_numpy, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_numpy/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_numpy/'})
def list_django(request,number = None):
    '''django列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_django=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=4))
    pag = Paginator(test_django, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_django/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_django/'})
def list_pandas(request,number = None):
    '''pandas列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_pandas=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=9))
    pag = Paginator(test_pandas, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_pandas/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_pandas/'})
def list_python(request,number = None):
    '''python列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_python=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=2))
    pag = Paginator(test_python, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_python/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_python/'})
def list_sql(request,number = None):
    '''sql列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_sql=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=3))
    pag = Paginator(test_sql, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_sql/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_sql/'})
def list_js(request,number = None):
    '''js列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_js=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=12))
    pag = Paginator(test_js, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_js/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_js/'})
def list_linux(request,number = None):
    '''linux列表'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_linux=TextInfo.objects.filter(Block=BlockInfo.objects.get(id=8))
    pag = Paginator(test_linux, 5)
    ye = pag.page(1)
    # 全部页数
    yall = pag.num_pages
    # 分页列表
    ylist = pag.page_range[ye.number:ye.number + 4]
    if number == None:
        ye_on = 0
        # 下一页
        ye_next = ye.number + 1
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_linux/'})
    else:
        try:
            ye = pag.page(number)
        except:
            return HttpResponse('<h1>404错误：你访问的页面不存在</h1>')
        ye_on = ye.number - 1
        ye_next = ye.number + 1
        ylist = pag.page_range[ye.number:ye.number + 4]
        return render(request, 'list.html', {'xxrj': xxrj, 'sb': sb, 'zj': zj,
                                             'ye': ye, 'yall': yall, 'ylist': ylist,
                                             'ynxet': ye_next, 'y_on': ye_on,'url':'/getnumber_linux/'})


def infos(request,id):
    '''默认详细'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_data=TextInfo.objects.get(id=id)
    text_path = str(test_data.text)
    path = '/static/media/'+ text_path
    id = int(id)
    # 获取id列表
    tlist = [i.id for i in TextInfo.objects.all()]
    t = shangxiaye(id,tlist) #判断是否有上下页，调用方法
    # 定位当前页ID下标
    top = tlist[index1(id,tlist)]#上一页下标
    dow = tlist[index2(id,tlist)]#下一页下标
    toptextname = TextInfo.objects.get(id=top)
    dowtextname = TextInfo.objects.get(id=dow)
    return render(request,'info.html',
                  {'data':test_data,'xxrj': xxrj,
                   'sb': sb, 'zj': zj,'path':path,'off':t,
                   'top':top,'dow':dow,'toptext':toptextname,'dowtext':dowtextname})
    pass

def infos_xxrj(request,id):
    '''学习日记详细'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_data=TextInfo.objects.get(id=id)
    text_path = str(test_data.text)
    path = '/static/media/' + text_path
    id = int(id)
    # 获取id列表
    tlist = [i.id for i in TextInfo.objects.filter(Block=BlockInfo.objects.get(id=7))]
    t = shangxiaye(id, tlist)  # 判断是否有上下页，调用方法
    # 定位当前页ID下标
    top = tlist[index1(id, tlist)]  # 上一页下标
    dow = tlist[index2(id, tlist)]  # 下一页下标
    toptextname = TextInfo.objects.get(id=top)
    dowtextname = TextInfo.objects.get(id=dow)
    return render(request, 'info.html',
                  {'data': test_data, 'xxrj': xxrj,
                   'sb': sb, 'zj': zj, 'path': path, 'off': t,
                   'top': top, 'dow': dow, 'toptext': toptextname, 'dowtext': dowtextname})
    pass

def infos_sb(request,id):
    '''sb详细'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_data=TextInfo.objects.get(id=id)
    text_path = str(test_data.text)
    path = '/static/media/' + text_path
    id = int(id)
    # 获取id列表
    tlist = [i.id for i in TextInfo.objects.filter(Block=BlockInfo.objects.get(id=5))]
    t = shangxiaye(id, tlist)  # 判断是否有上下页，调用方法
    # 定位当前页ID下标
    top = tlist[index1(id, tlist)]  # 上一页下标
    dow = tlist[index2(id, tlist)]  # 下一页下标

    toptextname = TextInfo.objects.get(id=top)
    dowtextname = TextInfo.objects.get(id=dow)
    return render(request, 'info.html',
                  {'data': test_data, 'xxrj': xxrj,
                   'sb': sb, 'zj': zj, 'path': path, 'off': t,
                   'top': top, 'dow': dow, 'toptext': toptextname, 'dowtext': dowtextname})
    pass

def infos_zj(request,id):
    '''zj详细'''
    xxrj = getxxrj();
    sb = getsb();
    zj = getzj()
    test_data=TextInfo.objects.get(id=id)
    text_path = str(test_data.text)
    path = '/static/media/' + text_path
    id = int(id)
    # 获取id列表
    tlist = [i.id for i in TextInfo.objects.filter(Block=BlockInfo.objects.get(id=6))]
    t = shangxiaye(id, tlist)  # 判断是否有上下页，调用方法
    # 定位当前页ID下标
    top = tlist[index1(id, tlist)]  # 上一页下标
    dow = tlist[index2(id, tlist)]  # 下一页下标

    toptextname = TextInfo.objects.get(id=top)
    dowtextname = TextInfo.objects.get(id=dow)
    return render(request, 'info.html',
                  {'data': test_data, 'xxrj': xxrj,
                   'sb': sb, 'zj': zj, 'path': path, 'off': t,
                   'top': top, 'dow': dow, 'toptext': toptextname, 'dowtext': dowtextname})
    pass


'''下面是业务逻辑封装的函数'''
def getxxrj():
    # 获取学习日记记录,id=7from
    # block_7 = BlockInfo.objects.get(id=7)
    # 查询学习日记记录下的文章
    text_xuexi = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=7))
    # 取前八篇
    if len(text_xuexi) >= 8:
        text_xuexi = text_xuexi.order_by('-date')[0:8]
    else:
        text_xuexi = text_xuexi.order_by('-date')
    return text_xuexi
def getsb():
    # 获取学习日记记录,id=5
    # block_5 = BlockInfo.objects.get(id=5)
    # 查询随笔记录下的文章
    text_suibi = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=5))
    # 取前八篇
    if len(text_suibi) >= 8:
        text_suibi = text_suibi.order_by('-date')[0:8]
    else:
        text_suibi = text_suibi.order_by('-date')
    return text_suibi
def getzj():
    text_zaji = TextInfo.objects.filter(Block=BlockInfo.objects.get(id=6))
    # 取前八篇
    if len(text_zaji) >= 8:
        text_zaji = text_zaji.order_by('-date')[0:8]
    else:
        text_zaji = text_zaji.order_by('-date')
    return text_zaji

def shangxiaye(id,list):
    '''逻辑判断是否有上下页'''
    if id == min(list):
        return '0'
    if id == max(list):
        return '1'#只有上一篇
    if id==min(list) and min(list)==min(list):
        return '2'
    else:
        return '3'#都有


def index1(id,list):
    '''获取上一篇id下标'''
    if list.index(id) > 0:
        return list.index(id)-1
    elif list.index(id)== 0:
        return list.index(id)

def index2(id,list):
    '''获取下一篇id下标'''
    if list.index(id) < len(list)-1:
        return list.index(id)+1
    elif list.index(id) == len(list)-1:
        return list.index(id)