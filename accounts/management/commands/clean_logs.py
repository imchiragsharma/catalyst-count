from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Cleans the debug.log file'

    def handle(self, *args, **options):
        log_file_path = 'debug.log'
        if os.path.exists(log_file_path):
            open(log_file_path, 'w').close()
            self.stdout.write(self.style.SUCCESS('Successfully cleaned debug.log'))
        else:
            self.stdout.write(self.style.WARNING('debug.log does not exist'))