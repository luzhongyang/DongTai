#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2020/8/20 15:10
# software: PyCharm
# project: dongtai-models

from django.db import models
from dongtai.models.project import IastProject
from dongtai.models.project_version import IastProjectVersion
from dongtai.models.agent import IastAgent
from dongtai.models.user import User
from dongtai.models.talent import Talent
from dongtai.models.department import Department
from dongtai.utils.settings import get_managed
from dongtai_web.dongtai_sca.models import VulPackage
from dongtai.models.aql_info import AqlInfo


class AssetVulRelation(models.Model):
    hash = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_del = models.SmallIntegerField(blank=True, null=True)
    talent = models.ForeignKey(
        to=Talent,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    department = models.ForeignKey(
        to=Department,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    project_version = models.ForeignKey(
        to=IastProjectVersion,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    project = models.ForeignKey(
        to=IastProject,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    agent = models.ForeignKey(
        to=IastAgent,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    vul_package = models.ForeignKey(
        to=VulPackage,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    aql_info = models.ForeignKey(
        to=AqlInfo,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    class Meta:
        managed = get_managed()
        db_table = 'iast_asset_vul_relation'
