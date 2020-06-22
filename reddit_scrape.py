from requests_html import HTMLSession
session = HTMLSession()

def post_to_dict(element):
    video_text = 'View Comments Play 0:00 0:00 Settings Fullscreen'

    if not 'promoted•' in element.text:
        post_dict = {
            'title': None,
            'text': None,
            'picture': None,
            'upvotes': None,
            'comments': None,
            'external_link': None,
            'gfycat_link': None,
            'imgur_link': None,
            'reddit_video': None,
            'youtube_id': None
            }

        post_dict['title'] = element.find('h3')[0].text
        post_details = element.text.split('}')[1].split('share')[0]
        post_dict['comments'] = post_details.split()[-2]
        post_dict['upvotes'] = post_details.split()[-3]
        post_dict['text'] = ' '.join(post_details.split()[:-3])
        if '.com' in post_dict['text']:
            try:
                post_dict['external_link'] = element.find('.styled-outbound-link', first=True).attrs['href']
            except:
                post_dict['external_link'] = 'Fail'
            if 'gfycat' in post_dict['external_link']:
                post_dict['gfycat_link'] = post_dict['external_link'].replace('https://gfycat.com/', 'https://www.gfycat.com/ifr/')
            elif 'imgur' in post_dict['external_link']:
                #post_dict['imgur_link'] = post_dict['external_link'].split('https://i.imgur.com/')
                post_dict['imgur_link'] = element.find('.styled-outbound-link', 
                                            first=True).search(
                                            'https://i.imgur.com/{img_id}.gifv')['img_id']

            elif 'youtube' in post_dict['external_link']:
                post_dict['youtube_id'] = post_dict['external_link'].split('?v=')[1]
        
        if element.find('video', first=True):
            post_dict['reddit_video'] = element.find('video', first=True).html
        if video_text in post_dict['text']:
            post_dict['text'] = post_dict['text'].replace(video_text, '') 

        if element.find('.media-element'):
            post_dict['picture'] = element.find('.media-element')[0].attrs['src']


        return post_dict

def get_subreddit(subreddit='Memes_Of_The_Dank', time='week'):
    r = session.get(f'https://www.reddit.com/r/{subreddit}/top/?t={time}')
    results = r.html.find('.Post')
    article_list = map(post_to_dict, results)
    return list(article_list)