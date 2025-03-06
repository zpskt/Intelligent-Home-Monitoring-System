package com.admin.detect.domain;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

import java.time.LocalDateTime;
import java.util.Date;
import lombok.Data;

/**
 * 检测任务表
 * @TableName detect_task
 */
@TableName(value ="detect_task")
@Data
public class DetectTask {
    /**
     * 任务的唯一标识符
     */
    @TableId(type = IdType.AUTO)
    private Integer id;

    /**
     * 任务的名称
     */
    private String taskName;

    /**
     * 任务是否有效，true表示有效，false表示无效
     */
    private Boolean isValid;

    /**
     * 任务是否正在运行，true表示正在运行，false表示未运行
     */
    private Boolean isRun;

    /**
     * 任务的备注信息
     */
    private String remark;

    /**
     * 任务的类型，使用整数表示不同的任务类型
     */
    private Integer taskType;

    /**
     * 任务的参数，以JSON格式存储
     */
    private Object taskParam;

    /**
     * 任务的创建时间
     */
    private LocalDateTime createTime;

    /**
     * 创建任务的用户
     */
    private String createUser;

    /**
     * 任务的更新时间
     */
    private LocalDateTime updateTime;

    /**
     * 更新任务的用户
     */
    private String updateUser;

}