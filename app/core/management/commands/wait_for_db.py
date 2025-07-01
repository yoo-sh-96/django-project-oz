# wait_for_db 는 장고가  디비가 준비가 될때까지 연결을 재시도하게 해주기 위해 필요
# 하나의 독커 이미지에 각 컨테이너가(app, db) 존재하기 때문에

import time
from django.core.management.base import BaseCommand
from django.db import connections # db와 연결을 시도

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wating for DB Connetion .. ')

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except(OperationalError, Psycopg2OperationalError):
                self.stdout.write('Retry DB Conmection ... ')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Success to PostgreSQL connection!'))