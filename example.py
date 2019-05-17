"""
描述信息文件
example.py主要完成相关类的定义
自定义学生信息、课程信息、教师信息三者的具体描述(三个类)
"""

class Student(object):
    """
    学生类
    """

    def __init__(self,s_number,s_name,cour_info = []):
        """
        实例化对象时参数的初始化
        :param s_number: 学生的学号
        :param s_name: 学生的姓名
        :param cour_info: 已选课程（默认值为空列表）
        """
        self.s_number = s_number
        self.s_name = s_name
        # 如果不用copy()，那么该类的不同对象的self.cour_info属性都将指向同一个变量，也就是该类的不同对象的self.cour_info值都会相等
        self.cour_info = cour_info.copy()


    def add_course(self,cour_info):
        """
        添加课程信息（cour_info）至学生对象的已选课程属性
        :param cour_info: 课程信息
        :return: 添加课程信息（cour_info）至学生对象的已选课程属性
        """
        self.cour_info.append(cour_info)


    def __str__(self):
        """
        设置学生类信息的字符串显示方法，返回如效果图所示学生信息表的学生姓名，学生学号
        :return: 返回如效果图所示学生信息表的学生姓名，学生学号
        """
        return ('name:{0},s_number:{1}'.format(self.s_name,self.s_number))


class Teather(object):
    """
    教师类
    """

    def __init__(self,t_number,t_name,t_phone):
        """
        实例化对象时参数的初始化
        :param t_number: 教师编号
        :param t_name:教师姓名
        :param t_phone:手机号码
        """
        self.t_number = t_number
        self.t_name = t_name
        self.t_phone = t_phone


    def __str__(self):
        """
        设置教师类信息的字符串显示方法，返回教师编号与教师姓名属性
        :return: 输出教师编号与教师姓名属性
        """
        return ("t_number:{0},t_name:{1}".format(self.t_number,self.t_name))


class Course(object):
    """
    课程类
    """

    def __init__(self,c_number,c_name,teather = None):
        """
        实例化对象时参数的初始化
        :param c_number:课程编号
        :param c_name:课程名称
        :param teather:授课教师（teacher默认值为None）
        """
        self.c_number = c_number
        self.c_number = c_name
        self.teather = teather

    def binding(self,teacher):
        """
        实现课程绑定授课教师功能
        :param teacher:教师类的实例
        :return:判断教师类的实例是否存在，如果存在,则返回{'课程名称': 'xxx', '教师名称': 'xxx'}；反之，则返回空
        """
        self.teather = teacher
        if isinstance(self.teather,Teather):
            return {'课程名称':self.c_number,'教师名称':self.teather.t_name}
        else:
            return ''


    def __str__(self):
        """
        设置教师类信息的字符串显示方法，返回教师编号与教师姓名属性
        :return: 输出教师编号与教师姓名属性
        """
        return ("c_number:{0},c_name:{1}".format(self.c_number,self.c_name))


