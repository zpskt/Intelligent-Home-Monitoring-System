from django.db import models
from django.utils import timezone

class SysDict(models.Model):
    value = models.CharField(max_length=100, null=True, blank=True, db_comment='数据值')
    label = models.CharField(max_length=100, null=True, blank=True, db_comment='标签名')
    type = models.CharField(max_length=100, null=True, blank=True, db_comment='类型')
    description = models.CharField(max_length=100, null=True, blank=True, db_comment='描述')
    order_num = models.SmallIntegerField(null=True, blank=True, db_comment='排序号')
    remark = models.CharField(max_length=255, null=True, blank=True, db_comment='备注信息')
    create_id = models.CharField(max_length=20, null=True, blank=True, db_comment='创建人ID')
    create_name = models.CharField(max_length=20, null=True, blank=True, db_comment='创建人名称')
    create_time = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='创建时间')
    modify_id = models.CharField(max_length=20, null=True, blank=True, db_comment='修改人ID')
    modify_name = models.CharField(max_length=20, null=True, blank=True, db_comment='修改人名称')
    modify_time = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='修改时间')

    class Meta:
        db_table = 'sys_dict'


class SysMenu(models.Model):
    MENU_TYPE_CHOICES = (
        (0, '目录'),
        (1, '菜单'),
        (2, '按钮'),
    )
    
    parent_id = models.BigIntegerField(db_comment='父级编号')
    parent_ids = models.CharField(max_length=2000, null=True, blank=True, db_comment='所有父级编号')
    name = models.CharField(max_length=100, null=True, blank=True, db_comment='菜单名称')
    path = models.CharField(max_length=200, null=True, blank=True, db_comment='路由地址')
    component = models.CharField(max_length=200, null=True, blank=True, db_comment='组件路径')
    permission = models.CharField(max_length=200, null=True, blank=True, db_comment='权限标识')
    icon = models.CharField(max_length=100, null=True, blank=True, db_comment='菜单图标')
    type = models.SmallIntegerField(choices=MENU_TYPE_CHOICES, null=True, blank=True, db_comment='菜单类型')
    is_frame = models.SmallIntegerField(default=0, db_comment='是否为外链')
    order_num = models.SmallIntegerField(null=True, blank=True, db_comment='排序号')
    status = models.SmallIntegerField(default=1, db_comment='菜单状态')
    remark = models.CharField(max_length=255, null=True, blank=True, db_comment='备注信息')
    create_by = models.BigIntegerField(null=True, blank=True, db_comment='创建者')
    create_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='创建时间')
    update_by = models.BigIntegerField(null=True, blank=True, db_comment='更新者')
    update_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='更新时间')

    class Meta:
        db_table = 'sys_menu'


class SysRole(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, db_comment='角色名称')
    order_num = models.SmallIntegerField(null=True, blank=True, db_comment='排序号')
    remark = models.CharField(max_length=255, null=True, blank=True, db_comment='备注信息')
    create_by = models.BigIntegerField(null=True, blank=True, db_comment='创建者')
    create_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='创建时间')
    update_by = models.BigIntegerField(null=True, blank=True, db_comment='更新者')
    update_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='更新时间')

    class Meta:
        db_table = 'sys_role'


class SysRoleMenu(models.Model):
    role_id = models.BigIntegerField(db_comment='角色编号')
    menu_id = models.BigIntegerField(db_comment='菜单编号')

    class Meta:
        db_table = 'sys_role_menu'


class SysUser(models.Model):
    USER_TYPE_CHOICES = (
        (1, '超级管理员'),
        (2, '普通用户'),
    )
    
    username = models.CharField(max_length=30, null=True, blank=True, db_comment='用户名')
    password = models.CharField(max_length=32, null=True, blank=True, db_comment='密码')
    salt = models.CharField(max_length=20, null=True, blank=True, db_comment='盐')
    nick_name = models.CharField(max_length=30, null=True, blank=True, db_comment='用户昵称')
    email = models.CharField(max_length=50, null=True, blank=True, db_comment='邮箱')
    phone = models.CharField(max_length=15, null=True, blank=True, db_comment='手机')
    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True, db_comment='用户类型')
    photo = models.CharField(max_length=100, null=True, blank=True, db_comment='用户头像')
    last_login_time = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='最近登录时间')
    last_login_ip = models.CharField(max_length=20, null=True, blank=True, db_comment='最近登录IP')
    remark = models.CharField(max_length=255, null=True, blank=True, db_comment='备注信息')
    status = models.SmallIntegerField(default=1, db_comment='状态')
    create_by = models.BigIntegerField(null=True, blank=True, db_comment='创建者')
    create_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='创建时间')
    update_by = models.BigIntegerField(null=True, blank=True, db_comment='更新者')
    update_date = models.DateTimeField(auto_now_add=True,null=True, blank=True, db_comment='更新时间')

    class Meta:
        db_table = 'sys_user'


class SysUserRole(models.Model):
    user_id = models.BigIntegerField(null=True, blank=True, db_comment='用户ID')
    role_id = models.BigIntegerField(null=True, blank=True, db_comment='角色ID')

    class Meta:
        db_table = 'sys_user_role'

