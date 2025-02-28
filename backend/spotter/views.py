# Create your views here.
import sys

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .yolo_detector import YOLODetector
import os
sys.path.append('D:/zpskt/Intelligent-Home-Monitoring-System')


def index(request):
    if request.method == 'GET':
        data = {
            'message': 'Hello World!',
            'status': 'success'
        }
        return JsonResponse(data)


@csrf_exempt
def detect_picture(request):
    try:
        if request.method == 'POST':
            # 获取上传的文件对象
            file = request.FILES.get('detect_picture')
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(__file__)

            yolo_detector = YOLODetector(current_dir+'/detection_models/yolo11l.pt')
            b = yolo_detector.predict(file)
            if b:
                return HttpResponse('检测到目标')
            else:
                return HttpResponse('没有检测到目标')
    except Exception as e:
        return HttpResponse(f'检测失败: {str(e)}', status=500)
