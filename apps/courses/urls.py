# _*_ coding: utf-8 _*_
from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView

__author__ = 'nestmilk'
__date__ = '2019/2/7 20:06'


from django.conf.urls import url


urlpatterns = [
    #课程列表页面
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    #课程章节列表页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    #课程评价页
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),

    #添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),

    #
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),

]