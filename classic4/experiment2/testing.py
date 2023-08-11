from bs4 import  BeautifulSoup
str='sabdhsds'
print(BeautifulSoup(str, "lxml").text)