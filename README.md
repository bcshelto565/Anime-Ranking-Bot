# Anime-Ranking-Bot
Discord Bot which provides relevant information regarding anime queried through messages based on rankings and information provided at myanimelist.net

<a href="https://www.buymeacoffee.com/bcshelto565" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

In the ARB-2.py code and ARB3.py code the TOKEN variable needs to be initialized with the actual token value for the bot in discord so that the bot runs correctly.

To run ARB-2.py as a simple local process on a machine, open applicable python terminal and type  "python ARB-2.py" and run. 

#### *Ensure the bot has been added to applicable servers in your discord account.* ####
#### *My version uses my server's specific channel names for parsing responses in channels the bot is allowed to trawl.* ####
#### *This means it will not respond if your server channels do not have the same names as in the code, simply edit those names in line 35 of ARB3.py or line 31 of ARB-2.py* ####

### *ARB3.py* specific information below ###
### i.e. *if you wanna use the docker version of the bot for simple containerized discord bots* ###

This version of the python file will run on any os capable of running python files. 
This version does not require a webdriver. 

To create the docker image use this command: 
`sudo docker image build -t arb:latest /home/ARB-docker`
where /home/ARB-docker is the directory storing the dockerfile and ARB3.py file. 
After that just add the image to your docker compose file and the container will run the discord bot automatically.

Template compose.yaml with this docker container would look like this:

`version: "2"`<br>
`services:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`arb:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`image: arb:latest`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`container_name: arb`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`restart:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`unless-stopped`<br>
