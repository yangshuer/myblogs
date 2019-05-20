from django.db import models

# Create your models here.
# 测试表
class Article(models.Model):
    title = models.CharField(verbose_name="博客标题",
                             max_length = 100)        #博客标题
    category = models.CharField(verbose_name="博客标签",
                                max_length = 50,blank = True)       #博客标签
    pub_date = models.DateTimeField(verbose_name="发布日期",
                                    auto_now_add = True,
                                    editable=True)       #博客发布日期
    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True,
                                       null=True)
    content = models.TextField(verbose_name='文章正文',blank=True,
                               null=True)  # 博客文章正文
    def __str__(self):
        return self.title

# 文章信息表
class TextInfo(models.Model):
    title = models.CharField(verbose_name='博客标题',
                                max_length=25,null=False,blank=False)
    author= models.CharField(verbose_name='作者',
                                max_length=8,null=False,blank=False)
    Block = models.ForeignKey('BlockInfo',verbose_name='所属版块')

    image = models.ImageField(verbose_name='标题图片',
                              upload_to='images',null=True,blank=True,default='no')

    introduce=models.TextField(verbose_name='简介',max_length=100)

    text = models.FileField(verbose_name='正文',upload_to='files')

    date  = models.DateTimeField(verbose_name='时间',auto_now = True)

    def __str__(self):
        return self.title
    class Meta:
        db_table='Texttable'
    pass

# 版块表
class BlockInfo(models.Model):
    Block_in = models.CharField(verbose_name='版块',max_length=20)
    def __str__(self):
        return self.Block_in
    class Meta:
        db_table='BlockInfo'
    pass

# 图片表
class Images(models.Model):
    image = models.ImageField(verbose_name='图片',
                              upload_to='image', null=True, blank=True)
    Text  = models.ForeignKey('TextInfo',verbose_name='所属文章')
    class Meta:
        db_table='Images'

