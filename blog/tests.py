from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from playwright import sync_playwright

import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

class ExampleTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('migrate')
        call_command('createsuperuser', '--noinput', '--username', 'admin', '--email', 'admin@admin.com')
        call_command('loaddata', 'data.json')
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_login(self):
        page = self.browser.newPage()
        page.goto(self.live_server_url)
        page.click('text=Lorem ipsum 1')
        assert 'post/1' in page.url
        page.close()
