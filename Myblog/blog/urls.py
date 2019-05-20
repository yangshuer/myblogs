
from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'index/',views.index),
    # url(r'info/',views.info),
    url(r'list/',views.list),
    url(r'xxrjadd/',views.xxrjadd),
    url(r'suibi/',views.suibi),
    url(r'zaji/',views.zaji),
    url(r'list_redis/',views.list_redis),
    url(r'list_numpy/',views.list_numpy),
    url(r'list_django/',views.list_django),
    url(r'list_pandas/',views.list_pandas),
    url(r'list_python/',views.list_python),
    url(r'list_sql/',views.list_sql),
    url(r'list_js/',views.list_js),
    url(r'list_linux/',views.list_linux),
    url(r'infos/(\d+)', views.infos),
    url(r'infos_xxrj/(\d+)',views.infos_xxrj),
    url(r'infos_sb/(\d+)',views.infos_sb),
    url(r'infos_zj/(\d+)',views.infos_zj),
    url(r'getnumber/(\d+)',views.list),
    url(r'getnumber_zj/(\d+)',views.zaji),
    url(r'getnumber_sb/(\d+)',views.suibi),
    url(r'getnumber_xxrj/(\d+)',views.xxrjadd),
    url(r'getnumber_redis/(\d+)',views.list_redis),
    url(r'getnumber_numpy/(\d+)',views.list_numpy),
    url(r'getnumber_python/(\d+)',views.list_python),
    url(r'getnumber_pandas/(\d+)',views.list_pandas),
    url(r'getnumber_sql/(\d+)',views.list_sql),
    url(r'getnumber_linux(\d+)',views.list_linux),
    url(r'getnumber_js/(\d+)',views.list_js),
    url(r'getnumber_django/(\d+)',views.list_django),

]