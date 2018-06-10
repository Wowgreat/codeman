from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from codeman import views


urlpatterns = [
    url(r'^api-root/$', views.api_root),
    url(r'^userAdd/$', views.UserAdd.as_view(), name='users-add'),
    url(r'^userLogin/$', views.UserAuth.as_view(), name='user-auth'),
    url(r'^getUserInfo/$', views.UserInfo.as_view(), name='user-info'),
    url(r'^createGroup/$', views.GroupAdd.as_view(), name='group-add'),
    url(r"^getGroupInfoById/$", views.GroupInfoById.as_view(), name="group-info-by-id"),
    url(r'^getGroupsByUser/$', views.GetGroupsByUser.as_view(), name="get-groups-by-user"),
    url(r'^articleAdd/$', views.ArticleAdd.as_view(), name="article-add"),
    url(r'^getArticleInfoById/$', views.GetArticleInfoById.as_view(), name='GetArticleInfoById'),
    url(r'^getArticlesByKeyWord/$', views.GetArticlesByKeyWord.as_view(), name="GetArticlesByKeyWord")
]

urlpatterns = format_suffix_patterns(urlpatterns)