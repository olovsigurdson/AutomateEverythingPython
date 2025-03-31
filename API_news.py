#20af8fc92d854885b056eabb3a82a073

import requests
API_KEY = "20af8fc92d854885b056eabb3a82a073"

def get_news(country='se', category='business'):
    r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
    json_content = r.json()

    for i in range(len(json_content.get('articles'))):
        print(json_content.get('articles')[i].get("author"), ' \n ', json_content.get('articles')[i].get("title"))
        print("**************")


def get_top_news_category():
    categories = ['business','entertainment','general','health','science','sports','technology']
    for category in categories:

        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}")
        json_content = r.json()
        print(f"******{category}******")
        print(json_content.get('articles')[0].get("author"), ' \n ', json_content.get('articles')[0].get("title"))
        #print(json_content.get('articles')[0]["author"], ' \n ', json_content.get('articles')[0].get("title"))
        print("**************")


#get_top_news_category()
get_news()