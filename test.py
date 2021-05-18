from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])#开发者模式
options.add_argument("--disable-blink-features=AutomationControlled")#禁用启用Blink运行时的功能
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
    })#再次覆盖window.navigator.webdriver的值

策略 = "一字板,涨停原因，最新涨停封单额，最新涨停封单量，涨停开板次数，涨停封成比，涨停封流比，连续涨停次数，首次涨停时间，最后涨停时间，流通盘，流通市值，上市天数，行业，首次封单量，占实际流通比，占成交量比，最高封单量，占实际流通比，占成交量比"
url = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=" + 策略
driver.get(url)

print(driver.page_source)