#
import requests
import tkinter as tk

#API dados
# Go to "https://newsapi.org/", register and generate the API key given by StopIteration
# Then insert the API link below and put the key and link for the JSON to capture the data
def getNews():
    api_key = " " # paste the site's API code here
    url = "https://newsapi.org/v2/top-headlines?country=br&apiKey="+api_key #Link that you will insert, depending on the news of the country you want to follow
    news = requests.get(url).json()

    # Dados dentro da API
    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
    
    for i in range(10):
        my_news = my_news  + str(i+1) + ". " + my_articles[i] + "\n"
    
    #print(my_news)
    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

canvas.mainloop()


# f6029f3a2c7c4fe28574fa3cb1e3fb57