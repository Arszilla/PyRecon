import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description="Searches for a given username across 33 websites.",
                                 usage="PyRecon -u username")
# Creates -u arg
parser.add_argument("-u", "--username", metavar="", required=True, help="Username to search for.")
args = parser.parse_args()

try:
    import requests

    def main(username):
        results = {"Badoo": badoo(username),
                   "Bandcamp": bandcamp(username),
                   "Buzzfeed": buzzfeed(username),
                   "DevianArt": deviantart(username),
                   "Disqus": disqus(username),
                   "eBay": ebay(username),
                   "Facebook": facebook(username),
                   "Flickr": flickr(username),
                   "Flipboard": flipboard(username),
                   "Foursquare": foursquare(username),
                   "Github": github(username),
                   "HackerNews": hackernews(username),
                   "Imgur": imgur(username),
                   "Instagram": instagram(username),
                   "Medium": medium(username),
                   "Newgrounds": newgrounds(username),
                   "Pastebin": pastebin(username),
                   "Patreon": patreon(username),
                   "Pinterest": pinterest(username),
                   "Reddit": reddit(username),
                   "Roblox": roblox(username),
                   "Slack": slack(username),
                   "Soundcloud": soundcloud(username),
                   "Spotify": spotify(username),
                   "Steam": steam(username),
                   "TripAdvisor": tripadvisor(username),
                   "Twitter": twitter(username),
                   "Vimeo": vimeo(username),
                   "VK": vk(username),
                   "Wattpad": wattpad(username),
                   "Wikipedia": wikipedia(username),
                   "Wordpress": wordpress(username),
                   "Youtube": youtube(username)}


        print(f"""
        Badoo: {results["Badoo"]}
        Bandcamp: {results["Bandcamp"]}
        Buzzfeed: {results["Buzzfeed"]}
        DevianArt: {results["DevianArt"]}
        Disqus: {results["Disqus"]}
        eBay: {results["eBay"]}
        Facebook: {results["Facebook"]}
        Flickr: {results["Flickr"]}
        Flipboard: {results["Flipboard"]}
        Foursquare: {results["Foursquare"]}
        Github: {results["Github"]}
        HackerNews: {results["HackerNews"]}
        Imgur: {results["Imgur"]}
        Instagram: {results["Instagram"]}
        Medium: {results["Medium"]}
        Newgrounds: {results["Newgrounds"]}
        Pastebin: {results["Pastebin"]}
        Patreon: {results["Patreon"]}
        Pinterest: {results["Pinterest"]}
        Reddit: {results["Reddit"]}
        Roblox: {results["Roblox"]}
        Slack: {results["Slack"]}
        Soundcloud: {results["Soundcloud"]}
        Spotify: {results["Spotify"]}
        Steam: {results["Steam"]}
        TripAdvisor: {results["TripAdvisor"]}
        Twitter: {results["Twitter"]}
        Vimeo: {results["Vimeo"]}
        VK: {results["VK"]}
        Wattpad: {results["Wattpad"]}
        Wikipedia: {results["Wikipedia"]}
        Wordpress: {results["Wordpress"]}
        Youtube: {results["Youtube"]}
        """)

        with open(f"PyRecon Search Results for {username}.txt", "w") as file:
            file.write(
                f'Badoo: {results["Badoo"]}\n'
                f'Bandcamp: {results["Bandcamp"]}\n'
                f'Buzzfeed: {results["Buzzfeed"]}\n'
                f'DevianArt: {results["DevianArt"]}\n'
                f'Disqus: {results["Disqus"]}\n'
                f'eBay: {results["eBay"]}\n'
                f'Facebook: {results["Facebook"]}\n'
                f'Flickr: {results["Flickr"]}\n'
                f'Flipboard: {results["Flipboard"]}\n'
                f'Foursquare: {results["Foursquare"]}\n'
                f'Github: {results["Github"]}\n'
                f'HackerNews: {results["HackerNews"]}\n'
                f'Imgur: {results["Imgur"]}\n'
                f'Instagram: {results["Instagram"]}\n'
                f'Medium: {results["Medium"]}\n'
                f'Newgrounds: {results["Newgrounds"]}\n'
                f'Pastebin: {results["Pastebin"]}\n'
                f'Patreon: {results["Patreon"]}\n'
                f'Pinterest: {results["Pinterest"]}\n'
                f'Reddit: {results["Reddit"]}\n'
                f'Roblox: {results["Roblox"]}\n'
                f'Slack: {results["Slack"]}\n'
                f'Soundcloud: {results["Soundcloud"]}\n'
                f'Spotify: {results["Spotify"]}\n'
                f'Steam: {results["Steam"]}\n'
                f'TripAdvisor: {results["TripAdvisor"]}\n'
                f'Twitter: {results["Twitter"]}\n'
                f'Vimeo: {results["Vimeo"]}\n'
                f'VK: {results["VK"]}\n'
                f'Wattpad: {results["Wattpad"]}\n'
                f'Wikipedia: {results["Wikipedia"]}\n'
                f'Wordpress: {results["Wordpress"]}\n'
                f'Youtube: {results["Youtube"]}')

        print("These search results and links are placed at the same location as your 'PyRecon.py'\n")


    def badoo(username):
        badoo_acc = requests.get(f"https://badoo.com/en/{username}")
        if badoo_acc.status_code != 404:
            return f"https://badoo.com/en/{username}"
        else:
            return "User was not found"


    def bandcamp(username):
        bandcamp_user = requests.get(f"https://bandcamp.com/{username}")
        if bandcamp_user.status_code != 404:
            return f"https://bandcamp.com/{username}"
        else:
            return "User was not found"


    def buzzfeed(username):
        buzzfeed_user = requests.get(f"https://buzzfeed.com/{username}")
        if buzzfeed_user.status_code != 404:
            return f"https://buzzfeed.com/{username}"
        else:
            return "User was not found"


    def deviantart(username):
        deviantart_user = requests.get(f"https://{username}.deviantart.com")
        if deviantart_user.status_code != 404:
            return f"https://{username}.deviantart.com"
        else:
            return "User was not found"


    def disqus(username):
        disqus_user = requests.get(f"https://disqus.com/{username}")
        if disqus_user.status_code != 404:
            return f"https://disqus.com/{username}"
        else:
            return "User was not found"


    def ebay(username):
        ebay_user = requests.get(f"https://ebay.com/usr/{username}")
        if ebay_user.status_code != 404:
            return f"https://ebay.com/usr/{username}"
        else:
            return "User was not found"


    def facebook(username):
        facebook_acc = requests.get(f"https://facebook.com/{username}")
        if facebook_acc.status_code != 404:
            return f"https://facebook.com/{username}"
        else:
            return "User was not found"


    def flickr(username):
        flickr_user = requests.get(f"https://flickr.com/people/{username}")
        if flickr_user.status_code != 404:
            return f"https://flickr.com/people/{username}"
        else:
            return "User was not found"


    def flipboard(username):
        flipboard_user = requests.get(f"https://flipboard.com/@{username}")
        if flipboard_user.status_code != 404:
            return f"https://flipboard.com/@{username}"
        else:
            return "User was not found"


    def foursquare(username):
        foursquare_user = requests.get(f"https://foursquare.com/{username}")
        if foursquare_user.status_code != 404:
            return f"https://foursquare.com/{username}"
        else:
            return "User was not found"


    def github(username):
        github_acc = requests.get(f"https://github.com/{username}")
        if github_acc.status_code != 404:
            return f"https://github.com/{username}"
        else:
            return "User was not found"


    def hackernews(username):
        hackernews_user = requests.get(f"https://news.ycombinator.com/user?id={username}")
        if hackernews_user.status_code != 404:
            return f"https://news.ycombinator.com/user?id={username}"
        else:
            return "User was not found"


    def imgur(username):
        imgur_user = requests.get(f"https://imgur.com/{username}")
        if imgur_user.status_code != 404:
            return f"https://imgur.com/{username}"
        else:
            return "User was not found"


    def instagram(username):
        instagram_acc = requests.get(f"https://instagram.com/{username}")
        if instagram_acc.status_code != 404:
            return f"https://instagram.com/{username}"
        else:
            return "User was not found"


    def medium(username):
        medium_user = requests.get(f"https://medium.com/@{username}")
        if medium_user.status_code != 404:
            return f"https://medium.com/@{username}"
        else:
            return "User was not found"


    def newgrounds(username):
        newgrounds_user = requests.get(f"https://{username}.newgrounds.com")
        if newgrounds_user.status_code != 404:
            return f"https://{username}.newgrounds.com"
        else:
            return "User was not found"


    def pastebin(username):
        pastebin_acc = requests.get(f"https://pastebin.com/u/{username}")
        if pastebin_acc.status_code != 404:
            return f"https://pastebin.com/u/{username}"
        else:
            return "User was not found"


    def patreon(username):
        patreon_acc = requests.get(f"https://patreon.com/{username}")
        if patreon_acc.status_code != 404:
            return f"https://patreon.com/{username}"
        else:
            return "User was not found"


    def pinterest(username):
        pinterest_acc = requests.get(f"https://pinterest.com/{username}")
        if pinterest_acc.status_code != 404:
            return f"https://pinterest.com/{username}"
        else:
            return "User was not found"


    def reddit(username):
        reddit_acc = requests.get(f"https://reddit.com/u/{username}")
        if reddit_acc.status_code != 404:
            return f"https://reddit.com/user/{username}"
        else:
            return "User was not found"


    def roblox(username):
        roblox_user = requests.get(f"https://roblox.com/user.aspx?username={username}")
        if roblox_user.status_code != 404:
            return f"https://roblox.com/user.aspx?username={username}"
        else:
            return "User was not found"


    def slack(username):
        slack_user = requests.get(f"https://{username}.slack.com")
        if slack_user.status_code != 404:
            return f"https://{username}.slack.com"
        else:
            return "User was not found"


    def soundcloud(username):
        soundcloud_user = requests.get(f"https://soundcloud.com/{username}")
        if soundcloud_user.status_code != 404:
            return f"https://soundcloud.com/{username}"
        else:
            return "User was not found"


    def spotify(username):
        spotify_acc = requests.get(f"https://spotify.com/user/{username}")
        if spotify_acc.status_code != 404:
            return f"https://spotify.com/user/{username}"
        else:
            return "User was not found"


    def steam(username):
        steam_user = requests.get(f"https://steamcommunity.com/user/{username}")
        if steam_user.status_code != 404:
            return f"https://steamcommunity.com/user/{username}"
        else:
            return "User was not found"


    def tripadvisor(username):
        tripadvisor_user = requests.get(f"https://tripadvisor.com/members/{username}")
        if tripadvisor_user.status_code != 404:
            return f"https://tripadvisor.com/members/{username}"
        else:
            return "User was not found"


    def twitter(username):
        twitter_user = requests.get(f"https://twitter.com/{username}")
        if twitter_user.status_code != 404:
            return f"https://twitter.com/{username}"
        else:
            return "User was not found"


    def vimeo(username):
        vimeo_user = requests.get(f"https://vimeo.com/{username}")
        if vimeo_user.status_code != 404:
            return f"https://vimeo.com/{username}"
        else:
            return "User was not found"


    def vk(username):
        vk_user = requests.get(f"https://vk.com/{username}")
        if vk_user.status_code != 404:
            return f"https://vk.com/{username}"
        else:
            return "User was not found"


    def wattpad(username):
        wattpad_user = requests.get(f"https://wattpad.com/user/{username}")
        if wattpad_user.status_code != 404:
            return f"https://wattpad.com/user/{username}"
        else:
            return "User was not found"


    def wikipedia(username):
        wikipedia_user = requests.get(f"https://wikipedia.org/wiki/User:{username}")
        if wikipedia_user.status_code != 404:
            return f"https://wikipedia.org/wiki/User:{username}"
        else:
            return "User was not found"


    def wordpress(username):
        wordpress_user = requests.get(f"https://{username}.wordpress.com")
        if wordpress_user.status_code != 404:
            return f"https://{username}.wordpress.com"
        else:
            return "User was not found"


    def youtube(username):
        youtube_user = requests.get(f"https://youtube.com/{username}")
        if youtube_user.status_code != 404:
            return f"https://youtube.com/{username}"
        else:
            return "User was not found"
        

except ModuleNotFoundError:
    # If "requests" module is not present in Python it will display the following message.
    print("'requests' is not present. Installing 'requests':\n")
    # Installs 'requests' module for the user.
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    print("\nRestarting...")
    # Restarts the script.
    os.execl(sys.executable, sys.executable, *sys.argv)


if __name__ == '__main__':
    main(args.username)
