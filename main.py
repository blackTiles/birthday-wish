from selenium import webdriver

dvr = webdriver.Chrome()
dvr.get("http://web.whatsapp.com/")

num_of_msg = int(input('No. of wishes: '))

input('Press any key: ')
 
birthday_boy = dvr.find_element_by_xpath("//span[@title='whatsapp_username']")

birthday_boy.click()

msg_box = dvr.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for i in range(num_of_msg):
    msg_box.send_keys("Happy Birthday", i)
    dvr.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Chala Gaya")
