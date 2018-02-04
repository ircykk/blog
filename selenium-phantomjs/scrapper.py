from selenium import webdriver
import time
import urllib.request

def get_url(url):
	# Inicjalizujmey selenium z silnikiem PhantomJS
	driver = webdriver.PhantomJS()

	# Ustawiamy rozdzielczość - opcjonlanie potrzebne do screenshotów
	driver.set_window_size(1024, 768)

	# Wczytujemy podany adres URL
	driver.get(url)

	# Czekamy kilka sekund na załadowanie strony
	time.sleep(5)

	try:
		# Znajdujemy element na stronie przez XPATH i klikamy
		driver.find_element_by_xpath("//*[@id='player']/div[5]/div").click()
		
		# Znów czekamy na załadowanie np. AJAX
		time.sleep(5)

		# Wyszukujemy elemnt, kopiujemy atrybut etc.
		src = driver.find_element_by_xpath("//*[@id='player']/video[1]").get_attribute("src")
	
		return src

	except Exception:
		debug(driver)
		driver.close()
		return False

	# Zamykamy połącznie
	driver.close()

	return src

def debug(driver):
	# Zapisujemy screenschot
	driver.save_screenshot('screenshot.png');

	# Zapisujemy HTML do pliku
	page = driver.page_source
	file_ = open('page.html', 'w')
	file_.write(page)
	file_.close()


# Wykonujemy
url = get_url("http://www.kreskowkazone.pl/odcinki-online_simpsonowie-1989_603")
if url != False:
	print(url)
else:
	print("Błąd!")