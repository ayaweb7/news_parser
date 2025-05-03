# Notebook news_parser.ipynb
# C:\ProgramData\anaconda3\python.exe C:/Users/User/my_learning/parsing_cases/notebooks/parsing_news.py

# Загрузка библиотек
# Для вспомогательных функций и основного парсера
"""
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

# Для экспорта/импорта временных данных
import json
import csv

# Для работы с динамическими сайтами
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Обновление CSV/JSON с дедупликацией
import pandas as pd

# Google Sheets
from gspread import Client, Spreadsheet, Worksheet, service_account, exceptions
from typing import Optional, List, Dict

# Библиотеки для ТелеБОТа
import telebot
# для указание типов
from telebot import types
# токен лежит в файле config.py
import config

# -------------------------------------------- #
"""


def test_parser():
    print("Заголовок страницы:")

if __name__ == "__main__":
    test_parser()