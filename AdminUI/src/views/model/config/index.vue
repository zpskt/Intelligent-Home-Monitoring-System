<template>
  <div class="app-container">
    <!-- 添加搜索框 -->
    <el-form :model="searchForm" inline>
      <el-form-item label="检测任务名称">
        <el-input v-model="searchForm.taskName" placeholder="请输入检测任务名称" />
      </el-form-item>
      <el-form-item label="创建人">
        <el-input v-model="searchForm.creator" placeholder="请输入创建人" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSearch">搜索</el-button>
        <el-button @click="handleReset">重置</el-button>
      </el-form-item>
    </el-form>
    <el-row>
      <el-col :span="24" class="card-box">
        <el-card>
          <div slot="header">
            <span><i class="el-icon-monitor" /> 检测任务列表</span>
            <!-- 移动新建任务和多选删除按钮到此处 -->
            <el-button type="danger" :disabled="selectedTasks.length === 0" @click="handleDeleteSelected" style="margin-left: 10px;">删除</el-button>
            <el-button type="primary" @click="handleAddTask" style="margin-left: 10px;">新建任务</el-button>
          </div>
          <el-table :data="taskList" style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55" />
            <el-table-column prop="taskName" label="检测任务名称" width="180" />
            <el-table-column prop="status" label="状态" width="200" />
            <el-table-column prop="creator" label="创建人" width="200" />
            <el-table-column prop="createTime" label="创建时间" width="300" />
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="mini" @click="handleView(scope.$index, scope.row)">查看</el-button>
                <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
    <!-- 添加任务弹出框 -->
    <el-dialog :title="dialogTitle" :visible.sync="dialogVisible" width="30%">
      <el-form :model="taskForm" label-width="100px">
        <el-form-item label="任务名称">
          <el-input v-model="taskForm.taskName" placeholder="请输入任务名称" />
        </el-form-item>
        <el-form-item label="状态">
          <el-select v-model="taskForm.status" placeholder="请选择状态">
            <el-option label="完成" value="完成" />
            <el-option label="进行中" value="进行中" />
          </el-select>
        </el-form-item>
        <el-form-item label="创建人">
          <el-input v-model="taskForm.creator" placeholder="请输入创建人" />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleSubmit">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 添加详情弹出框 -->
    <el-dialog title="任务详情" :visible.sync="detailDialogVisible" width="30%">
      <el-form :model="currentTaskDetail" label-width="100px">
        <el-form-item label="任务名称">
          <el-input v-model="currentTaskDetail.taskName" placeholder="任务名称" readonly />
        </el-form-item>
        <el-form-item label="状态">
          <el-input v-model="currentTaskDetail.status" placeholder="状态" readonly />
        </el-form-item>
        <el-form-item label="创建人">
          <el-input v-model="currentTaskDetail.creator" placeholder="创建人" readonly />
        </el-form-item>
        <el-form-item label="创建时间">
          <el-input v-model="currentTaskDetail.createTime" placeholder="创建时间" readonly />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="detailDialogVisible = false">关 闭</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'Config',
  data() {
    return {
      // 添加搜索表单数据
      searchForm: {
        taskName: '',
        creator: ''
      },
      // 添加任务列表数据
      taskList: [],
      // 添加选中的任务数组
      selectedTasks: [],
      // 添加任务表单数据
      taskForm: {
        taskName: '',
        status: '',
        creator: ''
      },
      // 弹出框标题
      dialogTitle: '',
      // 弹出框显示状态
      dialogVisible: false,
      // 当前编辑的任务索引
      currentEditIndex: -1,
      // 添加详情对话框显示状态
      detailDialogVisible: false,
      // 添加当前任务详情
      currentTaskDetail: {}
    }
  },
  created() {
    this.fetchTaskList()
    this.openLoading()
  },
  methods: {
    /** 查询所有的检测任务配置信息 */
    getList() {
      // todo
    },
    // 打开加载层
    openLoading() {
      this.$modal.loading('正在加载缓存监控数据，请稍候！')
      // 睡眠5s
      setTimeout(() => {
        this.$modal.closeLoading()
      }, 5000)
      this.$modal.closeLoading()
    },
    // 添加搜索方法
    handleSearch() {
      console.log('搜索条件:', this.searchForm)
      // todo: 根据搜索条件查询数据
      this.fetchTaskList()
    },
    // 添加重置方法
    handleReset() {
      this.searchForm.taskName = ''
      this.searchForm.creator = ''
      console.log('重置搜索条件')
      // todo: 重置数据并重新查询
      this.fetchTaskList()
    },
    // 添加获取任务列表的方法
    fetchTaskList() {
      // todo: 调用API获取任务列表数据
      // 示例数据
      this.taskList = [
        { taskName: '任务1', creator: '张三', createTime: '2023-10-01', status: '完成' },
        { taskName: '任务2', creator: '李四', createTime: '2023-10-02', status: '进行中' }
      ]
    },
    // 处理选中项变化
    handleSelectionChange(val) {
      this.selectedTasks = val
    },
    // 查看任务
    handleView(index, row) {
      this.currentTaskDetail = { ...row }
      this.detailDialogVisible = true
    },
    // 编辑任务
    handleEdit(index, row) {
      this.dialogTitle = '编辑任务'
      this.taskForm = { ...row }
      this.currentEditIndex = index
      this.dialogVisible = true
    },
    // 删除单个任务
    handleDelete(index, row) {
      this.$confirm('此操作将永久删除该任务, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log('删除任务:', row)
        // todo: 实现删除功能
        this.taskList.splice(index, 1)
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 删除选中的任务
    handleDeleteSelected() {
      this.$confirm('此操作将永久删除选中的任务, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log('删除选中的任务:', this.selectedTasks)
        // todo: 实现批量删除功能
        this.selectedTasks.forEach(task => {
          const index = this.taskList.findIndex(item => item.taskName === task.taskName)
          if (index !== -1) {
            this.taskList.splice(index, 1)
          }
        })
        this.selectedTasks = []
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 新建任务
    handleAddTask() {
      this.dialogTitle = '新建任务'
      this.taskForm = {
        taskName: '',
        status: '',
        creator: ''
      }
      this.currentEditIndex = -1
      this.dialogVisible = true
    },
    // 提交任务表单
    handleSubmit() {
      if (this.currentEditIndex === -1) {
        // 新建任务
        this.taskList.push({ ...this.taskForm, createTime: new Date().toLocaleString() })
      } else {
        // 编辑任务
        this.taskList.splice(this.currentEditIndex, 1, { ...this.taskForm })
      }
      this.dialogVisible = false
    }
  }
}
</script>