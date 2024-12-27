from selenium.webdriver.chrome.options import Options
from django.conf import settings

def configure_proxy():
    
    chrome_options = Options()
    
    # proxyMesh Credentials
    PROXY_HOST = settings.PROXY_HOST
    PROXY_PORT = settings.PROXY_PORT
    PROXY_USER = settings.PROXY_USER
    PROXY_PASS = settings.PROXY_PASS
    
    chrome_options.add_argument(f'--proxy-server=http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}')
    
    return chrome_options

def configure_twitter():
    # twitter Credentials
    return settings.TWITTER_USERNAME, settings.TWITTER_PASSWORD