package com.admin.detect.service;

import com.admin.detect.domain.DetectTask;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * @author zhangpeng
 * @description 针对表【detect_task(检测任务表)】的数据库操作Service
 * @createDate 2025-03-06 21:43:44
 */
public interface DetectTaskService extends IService<DetectTask> {

    IPage<DetectTask> getDetectTaskList(int pageNum, int pageSize);

    DetectTask getDetectTaskById(Long id);

    boolean updateDetectTaskById(DetectTask detectTask);

    boolean deleteDetectTaskById(Long id);
}
