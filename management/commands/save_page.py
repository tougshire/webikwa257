import logging

from django.core.management.base import BaseCommand, CommandError
from webikwa257.models import IcalendarPage

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Auto saves pages - this is useful for Icalendar pages. ex: \'python manage.py save_page 86 47\' saves pages with ids 86 and 47'

    def add_arguments(self, parser):
        parser.add_argument('page_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for page_id in options['page_ids']:
            try:
                page = IcalendarPage.objects.get(pk=page_id)
            except page.DoesNotExist:
                raise CommandError('Page "%s" does not exist' % page_id)

            page.save() #Icalendar pages will rewrite their data upon save

#            logger.info('Successfully upated page "%s"' % page_id)

#            self.stdout.write(self.style.SUCCESS('Successfully upated page "%s"' % page_id))