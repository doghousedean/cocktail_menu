# Cocktail Menu


## Why?

I created this for my wife's 40th birthday celebrations during 2021's lockdown
This was running on a Nvidia Jenson Nano 2GB with a touch screen 
so we can pick a cocktail and display the recipe

## Usage

Simple enough, interface is on port 80 after it comes up, 
feel free to change the port in the docker-compose.yml file

	git clone git@github.com:doghousedean/cocktail_menu.git
	cd cocktail_menu
	docker-compose up -d

## Configuration

You can change the header text by editing the config.json file, this is then bound to a file in the docker container

	{
	  "heading": "Cocktail Menu"
	}
	
