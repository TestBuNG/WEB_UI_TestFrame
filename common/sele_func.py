# -*- coding: utf-8 -*-
from common.common_func import getScreenShot
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config


CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


class BaseSele():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.t = 0.5

    def findElement(self, locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        if not isinstance(locator, tuple):
            logging.error(
                '***** <Locator Parameter Type Error> : The locator must be tuple, eg:loc = ("method", "value") *****')
        else:
            logging.info(
                '===== <Location Element>：method->%s, value->%s  =====' % (locator[0], locator[1]) + '=====')
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            logging.error(
                '***** <Locator Parameter Type Error> : The locator must be tuple, eg:loc = ("method", "value") *****')
        else:
            try:
                logging.info(
                    '===== <Location Elements>：method->%s, value->%s  =====' % (locator[0], locator[1]) + '=====')
                eles = WebDriverWait(
                    self.driver, self.timeout, self.t
                                     ).until(EC.presence_of_all_elements_located(locator))
                return eles
            except:
                logging.error('***** <Can not located element!> ：locator->%s %(locator) *****')
                return []

    def send_keys(self, locator, text=''):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        try:
            ele.click()
        except:
            logging.error('***** <Click Error> *****')
            getScreenShot(self.driver)


    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_title(self, _title=''):
        """返回bool值"""
        try:
            result = WebDriverWait(
                self.driver,self.timeout,self.t).until(
                EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text=''):
        """返回bool值"""
        if not isinstance(locator, tuple):
            logging.error(
                '***** <Locator Parameter Type Error> : The locator must be tuple, eg:loc = ("id", "value") *****')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t
                                   ).until(EC.text_to_be_present_in_element_value(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        '''返回bool值, value为空字符串，返回Fasle'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        """判断弹出框存在"""
        result = WebDriverWait(self.driver, timeout, self.t
                                   ).until(EC.alert_is_present())
        if result is True:
            return result
        else:
            return False

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            logging.error('***** <get_text Failure>: Return "" *****')
            getScreenShot(self.driver)
            return ""

    def get_attribute(self, locator, name):
        try:
            ele =self.findElement(locator)
            return ele.get_attribute(name)
        except:
            logging.error('***** <get_attribute: %s Failure>: Return "" '%name+' *****')
            getScreenShot(self.driver)
            return ""

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.findElement(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView;", target) #将滚动条拖动到需要显示的元素位置

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        ele = self.findElement(locator) #定位select列表
        Select(ele).select_by_index(index) #通过索引定位列表元素， 默认选第一个

    def select_by_value(self, locator, value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self, locator, text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to_frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to_frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to_frame(ele)
        except:
            logging.warning('----- <Iframe Handover Exception> -----')

    def switch_handle(self, window_name):
        self.driver.switch_to_window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            logging.warning('----- <Alert does not exist!> -----')
            getScreenShot(self.driver)
        else:
            return r

    def move_to_element(self, locator):
        """鼠标悬停"""
        ele = self.findElement(locator)
        ActionChains(self.driver
                     ).move_to_element(ele).perform()

    def js_get_text(self, value):
        js = 'document.getElementById(%s).value'%(value)
        text = self.driver.execute_script(js)
        return text


"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = BaseSele(driver)
    driver.get("http://192.168.57.129:8000/")
    loc_1 = (By.CLASS_NAME, "navbar-brand")
    loc_2 = ('name', 'login')
    time.sleep(5)
    logging.info("sendkeys")
    web.send_keys(loc_2, "111")

"""









