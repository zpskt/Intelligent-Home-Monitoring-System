import logging
from datetime import timezone, datetime
from io import BytesIO

import numpy as np
import pytz
from PIL import Image
from django.utils.timezone import now
from ultralytics import YOLO

import cv2
import matplotlib.pyplot as plt
import os

from spotter.models import DetectionResult, AlarmImage

logger = logging.getLogger('backend.spotter')


class YOLODetector:
    def __init__(self, model):
        self.model = YOLO(model)

    def predict(self, source):
        logger.info(f"source: {source}")
        # 将Django的InMemoryUploadedFile转换为PIL图像
        image = Image.open(BytesIO(source.read()))
        # 检查结果
        detected = False
        output_image_output_path = -1
        results = self.model.predict(source=image, imgsz=640,
                                     project='./out', name='home-monitor', save=False, conf=0.2, iou=0.7,classes=0)
        alarm_image = AlarmImage()
        # 绘制标签并保存标记后的图片
        for result in results:
            for conf in result.boxes.conf:
                if conf > 0.5:
                    detected = True
                    # 保存原始图片
                    parent_dir = os.path.dirname(os.path.dirname(__file__))

                    os.makedirs(parent_dir+"/out/home-monitor", exist_ok=True)
                    # 生成时间戳并格式化
                    timestamp = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y%m%d_%H%M%S")                    # 拼接完整输出路径
                    original_image_output_path = os.path.join(parent_dir, "out", "home-monitor",f"original_image_{timestamp}.jpg")
                    image = np.array(image)
                    cv2.imwrite(original_image_output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

                    plotted_image = result.plot()  # 返回带有标签的PIL图像
                    output_image_output_path = os.path.join(parent_dir, "out", "home-monitor",f"output_image_{timestamp}.jpg")
                    cv2.imwrite(output_image_output_path, plotted_image)

                    # 新建一个model实体，然后将本次的结果赋值给model实体
                    alarm_image.original_image = original_image_output_path
                    alarm_image.label_image = output_image_output_path
                    alarm_image.alarm_type = 'person'
                    alarm_image.alarm_desc = '检测到有人'
                    alarm_image.upload_time = datetime.now(pytz.timezone('Asia/Shanghai'))
                    alarm_image.created_time = datetime.now(pytz.timezone('Asia/Shanghai'))
                    alarm_image.save()

        return detected, output_image_output_path
        # 检查
