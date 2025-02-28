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
                                     project='/out', name='home-monitor', save=True, conf=0.2, iou=0.7)
        logger.info(f"Detected: {results}")
        # 检查结果
        detected = False
        for result in results:
            # print(result.boxes)
            print(result.boxes.cls.shape)  # 目标数量
            print(result.boxes.conf)
        return detected
        # 检查
