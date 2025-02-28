from django.apps import AppConfig
from ultralytics import YOLO
import logging
import os
import platform

# 将logger定义为模块级变量
logger = logging.getLogger(__name__)


class SpotterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spotter'
