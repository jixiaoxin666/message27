# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from message.models import UserMessage
# Create your views here.


# 显示留言板信息第一条
# jihuixin
# 2018-3-11
def get_form(request):
    user_manages = UserMessage.objects.all()
    if user_manages:
        user_manage = user_manages[0]
    return render(request, 'message_form.html', {'user_manage': user_manage})
