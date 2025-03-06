package com.admin.detect.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.admin.detect.domain.DetectTask;
import com.admin.detect.service.DetectTaskService;
import com.admin.detect.mapper.DetectTaskMapper;
import org.springframework.stereotype.Service;

/**
 * @author zhangpeng
 * @description 针对表【detect_task(检测任务表)】的数据库操作Service实现
 * @createDate 2025-03-06 21:43:44
 */
@Service
public class DetectTaskServiceImpl extends ServiceImpl<DetectTaskMapper, DetectTask>
        implements DetectTaskService {

    @Override
    public IPage<DetectTask> getDetectTaskList(int pageNum, int pageSize) {
        Page<DetectTask> page = new Page<>(pageNum, pageSize);
        return baseMapper.selectPage(page, null);
    }

    @Override
    public DetectTask getDetectTaskById(Long id) {
        return baseMapper.selectById(id);
    }

    @Override
    public boolean updateDetectTaskById(DetectTask detectTask) {
        return baseMapper.updateById(detectTask) > 0;
    }

    @Override
    public boolean deleteDetectTaskById(Long id) {
        return baseMapper.deleteById(id) > 0;
    }
}