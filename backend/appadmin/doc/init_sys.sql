-- sys_dict definition

CREATE TABLE `sys_dict` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `value` varchar(100) DEFAULT NULL COMMENT '数据值',
  `label` varchar(100) DEFAULT NULL COMMENT '标签名',
  `type` varchar(100) DEFAULT NULL COMMENT '类型',
  `description` varchar(100) DEFAULT NULL COMMENT '描述',
  `order_num` smallint(6) DEFAULT NULL COMMENT '排序号',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `create_id` varchar(20) DEFAULT NULL COMMENT '创建人ID',
  `create_name` varchar(20) DEFAULT NULL COMMENT '创建人名称',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `modify_id` varchar(20) DEFAULT NULL COMMENT '修改人ID',
  `modify_name` varchar(20) DEFAULT NULL COMMENT '修改人名称',
  `modify_time` datetime DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `sys_dict_value` (`type`,`value`) USING BTREE,
  KEY `sys_dict_label` (`type`,`label`) USING BTREE,
  KEY `sys_dict_type` (`type`) USING BTREE
) CHARSET=utf8mb4 COMMENT='字典表';


-- sys_menu definition

CREATE TABLE `sys_menu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `parent_id` bigint(20) NOT NULL COMMENT '父级编号',
  `parent_ids` varchar(2000) DEFAULT NULL COMMENT '所有父级编号',
  `name` varchar(100) DEFAULT NULL COMMENT '菜单名称',
  `path` varchar(200) DEFAULT NULL COMMENT '路由地址',
  `component` varchar(200) DEFAULT NULL COMMENT '组件路径',
  `permission` varchar(200) DEFAULT NULL COMMENT '权限标识',
  `icon` varchar(100) DEFAULT NULL COMMENT '菜单图标',
  `type` tinyint(4) DEFAULT NULL COMMENT '菜单类型（0：目录，1：菜单，2：按钮）',
  `is_frame` tinyint(4) DEFAULT '0' COMMENT '是否为外链（0：否，1：是）',
  `order_num` smallint(6) DEFAULT NULL COMMENT '排序号',
  `status` tinyint(4) DEFAULT '1' COMMENT '菜单状态（0：禁用，1：正常）',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `create_by` bigint(20) DEFAULT NULL COMMENT '创建者',
  `create_date` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` bigint(20) DEFAULT NULL COMMENT '更新者',
  `update_date` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `sys_menu_parent_id` (`parent_id`) USING BTREE
) DEFAULT CHARSET=utf8mb4 COMMENT='菜单表';


-- sys_role definition

CREATE TABLE `sys_role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(20) DEFAULT NULL COMMENT '角色名称',
  `order_num` smallint(6) DEFAULT NULL COMMENT '排序号',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `create_by` bigint(20) DEFAULT NULL COMMENT '创建者',
  `create_date` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` bigint(20) DEFAULT NULL COMMENT '更新者',
  `update_date` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) CHARSET=utf8mb4 COMMENT='角色表';


-- sys_role_menu definition

CREATE TABLE `sys_role_menu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_id` bigint(20) NOT NULL COMMENT '角色编号',
  `menu_id` bigint(20) NOT NULL COMMENT '菜单编号',
  PRIMARY KEY (`id`) USING BTREE
) CHARSET=utf8mb4 COMMENT='角色菜单表';


-- sys_user definition

CREATE TABLE `sys_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(30) DEFAULT NULL COMMENT '用户名',
  `password` varchar(32) DEFAULT NULL COMMENT '密码',
  `salt` varchar(20) DEFAULT NULL COMMENT '盐',
  `nick_name` varchar(30) DEFAULT NULL COMMENT '用户昵称',
  `email` varchar(50) DEFAULT NULL COMMENT '邮箱',
  `phone` varchar(15) DEFAULT NULL COMMENT '手机',
  `user_type` tinyint(4) DEFAULT NULL COMMENT '用户类型（1：超级管理员，2：普通用户）',
  `photo` varchar(100) DEFAULT NULL COMMENT '用户头像',
  `last_login_time` datetime DEFAULT NULL COMMENT '最近登录时间',
  `last_login_ip` varchar(20) DEFAULT NULL COMMENT '最近登录IP',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `status` tinyint(4) DEFAULT '1' COMMENT '状态（0：禁用，1：正常）',
  `create_by` bigint(20) DEFAULT NULL COMMENT '创建者',
  `create_date` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` bigint(20) DEFAULT NULL COMMENT '更新者',
  `update_date` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `sys_user_login_name` (`username`) USING BTREE
) CHARSET=utf8mb4 COMMENT='用户表';


-- sys_user_role definition

CREATE TABLE `sys_user_role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_id` bigint(20) DEFAULT NULL COMMENT '用户ID',
  `role_id` bigint(20) DEFAULT NULL COMMENT '角色ID',
  PRIMARY KEY (`id`) USING BTREE
) CHARSET=utf8mb4 COMMENT='用户角色表';