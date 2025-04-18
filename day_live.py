import requests
keyword = input("검새할 키워드를 입력해주세요 :")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword



html = requests.get(url) #get요청이란 '가져와.. 내가 주소 줄테니까 사이트에 드갈수 있도록 화면을 구성하는 html, css, js 코드를 보내줘
print(html.text)