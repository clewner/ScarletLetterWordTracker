from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.relative_locator import locate_with

tracker = []
addition = ""

while addition != "none":
	addition = input("Word to track (enter none when done): ")
	if(addition != "none"):
		tracker.append(addition)


url = "https://www.gutenberg.org/files/25344/25344-h/25344-h.htm"

#Would need to be replaced with directory to chromedriver on device
s = Service('C:/Users/isaac/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get(url)

paralist = driver.find_elements(By.CSS_SELECTOR, 'p')


for x in paralist:
	intpar = x.text.split("\n")
	for j in intpar:
		if(j.startswith("[") and j.endswith("]")):
			intpar.remove(j)

	wholepar = ' '.join(intpar)

	"""indices_object = re.finditer(pattern='mirror|reflect', string=wholepar, flags = re.IGNORECASE)
	indices = [index.start() for index in indices_object]
	for i in indices:
		back = 0;
		backindice = 0;
		while(True):
			if(i - back < 0):
				backindice = 0;
				break
			else:
				if(wholepar[i - back] == '.'):
					backindice = i - back
					break
				else:
					back += 1

		front = 0;
		frontindice = 0;
		while(True):
			if(i + front >= len(wholepar)):
				frontindice = len(wholepar) - 1;
				break
			else:
				if(wholepar[i + front] == '.'):
					frontindice = i + front
					break
				else:
					front += 1

		sentence = wholepar[backindice:frontindice + 1]
		while(True):
			if(sentence[0] == " " or sentence[0] == "."):
				sentence = sentence[1:]
			else:
				break
		
		print("\"" + sentence + "\"")
		print("\n")"""

	#replace this part with commented out part to just get the line instead of full paragraph
	if(any(c in wholepar for c in tracker)):
		email_locator = locate_with(By.TAG_NAME, "h4").above(x)
		title = driver.find_element(email_locator)
		print(title.text)
		print("\"" + wholepar + "\"")
		print("\n")

