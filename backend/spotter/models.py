from django.db import models
from django.utils import timezone


# 定义报警图片类
class AlarmImage(models.Model):
    id = models.AutoField(primary_key=True, db_comment='主键ID')
    user_id = models.CharField(max_length=32, db_comment='用户ID')
    image = models.CharField(max_length=255, db_comment='报警图片')
    original_image = models.CharField(max_length=255, db_comment='原始图片')
    label_image = models.CharField(max_length=255, db_comment='标签后的图片')
    upload_time = models.DateTimeField(auto_now_add=True, db_comment='上传时间')
    is_delete = models.BooleanField(default=False, db_comment='是否删除')
    alarm_time = models.DateTimeField(auto_now_add=True, db_comment='报警时间')
    alarm_type = models.CharField(max_length=32, db_comment='报警类型')
    alarm_desc = models.CharField(max_length=32, db_comment='报警描述')
    callback = models.CharField(max_length=32, db_comment='回调信息')
    created_time = models.DateTimeField(auto_now_add=True, db_comment='创建时间')

    class Meta:
        db_table = 'alarm_image'
        verbose_name = '报警图片'
        verbose_name_plural = '报警图片'


# 识别模型相关信息
class DetectionModel(models.Model):
    id = models.AutoField(primary_key=True, db_comment='主键ID')
    model_name = models.CharField(max_length=32, db_comment='模型名称')
    model_path = models.CharField(max_length=255, db_comment='模型路径')
    model_type = models.CharField(max_length=32, db_comment='模型类型')
    model_desc = models.CharField(max_length=255, db_comment='模型描述')
    model_version = models.CharField(max_length=32, db_comment='模型版本')
    model_size = models.CharField(max_length=32, db_comment='模型大小')
    user_id = models.CharField(max_length=32, db_comment='上传用户ID')
    upload_time = models.DateTimeField(auto_now_add=True, db_comment='上传时间')
    is_delete = models.BooleanField(default=False, db_comment='是否删除')
    created_time = models.DateTimeField(auto_now_add=True, db_comment='创建时间')

    class Meta:
        db_table = 'detection_model'
        verbose_name = '识别模型'
        verbose_name_plural = '识别模型'


# 模型配置

class ModelConfig(models.Model):
    id = models.AutoField(primary_key=True, db_comment='主键ID')
    model_id = models.CharField(max_length=32, db_comment='模型ID')
    model_name = models.CharField(max_length=32, db_comment='模型名称')
    model_type = models.CharField(max_length=32, db_comment='模型类型')
    model_desc = models.CharField(max_length=255, db_comment='模型描述')
    model_version = models.CharField(max_length=32, db_comment='模型版本')
    model_size = models.CharField(max_length=32, db_comment='模型大小')

    class Meta:
        db_table = 'model_config'
        verbose_name = '模型配置'
        verbose_name_plural = '模型配置'

# ... existing code ...


class YoloTrainingConfig(models.Model):
    id = models.AutoField(primary_key=True)
    model_path = models.CharField(max_length=255, db_comment="模型路径")
    data_path = models.CharField(max_length=255, db_comment="数据文件路径")
    epochs = models.IntegerField(default=2, db_comment="训练轮数")
    image_size = models.IntegerField(default=320, db_comment="训练图像尺寸")
    batch_size = models.IntegerField(default=8, db_comment="批次大小")
    workers = models.IntegerField(default=0, db_comment="工作线程数")
    device = models.CharField(max_length=32, default="cuda", db_comment="训练设备")
    model_name = models.CharField(max_length=32, db_comment="模型名称")
    optimizer = models.CharField(max_length=32, default="SGD", db_comment="优化器")
    project = models.CharField(max_length=32, default="runs/train", db_comment="项目路径")
    name = models.CharField(max_length=32, db_comment="训练名称")

    class Meta:
        db_table = 'yolo_training_config'


class DetectionConfig(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=255, db_comment="输入源路径")
    conf = models.FloatField(default=0.25, db_comment="置信度阈值")
    iou = models.FloatField(default=0.7, db_comment="IoU阈值")
    half = models.BooleanField(default=False, db_comment="使用半精度")
    device = models.CharField(max_length=32, default="cuda", db_comment="运行设备")
    show = models.BooleanField(default=False, db_comment="显示检测结果")
    save = models.BooleanField(default=False, db_comment="保存检测结果")
    save_txt = models.BooleanField(default=False, db_comment="保存为文本文件")
    save_conf = models.BooleanField(default=False, db_comment="保存置信度")
    save_crop = models.BooleanField(default=False, db_comment="保存裁剪图像")
    hide_labels = models.BooleanField(default=False, db_comment="隐藏标签")
    hide_conf = models.BooleanField(default=False, db_comment="隐藏置信度")
    max_det = models.IntegerField(default=300, db_comment="最大检测数")
    vid_stride = models.IntegerField(null=True, blank=True, db_comment="视频帧率步长")
    line_width = models.IntegerField(null=True, blank=True, db_comment="边界框线宽")
    visualize = models.BooleanField(default=False, db_comment="可视化特征")
    augment = models.BooleanField(default=False, db_comment="图像增强")
    agnostic_nms = models.BooleanField(default=False, db_comment="类别无关NMS")
    retina_masks = models.BooleanField(default=False, db_comment="高分辨率分割掩膜")
    classes = models.CharField(max_length=255, null=True, blank=True, db_comment="类别过滤")
    boxes = models.BooleanField(default=True, db_comment="显示边界框")
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'detection_config'


class Dataset(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_comment="数据集名称")
    description = models.TextField(db_comment="数据集描述")
    path = models.CharField(max_length=255, db_comment="存储路径")
    type = models.CharField(max_length=32, db_comment="数据集类型")
    is_public = models.BooleanField(default=False, db_comment="是否公开")
    is_deleted = models.BooleanField(default=False, db_comment="是否删除")
    created_by = models.CharField(max_length=32, db_comment="创建者")
    created_time = models.DateTimeField(auto_now_add=True, db_comment="创建时间")

    class Meta:
        db_table = 'dataset'


class TrainingTask(models.Model):
    STATUS_CHOICES = (
        ('pending', '等待中'),
        ('running', '运行中'),
        ('completed', '已完成'),
        ('failed', '失败'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_comment="任务名称")
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='pending', db_comment="任务状态")
    start_time = models.DateTimeField(null=True, blank=True, db_comment="开始时间")
    end_time = models.DateTimeField(null=True, blank=True, db_comment="结束时间")
    log_path = models.CharField(max_length=255, null=True, blank=True, db_comment="日志路径")
    is_deleted = models.BooleanField(default=False, db_comment="是否删除")
    created_by = models.CharField(max_length=32, db_comment="创建者")
    created_time = models.DateTimeField(auto_now_add=True, db_comment="创建时间")

    class Meta:
        db_table = 'training_task'


class DetectionResult(models.Model):
    id = models.AutoField(primary_key=True)
    detected_objects = models.JSONField(db_comment="检测到的物体")
    confidence = models.FloatField(db_comment="总体置信度")
    is_deleted = models.BooleanField(default=False, db_comment="是否删除")
    created_by = models.CharField(max_length=32, db_comment="创建者")
    created_time = models.DateTimeField(auto_now_add=True, db_comment="创建时间")

    class Meta:
        db_table = 'detection_result'
