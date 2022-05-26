#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# software: PyCharm
# project: lingzhi-engine
from dongtai_common.models.hook_type import HookType
from rest_framework import serializers


class HookTypeSerialize(serializers.ModelSerializer):
    class Meta:
        model = HookType
        fields = ['id', 'name']
