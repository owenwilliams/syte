
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'owenwilliamsnz.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'KAAha84EG32WK6GKrO8BHOCeUQPXNsnZfAKcDNqbPnDtN5J8Yq'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&count=50&screen_name='
TWITTER_CONSUMER_KEY = 'rR028aGExAfff4MTpSDbg'
TWITTER_CONSUMER_SECRET = 'e1bFLjLNNkGRGWF0pfwaTqqYtDEKe3qvLUPmkbGG8I'
TWITTER_USER_KEY = '14767730-3AgE9HQw26VMjJlinw5Lk3QbxlwJp6ECfHwlD6Had'
TWITTER_USER_SECRET = 'ErIQgucnrylzGC7q2a8nwm2DtpA3G3Fo61JUVYd0xk'


#Github Integration
GITHUB_INTEGRATION_ENABLED = False
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '[ENTER GITHUB ACCESS TOKEN HERE, SEE GITHUB SETUP INSTRUCTIONS]'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = '[ENTER GITHUB CLIENT ID HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_CLIENT_SECRET = '[ENTER GITHUB CLIENT SECRET HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '14131996.33dcbda.6092250f5dc441e88656087dec37e457'
INSTAGRAM_USER_ID = '14131996'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = '33dcbda42d354876a722e0bd0372f991'
INSTAGRAM_CLIENT_SECRET = 'cdbcf2d4d41e40eb8c3e34678201e01d'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-32240332-1'


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = True
DISQUS_SHORTNAME = 'owened'



if DEPLOYMENT_MODE == 'prod':
    SITE_ROOT_URI = 'http://freezing-snow-2048.herokuapp.com/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://freezing-snow-2048.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
