from django.core.management.base import BaseCommand
from dongtai_common.models.agent_method_pool import MethodPool


class Command(BaseCommand):
    help = 'scripts to scan all method pool'
    functions = []
    def add_arguments(self, parser):
        pass
        #parser.add_argument('update', nargs='+', type=int)

    def handle(self, *args, **options):
        method_pools = MethodPool.objects.all()
        from dongtai_engine.tasks import search_vul_from_method_pool
        for method_pool in method_pools:
            search_vul_from_method_pool(method_pool.pool_sign, method_pool.agent_id)
        self.stdout.write(
            self.style.SUCCESS('Successfully flash old data  "%s"' %
                               '123123213321'))
