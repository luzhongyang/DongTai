#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/26 下午7:27
# software: PyCharm
# project: lingzhi-engine

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from kombu import Queue, Exchange

from dongtai_conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dongtai_conf.settings')

app = Celery('dongtai')

configs = {k: v for k, v in settings.__dict__.items() if k.startswith('CELERY')}
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

configs["task_queues"] = [
    # normal
    Queue("dongtai-method-pool-scan", Exchange("dongtai-method-pool-scan"), routing_key="dongtai-method-pool-scan"),
    Queue("dongtai-replay-vul-scan", Exchange("dongtai-replay-vul-scan"), routing_key="dongtai-replay-vul-scan"),
    Queue("dongtai-sca-task", Exchange("dongtai-sca-task"), routing_key="dongtai-sca-task"),
    Queue("dongtai-function-flush-data", Exchange("dongtai-function-flush-data"), routing_key="dongtai-function-flush-data"),
    Queue("dongtai-es-save-task", Exchange("dongtai-es-save-task"), routing_key="dongtai-es-save-task"),
    # cronjob
    Queue("dongtai-periodic-task", Exchange("dongtai-periodic-task"), routing_key="dongtai-periodic-task"),
]
# celery config
configs['task_serializer'] = 'json'
configs['result_serializer'] = 'json'
configs['accept_content'] = ['json']
configs['task_ignore_result'] = True
configs['task_acks_late'] = True
configs['task_acks_on_failure_or_timeout'] = True
# configs['worker_concurrency'] = 8
configs["task_routes"] = {
    # normal
    "dongtai_engine.tasks.search_vul_from_method_pool": {'exchange': 'dongtai-method-pool-scan', 'routing_key': 'dongtai-method-pool-scan'},
    "dongtai_engine.tasks.search_vul_from_replay_method_pool": {'exchange': 'dongtai-replay-vul-scan', 'routing_key': 'dongtai-replay-vul-scan'},
    "dongtai_web.dongtai_sca.scan.utils.update_one_sca": {'exchange': 'dongtai-sca-task', 'routing_key': 'dongtai-sca-task'},
    "dongtai_engine.preheat.function_flush": {'exchange': 'dongtai-function-flush-data', 'routing_key': 'dongtai-function-flush-data'},
    "dongtai_common.utils.es.handle_save": {'exchange': 'dongtai-es-save-task', 'routing_key': 'dongtai-es-save-task'},
    "dongtai_common.utils.es.handle_batch_save": {'exchange': 'dongtai-es-save-task', 'routing_key': 'dongtai-es-save-task'},
    "dongtai_engine.elatic_search.data_correction": {'exchange': 'dongtai-es-save-task', 'routing_key': 'dongtai-es-save-task'},
    # cronjob
    "dongtai_engine.tasks.update_agent_status": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
    "dongtai_engine.tasks.heartbeat": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
    "dongtai_engine.tasks.clear_error_log": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
    "dongtai_engine.tasks.vul_recheck": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
    "dongtai_engine.preheat.function_preheat": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
    "dongtai_engine.plugins.data_clean": {'exchange': 'dongtai-periodic-task', 'routing_key': 'dongtai-periodic-task'},
}
configs["CELERY_ENABLE_UTC"] = False
configs["timezone"] = settings.TIME_ZONE
configs["DJANGO_CELERY_BEAT_TZ_AWARE"] = False
configs["CELERY_BEAT_SCHEDULER"] = 'django_celery_beat.schedulers:DatabaseScheduler'

app.namespace = 'CELERY'
app.conf.update(configs)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
from dongtai_conf.settings import DONGTAI_CELERY_CACHE_PREHEAT

def ready(self):
    super().ready()
    checkout_preheat_online(DONGTAI_CELERY_CACHE_PREHEAT)


app.ready = ready
print(f"preheat settings now : {DONGTAI_CELERY_CACHE_PREHEAT}")
def checkout_preheat_online(status):
    from django_celery_beat.models import (
        CrontabSchedule,
        PeriodicTask,
        IntervalSchedule,

    )
    import json
    from datetime import datetime, timedelta
    if not status:
        PeriodicTask.objects.delete(name='preheat functions')
    else:
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=10, period=IntervalSchedule.MINUTES)
        task = PeriodicTask.objects.get_or_create(
            name='preheat functions',  # simply describes this periodic task.
            defaults={
                'interval': schedule,  # we created this above.
                'task': 'dongtai_engine.preheat.function_preheat',  # name of task.
                'args': json.dumps([]),
                'kwargs': json.dumps({}),
            })
        print(task)
