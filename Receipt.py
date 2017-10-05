
import urllib.request
from bs4 import BeautifulSoup

class Receipt:
    
    # 財政部官網
    request_url = 'http://invoice.etax.nat.gov.tw/'

    # 取得HTML
    htmlContent = urllib.request.urlopen(request_url).read()
    soup = BeautifulSoup(htmlContent, "html.parser")

    results = soup.find_all("span", class_="t18Red")

    subTitle = ['特別獎', '特獎', '頭獎', '增開六獎'] # 獎項
    
    months = soup.find_all('h2', {'id': 'tabTitle'})
    
    # 最新一期
    month_newst = months[0].find_next_sibling('h2').text
    # 上一期
    month_previous = months[1].find_next_sibling('h2').text
    
    
    def getWinningNumber(self) -> str :
        
        text: str = ""
        
        print("最新一期統一發票開獎號碼 ({0})：".format(self.month_newst))
        text += "最新一期統一發票開獎號碼 ({0})：".format(self.month_newst)
        for index, item in enumerate(self.results[:4]):
            print('>> {0} : {1}'.format(self.subTitle[index], item.text))
            text += '\n>> {0} : {1}'.format(self.subTitle[index], item.text)
            
        print("上期統一發票開獎號碼 ({0})：".format(self.month_previous))
        text += "\n\n上期統一發票開獎號碼 ({0})：".format(self.month_previous)
        for index2, item2 in enumerate(self.results[4:8]):
            print('>> {0} : {1}'.format(self.subTitle[index2], item2.text))
            text += '\n>> {0} : {1}'.format(self.subTitle[index2], item2.text)
        return text
    
    
if __name__ == "__main__":
    
    re = Receipt()
    test = re.getWinningNumber()
    print(test)