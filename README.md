# Choropleth Map D3

In this assignment, I gathered the data of the rural population percentage of 20 countries. I created a proportional symbol map and a choropleth map. The project includes 2 files: a9.html and the data file (a9.json). I hope you like it.
All the data I used in this assignment were download from [worldbank.org](https://data.worldbank.org).
The map function was download from [Topojson] (https://github.com/topojson/topojson).

## Link to the assignment
I have published this assignment to usc scf server. In order to view this assignment, use this link: [http://www-scf.usc.edu/~zhangyou/a9.html](http://www-scf.usc.edu/~zhangyou/a9.html).


## Local View Prerequisites
To run the code locally, you need to have npm and browsersync on your device.
Install 'npm', 'node.js' and use 'browsersync' to run the code.
Here are some instructions:
- [npm tutorial](https://docs.npmjs.com/cli/install)
- [node.js download](https://nodejs.org/en/download/)
- [browsersync tutorial](https://www.browsersync.io/)

## Usage

With 'npm' installed, run

    $ npm install browser-sync -g
to install Browsersync.

And from the root of your project directory run the following command
    
    browser-sync start --server --files "*.html, css/*.css, *.js"
    
This will allow BrowserSync to watch all HTML and CSS files in the current directory. Once you run the command, a browser window will open in the default browser serving the directories root file, in this case 'a5.html'. In the console of the running BrowserSync start command, you should see the result in your terminal (as shown in the screenshot).

- **Local**: represents the address on your local machine with which you can view the project.
- **External**: represents the address that any user on you network can view the project.

Then simply copy the address to your browser, and you will be able to see the page!
