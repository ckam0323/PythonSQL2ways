from dbconn import Session,Department,Employees,Salary

# 创建会话实例，将来对数据库实现增删改查，都是通过session的方法实现
session = Session()

# 创建部门
# hr = Department(dep_id=1,dep_name='人事部')
# finance = Department(dep_id=2,dep_name='财务部')
# ops = Department(dep_id=3,dep_name='运维部')
# dev = Department(dep_id=4,dep_name='开发部')
# qa = Department(dep_id=5,dep_name='测试部')
# market = Department(dep_id=6,dep_name='市场部')
#
# # add data into biao
# session.add_all([hr,finance,ops,dev,qa,market])

# 创建员工
jax = Employees(
    emp_id=1,emp_name ='贾克斯',birth_date='1986-6-6',
    email='jax@163.com',dep_id=1
)
js = Employees(
    emp_id=2,emp_name='剑圣',birth_date='1988-10-6',
    email='js@163.com', dep_id=2
)
gl = Employees(
    emp_id=3,emp_name='盖伦',birth_date='1989-3-6',
    email='gl@163.com', dep_id=3
)
zx = Employees(
    emp_id=4,emp_name='赵信',birth_date='1990-6-6',
    email='zx@163.com', dep_id=4
)

session.add_all([jax,js,gl,zx])

session.commit()
session.close()