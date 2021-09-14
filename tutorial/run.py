from scrapy import cmdline

# name = 'douban_movie_top250'
name = 'douban_ajax'
cmd = 'scrapy crawl {0}'.format(name)
cmd = cmd + ' -o douban.csv'

cmdline.execute(cmd.split())