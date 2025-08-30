from django.test import TestCase
from django.conf import settings

from wagtail.test.utils import WagtailPageTestCase
from wagtail.models import Site

from webikwa257.models import ArticleIndexPage, ArticlePage, IcalendarIndexPage, RedirectPage, SidebarPage,\
    IcalendarPage, IcalCombinerPage

default_test_ics_source = "https://calendar.google.com/calendar/ical/c_029797f3540c28bde5137e22119757d392bf274ecfb24d3078e2f1c2777f9aea%40group.calendar.google.com/public/basic.ics"


class IcalendarTestCase(WagtailPageTestCase):
    
    @classmethod
    def setUpTestData(cls):
        root = ArticlePage.get_first_root_node()
        Site.objects.create(
            hostname="testserver",
            root_page=root,
            is_default_site=True,
            site_name="testserver",
        )
        
        articles=ArticleIndexPage(title="Articles")
        root.add_child(instance=articles)
        cls.home = RedirectPage(title="Home",target_page=articles)
        root.add_child(instance=cls.home)
        articles.move(cls.home)
        cls.page = ArticlePage(
            title="First Article"
        )
        articles.add_child(instance=cls.page)

        cls.sidebar_left = SidebarPage(title="Left Sidebar")
        cls.home.add_child(instance=cls.sidebar_left)
        
    def test_can_create_icalendar(self):
        calendar_index = IcalendarIndexPage(
            title="Calendar Index"
        )
        self.home.add_child(instance=calendar_index)

        
        python_calendar = IcalendarPage(
            title="Coding Tests",
            source=settings.TEST_ICS_SOURCE if hasattr(settings, "TEST_ICS_SOURCE") else default_test_ics_source  
        )
        calendar_index.add_child(instance=python_calendar)

        combiner = IcalCombinerPage(
            title="Main Calendars",
            calendars=[python_calendar] 
        )
        self.sidebar_left.add_child(instance=combiner)
        

        test_summaries = settings.TEST_ICS_SUMMARIES if hasattr(settings, "TEST_ICS_SUMMARIES") else []
        if len(test_summaries) == 0:
            self.fail("Please add TEST_ICS_SUMMARIES to settings and include strings to search for")
        for test_summary in test_summaries:
            self.assertIn(test_summary, python_calendar.data)
            