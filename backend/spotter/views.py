# Create your views here.
import sys

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .yolo_detector import YOLODetector

sys.path.append('D:/zpskt/Intelligent-Home-Monitoring-System')


def index(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def detect_picture(request):
    try:
        if request.method == 'POST':
            # 获取上传的文件对象
            file = request.FILES.get('detect_picture')
            yolo_detector = YOLODetector('detection_models/yolo11l.pt')
            b = yolo_detector.predict(file)
            if b:
                return HttpResponse('检测到目标')
            else:
                return HttpResponse('没有检测到目标')
    except Exception as e:
        return HttpResponse(f'检测失败: {str(e)}', status=500)
