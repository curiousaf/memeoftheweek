from requests_html import HTMLSession
session = HTMLSession()

def post_to_dict(element):
    video_text = 'View Comments Play 0:00 0:00 Settings Fullscreen'
    if not 'promoted•' in element.text:
        post_title = element.find('h3')[0].text
        post_details = element.text.split('}')[1].split('share')[0]
        post_comments = post_details.split()[-2]
        post_upvotes = post_details.split()[-3]
        post_text = ' '.join(post_details.split()[:-3])
        if '.com' in post_text:
            external_link = element.find('.styled-outbound-link', first=True).attrs['href']
            external_link = external_link.replace('https://www.gfycat.com/', 'https://www.gfycat.com/ifr/')
        else:
            external_link = None
        if video_text in post_text:
            post_text = post_text.replace(video_text, '') 

        if element.find('.media-element'):
            post_picture = element.find('.media-element')[0].attrs['src']
        else:
            post_picture = None
        post_dict = {'title': post_title,
                    'text': post_text,
                    'picture': post_picture,
                    'upvotes': post_upvotes,
                    'comments': post_comments,
                    'external_link': external_link}
        return post_dict

def get_subreddit(subreddit='Memes_Of_The_Dank', time='week'):
    r = session.get(f'https://www.reddit.com/r/{subreddit}/top/?t={time}')
    results = r.html.find('.Post')
    article_list = map(post_to_dict, results)
    return list(article_list)