import requests
import webbrowser

search_query = input("Enter what you would like to search: ")

url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + search_query

headers = {
    'x-rapidapi-key': "f55fa8515dmshf2b33af07a16bbap100188jsnd2dd3cf1899d",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)


results_string = response.text
index_link_start = results_string.find("link")
index_link_end = results_string.find(",", index_link_start)
link_string = results_string[index_link_start:index_link_end]
# print(link_string) prints: link":"https://bitcoin.org/"

link_string = link_string.strip('link":"')
link_string = link_string.strip('"')



# print(response.text) prints:

# {"results": [{"title": "Bitcoin - Open source P2P money",
# "link": "https://bitcoin.org/", "description":
# "Bitcoin uses peer-to-peer technology to operate with no central authority or banks​;
# managing transactions and the issuing of bitcoins is carried out collectively by ...",
# "g_review_stars": "Bitcoin uses peer-to-peer technology to operate with no central authority or banks​;
# managing transactions and the issuing of bitcoins is carried out collectively by ..."},
# {"title": "Bitcoin Price | BTC Price Index and Live Chart — CoinDesk 20", "link": "https://www.coindesk.com/price/bitcoin",
# "description": "Bitcoin was the first cryptocurrency to successfully record transactions on a secure,
# decentralized blockchain-based network. Launched in early 2009 by its ...","g_review_stars":
# "Bitcoin was the first cryptocurrency to successfully record transactions on a secure,
# decentralized blockchain-based network. Launched in early 2009 by its ..."},{"title":
# "Bitcoin - Wikipedia", "link": "https://en.wikipedia.org/wiki/Bitcoin", "description":
# "Bitcoin(₿) is a cryptocurrency invented in 2008 by an unknown person or group of
# people using the name Satoshi Nakamoto. The currency began use in 2009 when its
# implementation was released as open-source software.","g_review_stars":"Bitcoin(₿)
# is a cryptocurrency invented in 2008 by an unknown person or group of people using the name
# Satoshi Nakamoto. The currency began use in 2009 when its implementation was released as
# open-source software."},{"title":"Bitcoin(@Bitcoin) · Twitter","link":
# "https://twitter.com/Bitcoin?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor",
# "description": "", "g_review_stars": ""}, {"title": "Bitcoin.com | Buy BTC & BCH | News, prices,
# mining & wallet","link":"https: // www.bitcoin.com/","description":"Digital money that's instant,
#  private and free from bank fees. Download the official Bitcoin Wallet app today, and start
#  investing and trading in BTC or BCH.","g_review_stars":"Digital money that's instant,
#   private and free from bank fees. Download the official Bitcoin Wallet app today, and
#   start investing and trading in BTC or BCH."},{"title":"Bitcoin Definition - Investopedia",
#   "link": "https://www.investopedia.com/terms/b/bitcoin.asp", "description": "Bitcoin is a
#   digital or virtual currency created in 2009 that uses peer-to-peer technology to facilitate
#   instant payments. It follows the ideas set out in a whitepaper ...","g_review_stars":
#   "Bitcoin is a digital or virtual currency created in 2009 that uses peer-to-peer
#   technology to facilitate instant payments. It follows the ideas set out in a whitepaper ..."},
#   {"title": "How to Buy Bitcoin - Investopedia", "link": "https: // www.investopedia.com/articles /
#   investing/082914/basics-buying-and-investing-bitcoin.asp","description":"Buying Bitcoin is
#    getting easier by the day and the legitimacy of the exchanges and wallets is growing as well.
#    Key Takeaways. The value of Bitcoin is derived from ...","g_review_stars":"Buying Bitcoin is
#    getting easier by the day and the legitimacy of the exchanges and wallets is growing as well.
#    Key Takeaways. The value of Bitcoin is derived from ..."},{"title":"Bitcoin USD(BTC-USD)
#    Stock Price, News, Quote & History ...","link":"https: // finance.yahoo.com/quote/BTC-USD /",
#    "description": "Find the latest Bitcoin USD(BTC-USD) stock quote, history, news and other
#    vital information to help you with your stock trading and investing.","g_review_stars":
#    "Find the latest Bitcoin USD(BTC-USD) stock quote, history, news and other vital
#    information to help you with your stock trading and investing."}],"image_results": [],
#    "total":607000000, "answers":["1 Bitcoin equals", "56,372.40 United States Dollar",
#    "Apr 19, 2:04 PM UTC · Disclaimer", "1D", "5D", "1M", "1Y", "5Y", "Max", "61.60USD()
#      ‎10:30PM","50, 00055, 00060, 00065, 000","Mar 29Apr 9","No chart available"],"ts":7.13036847114563}


cleaned_url = link_string

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(cleaned_url)