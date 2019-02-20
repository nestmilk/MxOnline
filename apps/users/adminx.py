# _*_ coding: utf-8 _*_

__author__ = 'nestmilk'
__date__ = '2019/1/13 22:03'

import xadmin

from xadmin import views
from xadmin.plugins.auth import UserAdmin

from users.models import EmailVerifyRecord, Banner, UserProfile


# class UserProfileAdmin(UserAdmin):
#     pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', "send_time",'send_type' ]
    search_fields = ['code', 'email', 'send_type' ]
    list_filter = ['code', 'email', "send_time",'send_type']
    model_icon = 'fa fa-envelope-o'


class BannerAdmin(object):
    list_display = ['title', 'image', "url", 'index', 'add_time']
    search_fields = ['title', 'image', "url", 'index']
    list_filter = ['title', 'image', "url", 'index', 'add_time']
    model_icon = 'fa fa-bath'



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)