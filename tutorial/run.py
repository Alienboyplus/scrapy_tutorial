from scrapy import cmdline
import time
import os
import logging
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(
    filename='logs.log',
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        # name = 'electricity_query'
        # cmd = 'scrapy crawl {0}'.format(name)
        # # cmd = cmd + ' -o douban.csv'
        #
        # item = cmdline.execute(cmd.split())
        try:
            print
            os.system('scrapy crawl electricity_query')
        except Exception as e:
            print(e)
            # logging.info("Exception detected")+e

        logging.info("command started in "+time.asctime(time.localtime(time.time())))
        time.sleep(3600)

    # print(item['remains'])

