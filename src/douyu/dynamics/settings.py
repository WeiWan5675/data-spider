from datetime import datetime

# 文件及路径，log目录需要先建好
today = datetime.now()
log_file_path = "log/scrapy_{}_{}_{}.log".format(today.year, today.month, today.day)

# 日志输出
LOG_LEVEL = 'DEBUG'
LOG_FILE = log_file_path

BOT_NAME = "dynamics"

SPIDER_MODULES = ["dynamics.spiders"]
NEWSPIDER_MODULE = "dynamics.spiders"
ITEM_PIPELINES = {
       'dynamics.pipelines.DynamicsPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# 是否启用日志
LOG_ENABLED=True

# 日志使用的编码
LOG_ENCODING='utf-8'

# 日志文件(文件名)
LOG_FILE=None

# 日志格式
LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# 日志时间格式
LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'

# 日志级别 CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_LEVEL='DEBUG'

# 如果等于True，所有的标准输出（包括错误）都会重定向到日志，例如：print('hello')
LOG_STDOUT=False

# 如果等于True，日志仅仅包含根路径，False显示日志输出组件
LOG_SHORT_NAMES=False

