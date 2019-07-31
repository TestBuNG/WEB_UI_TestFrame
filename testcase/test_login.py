# -*- coding: utf-8 -*-
from selenium import webdriver
from bussness.loginPage import login, get_login_user, get_login_error
from common.common_func import ReadCSV
import allure
import pytest
import logging
import os, time

url = "http://192.168.57.129:8000/"


csv_path = os.path.join(os.path.dirname(os.getcwd()), 'data')
csvfile = csv_path + '/login_data.csv'
data1 = ReadCSV(csvfile, 1)
data2 = ReadCSV(csvfile, 2)
data3 = ReadCSV(csvfile, 3)
test_login_data1 = [(data1[0], data1[1], data1[2]), (data2[0], data2[1], data2[2])]
test_login_data2 = [(data3[0], data3[1], data3[2])]

@pytest.mark.skip
@allure.MASTER_HELPER.severity('BLOCKER')
@allure.MASTER_HELPER.feature('测试正常登录功能')
@pytest.mark.parametrize("username, password, expect", test_login_data1)
def test_login(username, password, expect, clean_cookies, _driver):
    login(_driver, host=url, user=username, psw=password)
    time.sleep(1)
    text = get_login_user(_driver)
    logging.info('===== < 登录结果：%s> '%(text)+' =====')
    assert expect in text
    time.sleep(1)


@pytest.mark.skip
@allure.MASTER_HELPER.severity('Critical')
@allure.MASTER_HELPER.feature('测试登录验证功能')
@pytest.mark.parametrize("username, password, expect", test_login_data2)
def test_login_error(username, password, expect, clean_cookies, _driver):
    login(_driver, host=url, user=username, psw=password)
    time.sleep(1)
    text = get_login_error(_driver)
    logging.info('===== < 登录结果：%s> ' % (text) + ' =====')
    assert expect in text


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])





