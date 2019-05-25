# coding: utf-8
from __future__ import unicode_literals
from pdw.contrib.http import get_user_agent
import uuid
import tempfile
from time import sleep
from selenium import webdriver
import mechanize
from bs4 import BeautifulSoup
from django.conf import settings
import deathbycaptcha
import logging
import os
import platform
from PIL import Image

logger = logging.getLogger(__name__)

if platform.system() == 'Windows': #cx_oracle usa unicode, porem da problema POPEN
    for k,v in os.environ.iteritems():
        os.environ[k] = str(v)

class CaptchaScraper(object):
    def __init__(self, url, img):
        self.url = url
        self.img = img
        self.client = deathbycaptcha.SocketClient(settings.CAPTCHAR_USERNAME, settings.CAPTCHAR_PWD)
        self.captcha = None
        self.retorno = None
        self.retorno_get = None

    def set_post_data(self):
        raise NotImplementedError

    def captcha_validation(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class MechanizeCaptchaScraper(CaptchaScraper):
    def __init__(self, url, img, *args, **kwargs):
        super(MechanizeCaptchaScraper, self).__init__(url, img)
        self.br = mechanize.Browser()
        agent = get_user_agent()
        self.br.addheaders = [('User-agent', agent)]
        self.br.set_handle_robots(False)
        self.br.set_handle_redirect(mechanize.HTTPRedirectHandler)
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)

        if hasattr(settings, 'HTTP_PROXY') and 'proxy' in kwargs:
            self.br.set_proxies({"http": getattr(settings,'HTTP_PROXY')})

    def execute(self):
        response = self.br.open(self.url)
        self.retorno_get = response.get_data()
        soup = BeautifulSoup(self.retorno_get, "lxml")
        self.image = None
        for img in soup.findAll('img'):
            if img['src'].startswith(self.img):
                image_response = self.br.open_novisit(img['src'])
                self.image = image_response.read()

        if self.image:
            f = tempfile.NamedTemporaryFile(delete=False)
            f.write(self.image)
            f.close()
            try:
                try:
                    self.captcha = self.client.decode(f.name)
                    if self.captcha:
                        print self.captcha
                        self.set_post_data()
                        self.br.submit()
                        sleep(10)
                        self.retorno = self.br.response().read()
                except deathbycaptcha.AccessDeniedException:
                    logger.error('PDW - acabou creditos do captcha')
                    raise Exception ("error: Access to DBC API denied, check your credentials and/or balance")
            finally:
                os.unlink(f.name)

class SeleniumCaptchaScraper(CaptchaScraper):
    def __init__(self, url, img, *args, **kwargs):
        super(SeleniumCaptchaScraper, self).__init__(url, img)
        headers = {
            'User-Agent': get_user_agent()
        }
        for key, value in enumerate(headers):
            webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
        if 'proxy' in kwargs and hasattr(settings, 'HTTP_PROXY'):
            myProxy = getattr(settings,'HTTP_PROXY')
            service_args = [
                '--proxy=%s' % myProxy,
                '--proxy-type=http',
                ]
            self.driver = webdriver.PhantomJS(settings.PHANTOMJS_PATH,service_args=service_args)
        else:
            # self.driver = webdriver.PhantomJS(settings.PHANTOMJS_PATH)
            self.driver = webdriver.Chrome(settings.CHROME_PATH)
        self.driver.set_page_load_timeout(30)

    def switch(self):
        pass

    def get_wait_for(self):
        pass

    def post_wait_for(self):
        pass

    def execute(self):
        self.screenshot_path = '%s/%s.png' % (tempfile.gettempdir(),uuid.uuid4())
        self.captcha_cropped_path = '%s/%s.png' % (tempfile.gettempdir(),uuid.uuid4())

        self.driver.get(self.url)
        self.get_wait_for()
        self.driver.get_screenshot_as_file(self.screenshot_path)
        self.crop_image()

        try:
            self.captcha = self.client.decode(self.captcha_cropped_path)
            if self.captcha:
                print self.captcha
                self.set_post_data()
                self.switch()
                self.get_wait_for()
                self.retorno = self.driver.page_source.encode('utf-8')
        except deathbycaptcha.AccessDeniedException:
            logger.error('PDW - acabou creditos do captcha')
            raise Exception ("error: Access to DBC API denied, check your credentials and/or balance")

    def _crop_image(self, image):
        element = self.driver.find_element_by_id(image) # find part of the page you want image of
        location = element.location
        size = element.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        screenshot_file = Image.open(self.screenshot_path)
        captcha_cropped = screenshot_file.crop((left, top, right, bottom))
        captcha_cropped.save(self.captcha_cropped_path)

    def crop_image(self):
        raise NotImplementedError

    def __del__(self):
        self.driver.quit()
        try:
            os.unlink(self.screenshot_path)
            os.unlink(self.captcha_cropped_path)
        except:
            pass

