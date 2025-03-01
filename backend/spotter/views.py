# Create your views here.
import logging
import os
import threading

import cv2
from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .yolo_detector import YOLODetector

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
            try:
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
            except Exception as e:
                logger.error(f'处理文件 {file.name} 时出错: {e}')
                result = {
                    'filename': file.name,
                    'message': str(e),
                    'status': 'error',
                }
            results.append(result)

        res = {
            'message': '批量检测完成',
            'status': 'success',
            'data': results
        }
        return JsonResponse(res)

@csrf_exempt
def create_video_detection_task(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        if not video_url:
            return JsonResponse({'message': '视频流链接未提供', 'status': 'error'})

        # 创建一个新的线程来处理视频流检测任务
        thread = threading.Thread(target=video_detection_task, args=(video_url,))
        thread.start()

        return JsonResponse({'message': '创建任务成功', 'status': 'success'})

def video_detection_task(video_url):
    # try:
    #     response = requests.get(video_url, stream=True)
    #     response.raise_for_status()
    # except requests.RequestException as e:
    #     logger.error(f'无法获取视频流: {e}')
    #     return
    #
    # if response.status_code != 200:
    #     logger.error('无法获取视频流')
    #     return

    current_dir = os.path.dirname(__file__)
    yolo_detector = YOLODetector(current_dir + '/detection_models/yolo11l.pt')
    if video_url == '0':
        video_url = 0
        video_capture = cv2.VideoCapture(video_url,cv2.CAP_AVFOUNDATION)
    else:
        video_capture = cv2.VideoCapture(video_url)
    if not video_capture.isOpened():
        logger.error('无法打开视频流')
        return

    frame_count = 0

    while True:
        ret, original_frame = video_capture.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 10 != 0:  # 每10帧检测一次
            continue

        # 将OpenCV的BGR图像转换为PIL图像
        pil_image = Image.fromarray(cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB))
        try:
            original_frame, detect_frame = yolo_detector.predict_video_frame(pil_image)
        #     将两个视频帧分别实时展示出来
            cv2.imshow('Original Frame', original_frame)
            cv2.imshow('Detected Frame', detect_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            logger.error(f'处理帧 {frame_count} 时出错: {e}')
            result = {
                'frame_number': frame_count,
                'message': str(e),
                'status': 'error',
            }
            logger.error(result)

    video_capture.release()