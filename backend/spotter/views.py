# Create your views here.
import logging
import sys

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .yolo_detector import YOLODetector
import os

logger = logging.getLogger('backend.spotter')


def index(request):
    if request.method == 'GET':
        data = {
            'message': 'Hello World!',
            'status': 'success'
        }
        return JsonResponse(data)


@csrf_exempt
def detect_picture(request):
    if request.method == 'POST':
        # 获取上传的文件对象
        file = request.FILES.get('detect_picture')
        # 获取当前文件的绝对路径
        current_dir = os.path.dirname(__file__)

        yolo_detector = YOLODetector(current_dir + '/detection_models/yolo11l.pt')
        detected, alarm_image_id = yolo_detector.predict(file)
        logger.info(detected)
        logger.info(alarm_image_id)
        if detected:
            data = {
                'message': '检测到目标',
                'status': 'success'
            }
            return JsonResponse(data)
        else:
            data = {
                'message': '没有检测到目标',
                'status': 'success'
            }
            return JsonResponse(data)
