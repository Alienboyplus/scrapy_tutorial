from scrapy import cmdline
import time
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        # name = 'electricity_query'
        # cmd = 'scrapy crawl {0}'.format(name)
        # # cmd = cmd + ' -o douban.csv'
        #
        # item = cmdline.execute(cmd.split())
        try:
            os.system('scrapy crawl electricity_query')
        except Exception as e:
            print(e)

        time.sleep(3600)

    # print(item['remains'])

