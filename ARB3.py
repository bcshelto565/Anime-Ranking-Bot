import discord
from bs4 import BeautifulSoup
import requests
from lxml import etree

TOKEN = '' # place discord token here


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

search_term = ""

#url = f"https://myanimelist.net/search/all?q={search_term}&cat=all"

print('python code run successfully')

@client.event
async def on_ready():
    print('Neckbeard online as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    i=1
    if message.author == client.user:
        return
    if message.channel.name == 'bot-test' or message.channel.name == 'off-topic-aka-hot-garbage' or message.channel.name == 'memes' or message.channel.name == 'weeb-shit':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '$animesux' or user_message.lower() == 'anime sucks' or user_message.lower() == 'anime sux':
            response = f'Anime Rocks. Be a weeb {username}!'
            await message.channel.send(response)
            return
        elif user_message.__contains__("$search"):
            i=1
            input_string = user_message.lower()
            response = (input_string[7:])
            response2 = response.replace(" ", "%20")
            url = f"https://myanimelist.net/search/all?q={response2}&cat=all"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            something = etree.HTML(str(soup))
            score = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[2]/text()[3]')[0]))
            episodecount = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[2]/text()[2]')[0]))
            url2 = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]/@href')[0]))
            print(url2)
            page2 = requests.get(url2)
            soup2 = BeautifulSoup(page2.text, "html.parser")
            title = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]/text()')[0]))
            await message.channel.send(title)
            await message.channel.send(score)
            sup3 = soup2.find_all("strong")
            strongCount = 0
            for sup2 in sup3:
                if strongCount == 1:
                    await message.channel.send("Total Site Ranking is: " + sup2.string)
                elif strongCount == 2:
                    await message.channel.send("Popularity Ranking is: " + sup2.string)
                    break
                strongCount = strongCount + 1
            if episodecount == "\n       (1 eps)":
                await message.channel.send("Movie")
            else:
                await message.channel.send("TV Show")
                await message.channel.send(episodecount)
            await message.channel.send(url2)
            await message.channel.send("Is this correct? If not message '$next (query)' to grab the next result")
            return
        elif user_message.__contains__("$next"):
            i+=1
            input_string = user_message.lower()
            response = (input_string[5:])
            response2 = response.replace(" ", "%20")
            url = f"https://myanimelist.net/search/all?q={response2}&cat=all"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            something = etree.HTML(str(soup))
            score = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[' + str(i) + ']/div[2]/div[2]/text()[3]')[0]))
            episodecount = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[' + str(i) + ']/div[2]/div[2]/text()[2]')[0]))
            url2 = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[' + str(i) + ']/div[2]/div[1]/a[1]/@href')[0]))
            title = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[' + str(i) + ']/div[2]/div[1]/a[1]/text()')[0]))
            await message.channel.send(title)
            await message.channel.send(score)
            await message.channel.send(episodecount)
            await message.channel.send(url2)
            await message.channel.send("current position in search results is: " + str(i))
            await message.channel.send("Is this correct? If not message '$next (query)' to grab the next result")
            return
client.run(TOKEN)
