import praw
import pandas as pd

# access app
reddit = praw.Reddit(client_id = 'c2Yc_OkVx5brqw', 
                     client_secret = 'F7Wk2ewLBYaQJNK6MNpnHH1i4ygnag', 
                     user_agent = 'memecollector')

# scraping image info
subreddit = reddit.subreddit('Memes') 
posts = subreddit.top( limit=500)

image_urls = []
image_titles = []
image_ids = []

for post in posts:
  image_urls.append(post.url)
  image_titles.append(post.title)
  image_ids.append(post.id)

df = pd.DataFrame(image_urls)
df.to_csv("urls.csv", index=False, header=False)