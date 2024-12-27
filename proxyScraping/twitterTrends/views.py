from django.shortcuts import render
from .utils.login_to_twitter import login_to_X
from .utils.scrape_top_trends import scrape_top_trends_from_X
from .utils.save_to_database import store_trends_in_DB
from .utils.cred_helpers import configure_proxy,configure_twitter
from django.http import JsonResponse

def index(request):
    return render(request, 'home.html')

def trends(request):
    try:
        configure_proxy()
    
        TWITTER_USERNAME, TWITTER_PASSWORD = configure_twitter()

        driver = login_to_X(TWITTER_USERNAME,TWITTER_PASSWORD)

        if not driver:
            return JsonResponse({
                "error": "Login to X failed"
            }, status=500)

        trends = scrape_top_trends_from_X(driver)

        if not trends:
            return JsonResponse({
                "error": "Scarping Trends Failed"
            }, status=500)

        upload_in_Mongo = store_trends_in_DB(trends)

        if not upload_in_Mongo:
            return JsonResponse({
                "error": "Upload to database failed"
            }, status=500)
            
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {e}"}, status=500)
    
    finally:
        if 'driver' in locals() and driver:
            driver.quit()
    
    return render(request, 'trends.html', {})
