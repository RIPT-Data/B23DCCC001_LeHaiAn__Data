import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://vnexpress.net/the-gioi"

try:
    response = requests.get(url)
    response.raise_for_status() 
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all("article", class_="item-news")


    news_list = []


    for article in articles:
        title_element = article.find("h3", class_="title-news")
        link_element = article.find("a")
        summary_element = article.find("p", class_="description")
        

        if title_element and link_element and summary_element:
            title = title_element.text.strip()
            link = link_element['href']
            if not link.startswith("https"):
                link = "https://vnexpress.net" + link
            summary = summary_element.text.strip()
            news_list.append({
                "Title": title,
                "Link": link,
                "Summary": summary
            })

    if news_list:
        df = pd.DataFrame(news_list)
        
        try:
            df.to_csv("vnexpress_news.csv", index=False, encoding='utf-8-sig')
            print("Dữ liệu đã được lưu vào vnexpress_news.csv")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu file CSV: {e}")
    else:
        print("Không có bài báo nào được tìm thấy.")
    
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi gửi yêu cầu HTTP: {e}")
