from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta

def get_info(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track')

    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    current_utc_time = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%SZ')
    delta = timedelta(hours=2)
    min_utc_time = current_utc_time - delta
    max_utc_time = current_utc_time + delta
    valid_utc_time = min_utc_time <= current_utc_time <= max_utc_time

    if not valid_utc_time:
        return JsonResponse({'error': 'invalid UTC time'},status=400)
    
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)