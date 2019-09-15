from dbconn import Session,Department,Employees,Salary

session = Session()
######################################################################

# qset1 = session.query(Department)
# print(qset1)
#
# for dep in qset1:
#     print(dep.dep_id,dep.dep_name)

# qset2 = session.query(Employees.emp_name,Employees.email)
# print(qset2.all())
#
# for item in qset2:
#     print(item)

# qset3 = session.query(Department).order_by(Department.dep_id)
# qset3 = session.query(Department).order_by(Department.dep_id)[1:3]
# for dep in  qset3:
#     print(dep.dep_id,dep.dep_name)

# qset4 = session.query(Department).filter(Department.dep_id == 3)
# qset4 = session.query(Department).filter(Department.dep_id <= 3)
# print(qset4.all())
# for dep in qset4:
#     print(dep.dep_id,dep.dep_name)

# qset5 = session.query(Department).filter(Department.dep_id>1,Department.dep_id<4)
# for dep in qset5:
#     print(dep.dep_id,dep.dep_name)

# qset6 = session.query(Employees).filter(Employees.email.like('%@163.com'))
# for emp in qset6:
#     print(emp.emp_name,emp.email)

# qset7 = session.query(Department).filter(Department.dep_id.in_([1,3,6]))
# print(qset7.all())
# print(qset7.first())
# dep = qset7.first()
# print(dep.dep_id,dep.dep_name)

# qset8 = session.query(Department).filter(Department.dep_id == 3)
# qset8 = session.query(Department).filter(Department.dep_id == 33)
# qset8 = session.query(Department).filter(Department.dep_id >= 3)
# dep = qset8.one()
# print(dep.dep_id,dep.dep_name)

# 如果先写的是Employees.emp_name.join的参数必须是Department
# qset9 = session.query(Employees.emp_name,Department.dep_name)
# qset9 = session.query(Employees.emp_name,Department.dep_name).join(Department)
# print(qset9.all())
# [('贾克斯', '人事部'), ('剑圣', '财务部'), ('盖伦', '运维部'), ('赵信', '开发部')]

# 如果先写的是Department.dep_name.join的参数必须是Employee
# qset9 = session.query(Employees.emp_name,Department.dep_name)
# qset9 = session.query(Department.dep_name,Employees.emp_name).join(Employees)
# print(qset9.all())
# [('人事部', '贾克斯'), ('财务部', '剑圣'), ('运维部', '盖伦'), ('开发部', '赵信')]

# qset10 = session.query(Department).filter(Department.dep_id==1)
# hr = qset10.one()
# hr.dep_name = '人力资源部'

qset11 = session.query(Department).filter(Department.dep_id==6)
market = qset11.one()
session.delete(market)

######################################################################
session.commit()
session.close()