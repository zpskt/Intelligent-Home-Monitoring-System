import logging
from io import BytesIO

from PIL import Image
from ultralytics import YOLO

logger = logging.getLogger('backend.spotter')


class YOLODetector:
    def __init__(self, model):
        self.model = YOLO('../detection_models/yolo11l.pt')

    def predict(self, source):
        logger.info(f"source: {source}")
        # 将Django的InMemoryUploadedFile转换为PIL图像
        image = Image.open(BytesIO(source.read()))
        logger.info(f"Image format: {image.format}, size: {image.size}")
        results = self.model.predict(source=image, imgsz=640,
                                     project='./out', name='home-monitor', save=True, conf=0.2, iou=0.7)
        # 检查结果
        detected = False
        for result in results:

            # result.boxes.conf 是一个tensor的列表，我要遍历列表只要大于0.5，那我就返回有数据检测到
            for conf in result.boxes.conf:
                if conf > 0.5:
                    detected = True
        return detected
        # 检查
