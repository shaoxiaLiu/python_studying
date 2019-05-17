"""
启动文件
主要包含5个方法，包括星号(“*”)分割线设置、初始化课程信息并装载入列表返回、初始化教师信息并装载入列表返回、遍历课程对象并绑定教师至课程对象的对应属性并装载入列表返回、初始化学生信息并装载入列表返回
"""
from example import Student,Teather,Course

def introduction(str):
    """
    str变量接收标题名字，使用format格式化为效果图中标题的样式，并输出，这里的*号不做数量要求
    :param str:标题名字
    :return:输出效果图中标题的样式
    """
    print('{0}{1}{0}'.format('*'*20,str))

def prepare_course():
    """
    创建课程信息初始化，并以列表形式返回所创建的8门课程对象
    :return:以列表形式返回所创建的8门课程对象
    """
    #创建字典接收课程信息
    cour_dict={"01": "网络爬虫", "02": "数据分析",
               "03": "人工智能", "04": "机器学习",
               "05": "云计算",   "06": "大数据",
               "07": "图像识别", "08": "Web开发"}
    #创建空列表
    cour_list = []
    #循环遍历字典中的数据，将课程编号和课程姓名传入课程类得到课程类的实例，空列表追加每一次的课程类实例
    for k,v in cour_dict.items():
        cour_list.append(Course(k,v))
    #返回追加后的列表
    return cour_list

def create_teather():
    """
    创建教师信息初始化，并以列表形式返回所创建的8名教师对象
    :return:以列表形式返回所创建的8名教师对象
    """
    #教师信息
    teat_list = [["T1", "张亮", "13301122001"],
                ["T2", "王朋", "13301122002"],
                ["T3", "李旭", "13301122003"],
                ["T4", "黄国发", "13301122004"],
                ["T5", "周勤", "13301122005"],
                ["T6", "谢富顺", "13301122006"],
                ["T7", "贾教师", "13301122007"],
                ["T8", "杨教师", "13301122008"]]
    #创建列表存储教师类的八个实例对象
    teather_list = []
    #将教师信息的每条数据分别传入教师类，分别使用变量接收
    for each_teah in teat_list:
        teather_list.append(Teather(*each_teah))
    #返回存储教师类的八个实例对象列表
    return teather_list


def course_to_teacher():
    """
    实现课程与教师逐一绑定（每一课程信息绑定倒叙的每一老师信息），并以列表形式返回所课程与教师的绑定结果
    :return:以列表形式返回所课程与教师的绑定结果
    """
    #创建空列表
    cour_to_teah_list = []
    # 调用课程信息初始化方法，使用变量ls_course接收
    ls_course = prepare_course()
    #调用教师信息初始化方法，使用变量ls_teacher接收
    ls_teacher = create_teather()
    #循环遍历课程信息初始化方法的长度：结合课程信息初始化方法与遍历的数字，得到课程信息初始化方法列表中的每条课程类实例，通过每条课程类实例去绑定（课程类中已定义绑定方法，直接调用即可）倒叙的每一条教师类信息，将绑定后的每条数据追加到空列表
    for cour_i in range(len(ls_course)):
        cour_to_teah_list.append(ls_course[cour_i].binding(ls_teacher[len(ls_teacher)-1-cour_i]))
    #返回追加后的列表
    return cour_to_teah_list

def create_student():
    """
    创建学生信息初始化，并以列表形式返回所创建的8名学生对象
    :return:以列表形式返回所创建的8名学生对象
    """
    # 学生信息
    stu_list = [ "小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    # 使用range取得学号列表，其中学号的范围为1000~1007
    stu_no = range(1000,1008)
    # 创建空列表
    ls_student = []
    #循环遍历学生信息的长度，将学号与（据效果图所示）倒叙的学生姓名传入学生类，得到学生类的实例，将学生类实例追加至空列表
    for stu_i in range(len(stu_list)):
        ls_student.append(Student(stu_no[stu_i],stu_list[len(stu_no)-1-stu_i]))
    #返回追加后的列表
    return ls_student

if __name__ == '__main__':
    """
    实现函数调用
    """
    #调用课程绑定教师函数
    cour_to_teat_list=course_to_teacher()
    #调用学生信息初始化函数
    ls_student=create_student()
    #调用introduction(str)，传入参数，实现效果图标题一展示
    introduction('慕课学院（1）班学生信息')
    #循环输出学生信息
    for each_stu in ls_student:
        print(each_stu)
    #调用introduction(str)，传入参数，实现效果图标题二展示
    introduction('慕课学院（1）班选课结果')
    #循环遍历课程绑定教师函数的长度，为学生初始化信息的每一对象添加绑定老师之后的课程信息
    for count,each_cour_to_teat in enumerate(cour_to_teat_list):
        ls_student[count].add_course(each_cour_to_teat)
    #遍历学生初始化信息，实现如效果图Name：xxx, Selected：[{'课程名称': 'xxx', '教师名称': 'xxx'}]的展示
    for each_stu_cour in ls_student:
        print('Name:{0},Selected:{1}'.format(each_stu_cour.s_name,each_stu_cour.cour_info))




