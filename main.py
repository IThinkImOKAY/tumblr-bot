import pytumblr
import time
from halo import Halo

client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)

tags = ['your', 'tags', 'to', 'follow', 'and', 'like']

while True:
    try:
        for tag in tags:
            for item in client.tagged(tag):
                client.like(item["id"] , item["reblog_key"])
                print("Liked: " + item["blog_name"] + ".tumblr.com")
                client.follow(item["blog_name"] + ".tumblr.com")
                print("Followed: " + item["blog_name"] + ".tumblr.com")
        
    except Exception as e:
        print(e)
        time.sleep(60)
        
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
