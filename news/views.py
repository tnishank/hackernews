from django.conf import settings
from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import unirest
from dbapi import create_entry, create_entry_bulk



@api_view(['GET'])
def index(request):
    stories = []
    article = {}
    response = unirest.get(settings.TOP_STORIES_URL,
      headers={
        "X-Mashape-Key": settings.HN_API_KEY,
        "Accept": "application/json"
      }
    )
    # pdb.set_trace()
    for i in range(5):

        detail = unirest.get(settings.ARTICLE_URL %response.body[i],
          headers={
            "X-Mashape-Key": settings.HN_API_KEY,
            "Accept": "application/json"
          }
        )
        article['username'] = detail.body['by'].encode("utf-8")
        article['title'] = detail.body['title'].encode("utf-8")
        try:
            article['URL'] = detail.body['url'].encode("utf-8")
        except: pass
        article['score'] = detail.body['score']
        article['sentiment'] = find_sentiment(detail.body['title'])
        stories.append(article.copy())
        article.clear()

    create_entry_bulk(stories)
    return Response(stories)


def find_sentiment(text):
    sentiment = unirest.post(settings.SENTIMENT_URL,
      headers={
        "X-Mashape-Key": settings.HN_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      },
      params={
        "text": text
      }
    )
    return sentiment.body['type'].encode("utf-8")