from openpyxl import Workbook
from openpyxl import load_workbook
from selenium import webdriver
import time,os




fo3 = open("./links.txt", "r", encoding='utf-8-sig')

title_line = fo3.readlines()

wb = Workbook()
#create a page
page = wb.active
#name a page
page.title = "content1"
#the list is waiting to be inserted
links = []

#header---first line of the spreadsheet
header = ["EyeTitle", "EyeSource", "EyeLabel", "EyePublishDateTime", "EyePicURLList", "EyeContent", "EyeHtmlURL"]
page.append(header)

driver = webdriver.Firefox()


for line in title_line:
	line = line.strip()
	links.append(line)
	print(line)

  # `EyeTitle` TEXT NULL COMMENT '标题',
  # `EyeSource` TEXT NULL COMMENT '来源',
  # `EyeLabel` TEXT NULL COMMENT '标签，分号隔开',
  # `EyePublishDateTime` VARCHAR(45) NULL COMMENT '发布时间',
  # `EyePicURLList` TEXT NULL COMMENT '图片URL列表，分号隔开',
  # `EyeContent` TEXT NULL COMMENT '网页内容',
  # `EyeHtmlURL` TEXT NULL COMMENT '网页链接'




for i in links:

	driver.get(i)
	#test = driver.find_element_by_xpath('//*[@id="index_content"]/div/div').get_attribute('innerHTML')
	#get author
	author = driver.find_element_by_xpath('//*[@id="index_content"]/div/div/div/span[2]').text
	print(author)

	#get publish date
	publish_date = driver.find_element_by_xpath('//*[@id="index_content"]/div/div/div/span[3]').text
	print(publish_date)
	

	#get title
	title = driver.find_element_by_xpath('//*[@id="index_content"]/div/div/h3').text
	print(title)
	

	#get tag
	tag = driver.find_element_by_xpath('//*[@id="index_content"]/div/h4/a[2]').text
	print(tag)
	
	




	#get img links
	image = driver.find_elements_by_xpath('//img[contains(@src,"/uploadfiles/images")]')
	img_links = ""
	for j in image:
		image_link = j.get_attribute("src")
	#imgs = driver.find_element_by_xpath('//*[@id="index_content"]/div/div/p[3]/span/img').get_attribute("src")
		img_add_name = image_link +";\n"
		img_links += img_add_name

	print(img_links)

		
	

	#get content
	content = driver.find_element_by_xpath('//*[@id="index_content"]/div/div').get_attribute('innerHTML')
	content = str(content)
	abc = content.replace('/uploadfiles', 'http://www.oio.cn/uploadfiles')

	print("get content\n" + abc)



	website_source = "天津市眼科医院"

	# with open('./innerHTML.txt', 'a', encoding='utf-8-sig') as f_txt:
	# 	f_txt.write('\n' + test + '\n-------------------------------------------------------------------------------------------------')


	page.append([title, website_source, tag, publish_date, img_links, abc, i])


	wb.save("./innerHTML1.csv")
	print("finishing num " + str(i)+ " url" )


print("finish getting html")
