## Escape from Amsterdam

Escape from Amsterdam is a small retro text based advanture game that draws 
inspiration from games like Zork and Slouching Towards Bedlam.

Because best 3D engine is your own imagination :)

The story follows main protagonist who wakes up in what looks like a hotel room in Amsterdam. His memory is hazy, but the rules are clear.

Find the snippets of code hidden around the room to get out of the room until door is locked...Forever.

## Features
* ASCII art
![Start game](/screenshots/start_game.png)

* Multiple items to investigate
![Game menu](/screenshots/game_menu.png)

* Replayability is achieved through randomization of code locations

<br/>

## Testing

* User input validations

    * Input length
    * Is input a (valid) number
    * Correct code sequence

<br/>

* PEP8 

    * `Run.py` - Fully passes PEP8 validation from online validator http://pep8online.com/

    * `Items.py` - Some lines are longer to keep the proper text formating in game

<br/>

* Tested on Windows 10 and Fedora 35

### Requirements
* Python version 3.10+ is required because of the use of new match case statement
* .gitpod.dockerfile is set to correct version

<br/>

## Deployment

### Local

To locally deploy the project clone the Git repository
>git clone https://github.com/Azelliott/escape-from-amsterdam.git

### Heroku

You can visit the live application on Heroku
> https://escape-from-amsterdam.herokuapp.com

## Credits

I got the inspiration from great write-up by Mike Wolfe, you can check it out here:

>https://python.plainenglish.io/building-an-old-school-text-based-game-with-python-efcc33d25a42
