# Create your views here.
import logging
import sys

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import AlarmImage
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
        detected, output_image_output_path = yolo_detector.predict(file)
        # 根据id去models中查询对应的图片

        if detected:
            if output_image_output_path == -1:
                logger.error('找不到图片路径')
            data = {
                'image_url': output_image_output_path
            }
            res = {
                'message': '检测到目标',
                'status': 'success',
                'data': data
            }
            return JsonResponse(res)
        else:
            res = {
                'message': '没有',
                'status': 'success',
            }
            return JsonResponse(res)

@csrf_exempt
def detect_batch_pictures(request):
    if request.method == 'POST':
        # 获取上传的文件对象列表
        files = request.FILES.getlist('detect_pictures')
        # 获取当前文件的绝对路径
        current_dir = os.path.dirname(__file__)

        yolo_detector = YOLODetector(current_dir + '/detection_models/yolo11l.pt')
        results = []

        for file in files:
            detected, output_image_output_path = yolo_detector.predict(file)
            if detected:
                if output_image_output_path == -1:
                    logger.error(f'找不到图片路径: {file.name}')
                data = {
                    'image_url': output_image_output_path
                }
                result = {
                    'filename': file.name,
                    'message': '检测到目标',
                    'status': 'success',
                    'data': data
                }
            else:
                result = {
                    'filename': file.name,
                    'message': '没有',
                    'status': 'success',
                }
            results.append(result)

        res = {
            'message': '批量检测完成',
            'status': 'success',
            'data': results
        }
        return JsonResponse(res)