# print()  打印  字符串要用''或""括起来
# print('hello world')

# input()  输入

# format 增强的格式化字符 串函数
# "苹果的的钱是:{};葡萄的钱是:{}总花费:{}" .format(apple , grape ,total)
# print (f'{a}')  f 是格式化，跟大括号可以输入变量 

# 变量 ：代表某个值的名称
	# 变量名命规范
	# 1.标识符的第一个字符必须是字表表中的字线（大写戒小写）或者一下下划线
	# 2.标识符的其他以由字母（大写或小写），下划线 "_" ,或 数字0-9组成
	# 3.标识符名称是对大小写敏感的
# apple_price = 10  # 苹果单价

# 语法糖，交换变量   
# a = 10
# b = 20
# a,b = b,a
# print("a is {} , b is {}".format(a,b))

# round(100/3 , 3)  # 100除以3，保留小数字后3位，不写3的话，不保留小数点后

# 变量类型
	# python 是一种动态类型语言，一个变量是什么类型，要看程序在运行中变量所代表的值是什么
	# var = 10  # 
	# type(var) # type可以查看变量的类型 当前的类型int
	# var = 'hello'  
	# type(var) # 这时var的类型是str类型
	# 1、字条串 str
		#字符串可以用双引号，也可以用单引号。通过单、双引号的恰当使用，可以
		#避免不必要的转义(escape),也就是说，可以避免使用 \ (转义字符)
		#字符串是不可变类型的变量 
			#字符串可以使用运算符 + 和 *
			# 'nihao' + 'mr' # 结果是 'nihao mr'
			# 'nihao' * 10  # 结果是 'nihao niaho nihao ...' 
		#切片
			# line = 'huan ying dajia lai wan'   # 取前十个字符
			# line[:10]  取0到10
			# line[0:10:2] 取0到10，每隔一个取一个
			# line[-10:] 取后10个字符
			# line[::1]  翻转字符
		# 字符串 函数
			# line.capitalize() # 把第一个字符大写，其它全部小写
			# line.upper() # 全部大写
			# line.lower() # 全部小写
			# line.istitle() # 是不是标题
			# line.strip() # 去除字符中左右两侧的空格的制表符
			# line.rstrip() # 只除去右边
			# line.lstrip() # 只除去左边
			# line.swapcase() # 将字符串中的大小写进去反转，大写的变小写，小写的变大写
			# line.center(20,'%')   # 传入一个参数，用%补齐，line居中，line的数够就不补
			# line.count('A')   # 计数 。传入一个字符，查看在line中有多少个。
			# line.endswith('wan')  # 是否以些结尾 对为Ture
			# line.startswith('huan') # 是束以这些字符开头 ，是就返回Ture
			# line.find('y',3)  # 返回找到的第一个y的下标，没有返回-1,从第三个字符可以找
			# line.index('d') # 返回找到的第一个d的下标，没有会报错 


	# 2、数字 int float complex ...
	# 3、列表 list
		# 列表可以容纳任意类型的对象，任意数量的对象 【重点】列表是可变类型的
		# 列表是一种容器型的序列；字符串是一种扁平型的序列
		# varibals = []      # 创建一个空列表 
		# varibals = list()  # 创建一个空列表
		# varibals = [1,2,3,'nihao','hello,world',[],[100,100]] 
			# len(varibals) 查看当前列表的长度
			# varibals.append(1) # 往表里加一个1的元素
			# varibals.clear()   # 清除表内容
			# newvaribals = varibals.copy ()     # 深复制
			# copy当前列表到一个新的地址 ，操作任何一个都不会影响另外一个
			# newvaribals = varibals      # 浅复制
			# 只把varibals的内存地址交给我new，这里对那个操作，另一个都会变化 
			# a = [1,2]
			# b = [3,4]
			# a+b   # 结果是a = [1,2,3,4]
			# a.extend(b) 把b加到a的后面 a =[1,2,3,4,3,4]
			# a.insert{0,100} 把100加到下标0的位置 a = [100,1,2,3,4,3,4,] 
			# a.pop(0)  把传入下标位置，的值弹出 a =[100,1,2,3,4,3,4,],不传参数会弹出最后一个
			# a.remove['2'] 删除列表中的2，如果2不存在，则报错
			# a.sort()排序  从小到大排序
			# a.sort(reverse = True) 反转排序

	# 4、元组 tuple
		# 是一个不可变的列表
		# var = tuple{}
		# var = ()
		# type(var)

	# 5、字典 dict
		# var = {}
		# var = dict()
		# type(var)
		'''var = {
			'中':100,
			'国';200,
			}
		'''
		# var['中']  返回 100 
		# dict中的数据成对存储，左面的是Key，右边的是值。
		# 列表可以通过，zip()函数来整合 ,也叫拉锁函数
		# words = ['中','左']
		# location = [100,200]
		# location = [words.indx('中')]
		# new_var = list(zip(words,location))
		# 把words和location 合并在一起，转换成列表赋值给new_var
		# dict(new_var)    # 把new_var转换成列表

		# students = ['zhao','qian','sun','li']
		# dict.fromkeys(students,10) 
		# fromkeys函数可以把给列表中所有key设置一个值,10
		# 结果是{'zhao':10 ,'qian':10,'sun':10,'li':10}

		# 访问
		# print(students)  # 显示students的key和值
		# students['wang']
		# 可以使用函数get,有就返回，没有就创建
		# students.get['zhou','100']
		# students.keys()   # 显示students里的所有key
		# students.values() # 显示值 ，
		# students.pop('zhao') #删除 zhao
		# students.['zhao'] = 100 加入zhao的key 值是100



