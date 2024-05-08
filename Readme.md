# 学生学习管理规划系统
### 基本表
- 学生：学号，姓名，性别，年龄，导师（link），研究方向名称
- 导师：姓名，性别，研究方向名称，link
- 研究方向：方向名称，方向简介，方向所属学科
- 课程：所属学科号，课程号，课程简介
- 成绩：课程号，学号，得分
- 学习资料：学科号，内容简介，课程号
- 学科：学科名称，学科号，学科简介
### 范式满足
### 实现功能
1. 学生作为系统使用者，可注册，登录，注销学生用户角色
2. 超级管理员拥有一切权限
3. 导师可以注册，登录，注销自身角色，可更改学生自己所教课程的成绩
4. 学生角色，老师角色可以上传学习资料（是否经过大模型审核，有待商榷）
5. 学生可以自行选课，退课，选择学习资料，导师，研究方向
6. 大模型可根据每个学生的成绩，选课，课程等信息为该学生制定选课，选择学习资料，选择研究方向，导师的方案
7. 大模型可辅助查找信息
### 项目特色
