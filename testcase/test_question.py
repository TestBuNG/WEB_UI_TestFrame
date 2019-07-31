# -*- coding: utf-8 -*-

from bussness.askQuestionPage import base_ask,publish_qustion,get_success_message,get_sameTitle_error
import time
import pytest
import logging
import allure

qa_url = 'http://192.168.57.129:8000/qa/'


class TestQustion():
    @allure.MASTER_HELPER.severity('Critical')
    @allure.MASTER_HELPER.feature('测试提问功能')
    @allure.MASTER_HELPER.story('用例描述')
    def test_ask_question(self, _driver):
        """
        用例描述：首轮回归测试
        """
        logging.info('===== <Ask Question Action> ======')
        time.sleep(1)
        _driver.get(qa_url)
        time.sleep(1)
        base_ask(_driver)
        publish_qustion(_driver)
        time.sleep(10)
        message = get_success_message(_driver)
        logging.info('=====< Success publish message > message: %s'%(message)+' =====')
        assert '问题已提交' in message


    @allure.MASTER_HELPER.severity('Normal')
    @allure.MASTER_HELPER.feature('测试提问相同问题提示功能')
    def test_ask_sameQuestion(self, _driver):
        logging.info('===== <Ask Same Question Action> ======')
        time.sleep(1)
        base_ask(_driver)
        publish_qustion(_driver)
        time.sleep(1)
        message = get_sameTitle_error(_driver)
        logging.info('=====< Same title message > message: %s'%(message)+' =====')
        assert'已存在' in message


#if __name__ == '__main__':
    #pytest.main(['-s', 'test_question.py'])