'''Import selenium, time & argparse'''
from selenium import webdriver
import time
import argparse

PARSER = argparse.ArgumentParser(description="TL-WR740N CLI Tool by Kanishk Singh.")
PARSER.add_argument('-reconnect', '-r', type=str, help="Reconnect", required=False, default="")
ARGS = PARSER.parse_args()

try:
    print " [#] Initializing..."
    DRIVER = webdriver.PhantomJS("phantomjs.exe") # Create a new instance of the PhantomJS DRIVER

    # Navigate to Router page
    print " [#] Authenticating..."
    DRIVER.get("http://admin:notadmin@192.168.0.1")

    time.sleep(5) # Wait for 5 seconds
    DRIVER.switch_to_frame(DRIVER.find_element_by_name("bottomLeftFrame")) # Switch the frames
    DRIVER.find_element_by_id("a3").click() # Navigate to Network Tab
    DRIVER.switch_to_default_content() # Switch back to the "default content" (out of the frames)


    def reconnect():
        '''Disconnect'''
        print " [#] Disconnecting..."
        DRIVER.find_element_by_name("Disconnect").click()
        DRIVER.switch_to_default_content()

        ## Reconnect ##
        print " [#] Reconnecting after sleeping for 5s..."
        time.sleep(5) ## Wait for 5 seconds ##
        DRIVER.switch_to_frame(DRIVER.find_element_by_name("mainFrame"))
        DRIVER.find_element_by_name("Connect").click()
        DRIVER.switch_to_default_content()
        status()

    def status():
        '''Check status'''
        print " [#] Checking status..."
        time.sleep(10) ## Wait for 10 seconds ##
        DRIVER.switch_to_frame(DRIVER.find_element_by_name("mainFrame"))
        linkStat = DRIVER.find_element_by_id("linkStat")
        stat = linkStat.text
        t_connect = "Connecting..."
        t_connect2 = "Disconnected!"
        if stat == t_connect or stat == t_connect2:
            print " [-] Connection error. Reconnecting..."
            reconnect()
        else:
            print " [+] " + stat

    def reconnect2():
        '''Force reconnect'''
        print " [#] Force reconnecting..."
        time.sleep(10) ## Wait for 10 seconds ##
        DRIVER.switch_to_frame(DRIVER.find_element_by_name("mainFrame"))
        print " [#] Disconnecting..."
        DRIVER.find_element_by_name("Disconnect").click()
        DRIVER.switch_to_default_content()
        ## Reconnect ##
        print " [#] Reconnecting after sleeping for 5s..."
        time.sleep(5) ## Wait for 5 seconds ##
        DRIVER.switch_to_frame(DRIVER.find_element_by_name("mainFrame"))
        DRIVER.find_element_by_name("Connect").click()
        DRIVER.switch_to_default_content()
        status()

    if ARGS.reconnect == "t":
        reconnect2()
    else:
        status()

except KeyboardInterrupt:
    print " [!] Operation terminated!"

DRIVER.quit() # Exit
