
from splinter import Browser
import sys, getopt, re
from datetime import datetime
from splinter.request_handler.status_code import HttpResponseError
import time
import traceback

def main(argv):
    print 'in main' # debug

    try:
    	opts, args = getopt.getopt(argv,"i:",["file="])
        #opts, args = getopt.getopt(argv,"hi:u:",["file="])
    except getopt.GetoptError:
    	print 'pushGolden01.py  -i <file>'
       
    #sys.exit(0)
    for opt, arg in opts:
        if opt == '-h':
            print 'pushGolden01.py  -i <file>'
            sys.exit()
        elif opt in ("-i", "--file"):
            txt = arg
     
    try:
        txt
    except getopt.GetoptError:
        print 'pushGolden01.py.py  -i <file>'

    inputField = 'push message'

    #handle url input file
    try:
      file = open(txt, 'r')
    except:
        print "Open file error"
        sys.exit()

    lines = file.readlines()  
    if len(lines) == 0:
      print 'no input url'  
      sys.exit()


    with Browser() as browser:

        # login page
        browser.visit("http://forum4.hkgolden.com/login.aspx")
        time.sleep(30)

        # ---------- loop here 
        # visit web page from lines array and then input a post
        for i in range(1,1000):
          print 'loop', i  
          j = 0
          for line in lines:
              j = j + 1
              print 'line = ', line
              url = line
              browser.visit(line)   
              browser.execute_script('document.getElementById("ctl00_ContentPlaceHolder1_messagetext").value = "'+inputField+'"')                   
              time.sleep(150)
              browser.find_by_css('input[type="image"]').click()
              print 'post ', j , ' completed'
              time.sleep(150)  

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.stdout.write('\nQuit by keyboard interrupt sequence !')