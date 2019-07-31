# -*- coding: utf-8 -*-
from common.sele_func import BaseSele
from selenium import webdriver
import time
import logging
import pytest

loc_askBtn = ('class name', 'pull-right')
loc_title = ('name', 'title')
loc_content_edit = ('name', 'content')
loc_tag = ('name', 'tags')
loc_publishBtn = ('id', 'publish')
loc_draftBtn = ('id', 'draft')
loc_cancelBtn = ('class name', 'btn-light')
loc_content_preview = ('id', 'preview-tab')
loc_preview_text = ('class name', 'markdownx-preview')
loc_success_alert = ('id', 'messages')
loc_title_error = ('class name', 'invalid-feedback')


def get_preview_text(driver):
    web = BaseSele(driver)
    web.click(loc_content_preview)
    web.get_text(loc_preview_text)


def base_ask(driver):
    web = BaseSele(driver)
    web.click(loc_askBtn)
    web.send_keys(loc_title, '提出问题722')
    web.send_keys(loc_content_edit, '问题内容12345')
    web.send_keys(loc_tag, '问题标签12345')


def save_draft(driver):
    web = BaseSele(driver)
    base_ask(driver)
    web.click(loc_draftBtn)


def publish_qustion(driver):
    web = BaseSele(driver)
    web.click(loc_publishBtn)


def cancel(driver):
    web = BaseSele(driver)
    web.click(loc_cancelBtn)


def get_success_message(_driver):
    web = BaseSele(_driver)
    message = web.get_text(loc_success_alert)
    return message


def get_sameTitle_error(_driver):
    web = BaseSele(_driver)
    message = web.get_text(loc_title_error)
    return message