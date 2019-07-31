# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import logging
from bussness.loginPage import login
import os, time
import csv


def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: firefox or chrome"
             )
    # 添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host", action="store", default="http://192.168.57.129:8000", help="test host->http://192.168.57.129:8000"
    )


@pytest.fixture(scope='session')
def _driver(request):
    driver = webdriver.Chrome()
    time.sleep(1)
    login(driver=driver)

    def fn():
        logging.info("=====< Teardown: quit driver > 全部用例执行完毕! =====")
        driver.quit()
    request.addfinalizer(fn)
    return driver


@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")


@pytest.fixture()
def clean_cookies(_driver):
    logging.info("===== <Cleaning Cookies, Sign Out> =====")
    _driver.delete_all_cookies()
    _driver.refresh()