# 数据类型
	# 数值类
		# min(10,12,234,100,1)   找到最小值  1
		# max(10,12,234,100,1)   找到最大值  100
		# sum(10,12,234,100,1)   求和 357
		# ** 3**10    乘方  3的10次方
		# + - * /     加减乘除
		# % 模余（C里要取余）  10%3  结果是1  6#2 结果是0 
	# bool型  布尔型
		# True   真  值是1   True == 1
		# False	 假  值是0   False== 0
		#运算符
			# and  与运算，两个条件都要是真才是真
			# or   或运算，两个条件有一个为真就为真
			# not  非运算，取反
		#操作符
			# <		小于
			# > 	大于
			# ==	等于
			# !=    不等于
			# >=    大于等于
			# <=    小于等于
			# is    是相同对象

# len()	   查看长度，可用于列表，元组，字典
# type (a)  查看a的类型
# id (a)  查看内存ID
# del()    删除


# a = 1   #把1赋值给a ,1是int 类型
# print (type(a))

# a = 'hello'  #把hello赋值给a 类型是str
# print (type(a))  

# a = [1,2,3]   #新建列表,赋值给a，列表的类型是list
# print(type(a))

# a = (1,2,3)   #元组（数据不可改变），新建元组,赋值给a，无组的类型是tuple
# print(type(a))

# a = {'key''1','name1','2'}   #字典（也叫键值对，注意KEY不可重复）类型是set
# a = dict(key = 'aa' , name = 'yy') #使用dict函数创建字典，类型是dict
# a = dict([('key','1'),('name','yy')] ) #双值子序列可以转换成字典
# print(a,type(a))

# def a(b , c) #定义一个函数
# def a(*b)  #可传入任意数量的实参，不能传入关键字参数，只能有一个
# def a(**b) #可传入任意娄量不限参数的的实参，必须也在最后

### mysql数据库的基本操作

#链接数据库
# mysql -u root -p
# u 是用户名 p:需要用密码登录数据库

# 查看数据库
# show databases;

# 选择数据库
# use database_name

# 查看数据库中的table表
# show tables;

# 查看表格结构
# desc tables;

# 查看表中的数据 
# select #from table_name;

# 查看数据并限制数量
# select * from table_name limit 10;

