
from selenium import webdriver
from openpyxl import Workbook
from openpyxl import load_workbook
import time,os
import random
from selenium.webdriver.common.keys import Keys
#导入需要使用到的数据模块
import pandas as pd
import MySQLdb

test = ""

links = []
quit = False
quit2 = False
print('starting')
#图片循环数，每次以3或4递增
#title循环数，总循环数

# open website
driver = webdriver.Firefox()
driver.get("http://www.oio.cn/")#打开网页
# driver.set_window_size(1920,1080)
driver.maximize_window()
time.sleep(2)

#------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/span/a').click()
print("click geng duo")#医院新闻


while quit == False:
	num = 1
	try:
		print("enter links")
		driver.find_element_by_xpath('//a[contains(@title,"下一页")]')#check下一页是否存在

		eles = driver.find_elements_by_xpath('//*[@class="items"]/li/a')#找到目标链接的父级

		#add links to the array
		for ele in eles:

			# print(ele.get_attribute('href'))
			links_addr = ele.get_attribute('href')
			print("click " +str(num)+ " link")

			####################################
			# write address into txt
			# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
			# 	f_txt.write('\n' + links_addr + '\n-------------------------------------------------------------------------------------------------')
			####################################
			
			links.append(links_addr)
			num+=1


		# scroll down
		# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

		#click next page
		next_page = driver.find_element_by_xpath('//a[contains(@title,"下一页")]')
		next_page.click()
		print("click next page")
	#没有下一页，完成本页链接后结束
	except:
		print("next page does not exist")
		eles = driver.find_elements_by_xpath('//*[@class="items"]/li/a[contains(@href,"/news/view/")]')

		for ele in eles:

			# print(ele.get_attribute('href'))
			links_addr = ele.get_attribute('href')
			print("click " +str(num)+ " link")

			####################################
			# write address into txt
			# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
			# 	f_txt.write('\n' + links_addr + '\n-------------------------------------------------------------------------------------------------')
			####################################
			
			links.append(links_addr)
			num+=1
			
		quit = True
		print("no more pages, start getting contents")
		print("finish first section-------------------------------------------------------------------------------------------")



#------------------------------------------------------------------------------------------------------------------
time.sleep(2)
driver.get("http://www.oio.cn/")#打开网页
time.sleep(2)

x=1
click_more_contents = driver.find_elements_by_xpath('//a[contains(@title,"更多内容")]')

for more in click_more_contents:

	more.click()
	print("click geng duo")#教育科研

	for i in range(5):
		try:
			time.sleep(2)
			driver.find_elements_by_xpath('//*[@id="links"]/li[1]/a')#check下一页是否存在
			print("open the page")
			break
		except:
			i+=1
			time.sleep(2)

	print("ready to switch tab")
	driver.switch_to_window(driver.window_handles[1])
	time.sleep(3)
	n=1


	while quit2 == False:
		try:
			print("enter links")
			driver.find_element_by_xpath('//a[contains(@title,"下一页")]')#check下一页是否存在

			eles = driver.find_elements_by_xpath('//*[@class="items"]/li/a')#找到目标链接的父级

			#add links to the array
			for ele in eles:

				# print(ele.get_attribute('href'))
				links_addr = ele.get_attribute('href')
				print("click " +str(n)+ " link")

				####################################
				# write address into txt
				# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
				# 	f_txt.write('\n' + links_addr + '\n-------------------------------------------------------------------------------------------------')
				####################################
				
				links.append(links_addr)
				n+=1


			# scroll down
			# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

			#click next page
			next_page = driver.find_element_by_xpath('//a[contains(@title,"下一页")]')
			next_page.click()
			print("click next page")
		#没有下一页，完成本页链接后结束
		except:
			print("next page does not exist")
			eles = driver.find_elements_by_xpath('//*[@class="items"]/li/a[contains(@href,"/view/")]')#sometimes the xpath for last page is different

			for ele in eles:

				# print(ele.get_attribute('href'))
				links_addr = ele.get_attribute('href')
				print("click " +str(n)+ " link")

				####################################
				# write address into txt
				# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
				# 	f_txt.write('\n' + links_addr + '\n-------------------------------------------------------------------------------------------------')
				####################################
				
				links.append(links_addr)
				n+=1
				
			quit2 = True
			print("no more pages, start getting contents")
			print("finish first section-------------------------------------------------------------------------------------------")
	x+=1
	print("go back to main page")
	driver.switch_to_window(driver.window_handles[0])
	time.sleep(3)
	quit2 = False




print("finish adding urls to the list")

for i in links:

	with open('./links.txt', 'a', encoding='utf-8-sig') as f_txt:
		f_txt.write(links_addr+ '\n')

print("finish adding to the txt file")



#选取innerhtml from link array
# next_page = driver.find_elements_by_xpath('//a[contains(@title,"下一页")]')
# next_page.click()


# wb = Workbook()
# #create a page
# page = wb.active
# #name a page
# page.title = "content1"
# #the list is waiting to be inserted
# links = ["a","b0","ada"]
# #header---first line of the spreadsheet
# header = ["content"]
# page.append(header)


# for i in links:

# 	driver.get(i)
# 	test = driver.find_element_by_xpath('//*[@id="index_content"]/div/div').get_attribute('innerHTML')

# 	# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
# 	# 	f_txt.write('\n' + test + '\n-------------------------------------------------------------------------------------------------')


# 	page.append([i])



# 	wb.save("./innerHTML1.csv")
# 	print("finishing num " + str(n)+ " url" )


# print("finish getting html")









#需要一个for loop所以可以自动定位到下一个链接

# #建立数据库连接
# db = MySQLdb.connect('localhost','root','634158Han','han1',charset='utf8')
# #获取游标对象
# cursor = db.cursor()
# #创建数据库，如果数据库已经存在，注意主键不要重复，否则出错
# # try:
# #     cursor.execute('CREATE TABLE art(Id int AUTO_INCREMENT PRIMARY KEY,Content varchar(255)');
# # except:
# #     pass


# #     print('数据库已存在！')
# sql = "insert into art1(content) values(%s)"
# cursor.execute(sql,(test,))
# print("write into mysql")
# # #插入数据语句
# # query = """insert into catering_sale (content) values (%test)"""

# # #迭代读取每行数据
# # #values中元素有个类型的强制转换，否则会出错的
# # #应该会有其他更合适的方式，可以进一步了解
# # for r in range(0, len(data)):
# #     num = data.ix[r,0]
# #     date = data.ix[r,1]
# #     sale = data.ix[r,2]
# #     values = (int(num), str(date), float(sale))
# #     cursor.execute(query, values)

# #关闭游标，提交，关闭数据库连接
# #如果没有这些关闭操作，执行后在数据库中查看不到数据 
# cursor.close()
# db.commit()
# db.close()
