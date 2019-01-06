from base.testBase import ParametrizedTestCase as pt
import time

class testHome(pt):
    def test_home(self):
        time.sleep(1)
        self.driver.get('http://172.16.5.162:8080/mpr/testurl.html')
        self.driver.find_element_by_xpath('/html/body/div[8]/a[1]').click()
        time.sleep(1)

    def test_1(self):
        time.sleep(1)
        self.driver.get('http://172.16.5.162:8080/mpr/testurl.html')
        self.driver.find_element_by_xpath('/html/body/div[8]/a[1]').click()
        time.sleep(1)