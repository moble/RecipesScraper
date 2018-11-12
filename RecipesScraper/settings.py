"""
Scrapy settings for RecipesScraper project.
"""
# Names
BOT_NAME = 'RecipesScraper'

SPIDER_MODULES = ['RecipesScraper.spiders']
NEWSPIDER_MODULE = 'RecipesScraper.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {
    'RecipesScraper.pipelines.JsonPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"
DOWNLOAD_DELAY = 2.5  # Wait 2.5 seconds between requests; their robots.txt asks for 1, and scrapy randomizes the wait between 0.5 and 1.5 times this number

CONCURRENT_REQUESTS_PER_DOMAIN = 1
