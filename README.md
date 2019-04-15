# PyRecon
A small program that searches for existence of a given username in various websites.

## Requirements
- Python 3+
- [requests module](https://github.com/kennethreitz/requests) - The program will automatically install this module if 
you don't have it

## Information
To run the script just launch the `PyRecon.py` using `python PwnChrome.py -u`.

Websites supported:
- Badoo
- Bandcamp
- Buzzfeed
- DevianArt
- Disqus
- eBay
- Facebook
- Flickr
- Flipboard
- Foursquare
- Github
- HackerNews
- Imgur
- Instagram
- Medium
- Newgrounds
- Pastebin
- Patreon
- Pinterest
- Reddit
- Roblox
- Slack
- Soundcloud
- Spotify
- Steam
- TripAdvisor
- Twitter
- Vimeo
- VK
- Wattpad
- Wikipedia
- Wordpress
- Youtube

More websites can and will be added upon request.

Do note that there *may* be false positives. There is nothing I can do to prevent this as this script/program just 
checks if an account by that username exists in said websites. Future updates may gear towards eliminating such false 
positives but this is not guaranteed.

This project is educational purposes **ONLY**.

Written with Python 3.7.

## Known Issues
- Doing a search can take anywhere from a minute to two and a half minutes; depending on your internet speed. Will try 
to optimize this in future updates.
- If a website is blocked in your country, you will not be able to do a search for that website and that will cause the 
script to crash/halt. To prevent this I suggest you run the script with either a proxy or a VPN. 
- False positives will exist.

## Disclaimer
This project is for educational purposes **ONLY**. As the MIT License states:

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._

## Donations
If you'd like to donate to me use one of these two methods please:

**Bitcoin Cash:** [bitcoincash:qppxw4t8zqm4cp8gpvaldx4sur2f4e8wvgqecnl4ld](https://i.imgur.com/rwIhn3b.png)

**Bitcoin:** [1FBGXoAMSEmZwnbzyjQ81eo72EGU8hjV7A](https://i.imgur.com/6wxQ9G0.png)
