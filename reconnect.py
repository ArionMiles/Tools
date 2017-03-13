from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
	print (" [#] Initializing...")
	driver = webdriver.PhantomJS("phantomjs.exe") ## Create a new instance of the PhantomJS driver ##

	## Navigate to Router page ##
	print (" [#] Opening router page...")
	driver.get("http://admin:pass@192.168.0.1")

	time.sleep(10) ## Wait for 5 seconds ##
	driver.switch_to_frame(driver.find_element_by_name("bottomLeftFrame")) ## Switch the frames ##
	driver.find_element_by_id("a3").click(); ## Navigate to Network Tab ##
	driver.switch_to_default_content(); ## Switch back to the "default content" (that is, out of the frames) ##

	def reconnect():
		## Disconnect ##
		print (" [#] Disconnecting...")
		driver.find_element_by_name("Disconnect").click();
		driver.switch_to_default_content()

		## Reconnect ##
		print(" [#] Reconnecting after sleeping for 5s...")
		time.sleep(5) ## Wait for 5 seconds ##
		driver.switch_to_frame(driver.find_element_by_name("mainFrame"))
		driver.find_element_by_name("Connect").click();
		driver.switch_to_default_content()
		status()

	def status():
		print(" [#] Checking status...")
		time.sleep(10) ## Wait for 10 seconds ##
		driver.switch_to_frame(driver.find_element_by_name("mainFrame"))
		linkStat = driver.find_element_by_id("linkStat");
		stat = linkStat.text;
		t_connect = "Connecting...";
		t_connect2 = "Disconnected!";
		if stat == t_connect: 
			print (" [-] Connection error. Reconnecting...");
			reconnect()
		elif stat == t_connect2:
			print (" [!] Disconnected! Connecting now...");
			reconnect()
		else:
			print " [+] " + stat;
	status()
except KeyboardInterrupt:
	print (" [!] Operation terminated!")

driver.quit() ## Exit ##