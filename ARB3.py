import discord
from bs4 import BeautifulSoup
import requests
import re
from lxml import etree

TOKEN = '' # place discord token here


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# client = discord.Client(intents=discord.Intents.default())

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
            #await message.channel.send(response)
            url = f"https://myanimelist.net/search/all?q={response2}&cat=all"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            something = etree.HTML(str(soup))
            score = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[2]/text()[3]')[0]))
            href_tags = soup.find_all(href=True)
            name = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]')[0]))
            episodecount = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[2]/text()[2]')[0]))
            #ranking = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]')))
            #score1 = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]/div[1]/div[1]/div[1]/div')))
            url2 = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]/@href')[0]))
            print(url2)
            page2 = requests.get(url2)
            soup2 = BeautifulSoup(page2.text, "html.parser")
            something2 = etree.HTML(str(soup2))
            #ranking = (something2.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]'))
            #a_tags = soup.find_all('a')
            #print(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]'))
            #ranking = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]')))
            #link = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[3]/div[3]/a')[1]))
            synopsis = (something2.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/p/text()[1]'))
            title = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[1]/a[1]/text()')[0]))
            await message.channel.send(title)
            await message.channel.send(score)
            #await message.channel.send(link)
            await message.channel.send(episodecount)
            #await message.channel.send(ranking)
            #await message.channel.send(score1)
            #await message.channel.send(link)
            #await message.channel.send(synopsis)
            await message.channel.send(url2)
            #print(result)
            #if(response = "!next"):
                #i+=1
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
            name = (str(something.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[' + str(i) + ']/div[2]/div[1]/a[1]')[0]))
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
