from flask import Flask, render_template
from reddit_scrape import get_subreddit
app = Flask(__name__)

#meme_list = [{'title': '😳', 'text': '', 'picture': 'https://preview.redd.it/vdehkkmk20651.jpg?width=640&crop=smart&auto=webp&s=3e078fdffacee21d8859d896b20c75013889c133', 'upvotes': '11.2k', 'comments': '95'}, {'title': 'Dats rite!', 'text': '', 'picture': 'https://preview.redd.it/37nqhpjja9551.jpg?width=640&crop=smart&auto=webp&s=0cd6e83fbee34a4db9732c2f6f1eb0e899bbb967', 'upvotes': '10.5k', 'comments': '65'}, {'title': 'Unicorn are real', 'text': '', 'picture': 'https://preview.redd.it/vfrd59gry7651.jpg?width=640&crop=smart&auto=webp&s=3672460b6acf8a148d6da31c89f4d289371b53c8', 'upvotes': '9.0k', 'comments': '77'}, {'title': "Hehe... I'm in danger", 'text': '', 'picture': 'https://preview.redd.it/ujm1517jij551.jpg?width=640&crop=smart&auto=webp&s=bda8319d83317a5412a56542db44e41f46ec0662', 'upvotes': '7.3k', 'comments': '104'}, {'title': 'Han SoHigh lol', 'text': '', 'picture': 'https://preview.redd.it/1t2521j9bb651.jpg?width=640&crop=smart&auto=webp&s=c47e1943e662521d873aff722e7bf57312fa94fc', 'upvotes': '8.1k', 'comments': '42'}, {'title': 'Facts', 'text': '', 'picture': 'https://preview.redd.it/7q3xdq7anq551.png?width=640&crop=smart&auto=webp&s=7429109785c1cb7794ab3c2e5249bf6186f96a70', 'upvotes': '6.6k', 'comments': '124'}, {'title': 'Eeeeeeeee', 'text': '', 'picture': 'https://preview.redd.it/4ndlvdy8rc551.jpg?width=640&crop=smart&auto=webp&s=1f2489bf7338923dfcb7883100bde7306224878e', 'upvotes': '6.4k', 'comments': '60'}, {'title': 'Suffering cleans the soul', 'text': '', 'picture': 'https://i.redd.it/n5ewpwqrjg551.png', 'upvotes': '5.6k', 'comments': '30'}]

@app.route("/")
def hello():
    meme_list=get_subreddit(subreddit='interestingasfuck')
    print(meme_list)
    return render_template('index.html', meme_list=meme_list)

if __name__ == '__main__':
    app.run(debug=True)