# Scrapy settings for scrapytest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html

BOT_NAME = 'scrapytest'

SPIDER_MODULES = ['scrapytest.spiders']
NEWSPIDER_MODULE = 'scrapytest.spiders'

ITEM_PIPELINES = ["scrapytest.scrapymongodb.MongoDBPipeline"]

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapytest (+http://www.yourdomain.com)'
