import json
import subprocess
from django.http import HttpResponse

def tweets_user(request, username: str):
    """Endpoint for retreiving tweets from users"""
    username = username.lstrip('@')
    limit = request.GET.get('limit', '30')
    if not limit.isdigit() or int(limit) == 0:
        limit = 30
    command = f'snscrape --jsonl --max-results {limit} twitter-user {username}'.split()
    tweets = run_command(command)
    result = [json.loads(tweet) for tweet in tweets]
    return HttpResponse(json.dumps(result), content_type='application/json')


def tweets_hashtag(request, hashtag: str):
    """Endpoint for retreiving tweets by hashtags"""
    hashtag = hashtag.lstrip('#')
    limit = request.GET.get('limit', '30')
    if not limit.isdigit() or int(limit) == 0:
        limit = 30
    command = f'snscrape --jsonl --max-results {limit} twitter-hashtag {hashtag}'.split()
    tweets = run_command(command)
    result = [json.loads(tweet) for tweet in tweets]
    return HttpResponse(json.dumps(result), content_type='application/json')


def run_command(command):
    """Function for running commands"""
    proc = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(proc.stdout.readline, b'')
