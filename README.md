# TIM (Time Is Money)
A simple command line script for time recording.  Windows only currently.


![Time is Money](https://media.giphy.com/media/26tnqkPaDXV7EzPAQ/giphy-downsized-large.gif)


## Background
As a former video editor I'm a great fan of programmable keyboards and gadgets like the Elgato Streamdeck and wanted a simple "one button solution" for time recording when doing  client work. Having to log on to various (paid/subscription) web apps often meant I just didn't bother, or forgot, to start the clock on smaller jobs.  I was also looking for an excuse to use `pendulum` for the first time.  It looked promising for date/time manipulation, and really is!

I created `Time Is Money` as a quick and dirty solution to that problem and would be pleased if other people found it useful or wanted to expand it's scope or functionality.  If that's you, please have a look at https://github.com/PFython/time_is_money/issues for some ideas about how to contribute.

## Usage

Start time recording for client MY CLIENT NAME an activity dsecription MY CURRENT TASK:

    C:\> tim.pyw "MY CLIENT NAME" "MY CURRENT TASK"

    C:\> tim.pyw CLIENT TASK

_(I've used capital letters for emphasis but you can use whatever case you want)._

Stop recording time for the latest log entry:

    C:\> tim.pyw STOP

Calculate all time recorded in current log file (default `tim.csv`):

    C:\> tim.pyw TOTALS

Calculate all time recorded since "2022-03-10"

    C:\> time.pyw 2022-03-10

----
If you find `Time Is Money` helpful, please feel free to:

<a href="https://www.buymeacoffee.com/pfython" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>
