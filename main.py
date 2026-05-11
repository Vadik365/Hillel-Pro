import requests
from bs4 import BeautifulSoup


def scrape_news():
    url = "https://habr.com/ru/articles/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Connection completed! Status: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find_all("a", class_="tm-title__link")

        articles_list = []

        for title in titles:
            # Исправляем ошибки с переменными и атрибутами
            text = title.text.strip()
            link = "https://habr.com" + title.get("href")

            articles_list.append({"title": text, "link": link})

        return articles_list
    else:
        print(f"Error connected: {response.status_code}")
        return None


# Вызываем функцию и сохраняем результат
news_data = scrape_news()

# Если данные получены, записываем их в файл
if news_data:
    with open("news.txt", "w", encoding="utf-8") as file:
        for idx, item in enumerate(news_data, 1):
            file.write(f"{idx}. {item['title']}\n")
            file.write(f"   Link: {item['link']}\n\n")
    print("Результаты успешно сохранены в файл news.txt!")
