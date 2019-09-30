from django.core.management.base import BaseCommand, CommandError
import os
from crontab import CronTab
from django.conf import settings

class Command(BaseCommand):
    help = 'Cron testing'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #init cron
        cron = CronTab(user='omar')

        #add new cron job
        job = cron.new(command='source ~/.pyenv/versions/alten-env/bin/activate && ' + 'python %s >>/tmp/out.txt 2>&1' % (settings.SITE_ROOT + '/server/toggle_vehicle_status.py'))

        #job settings
        job.minute.every(1)

        cron.write()