# -*- coding: utf-8 -*-
from common.sele_func import BaseSele
from selenium import webdriver
import time
import logging


loc_username = ('name', "login")
loc_password = ('name', "password")
loc_loginBtn = ('class name', "primaryAction")
loc_loginUser = ('class name', "alert-success")
loc_login_error = ('class name', 'alert-danger')

def login(driver, host="http://192.168.57.129:8000/", user="admin", psw="lorda7900"):
    logging.info('=====< Login Action >=====')
    web = BaseSele(driver)
    driver.get(host)
    time.sleep(1)
    web.send_keys(loc_username, user)
    time.sleep(1)
    web.send_keys(loc_password, psw)
    time.sleep(1)
    web.click(loc_loginBtn)
    time.sleep(1)


def get_login_user(driver):
    web = BaseSele(driver)
    text = web.get_text(loc_loginUser)
    return text


def get_login_error(driver):
    web = BaseSele(driver)
    text = web.get_text(loc_login_error)
    return text
