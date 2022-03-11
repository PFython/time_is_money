# TIME (time_is_money)
A simple command line script for time recording.  Windows only currently.

## Background
As a former video editor I'm a great fan of programmable keyboards and gadgets like the Elgato Streamdeck and wanted a simple "one button solution" for time recording when doing billable client work. Having to log on to various (paid/subscription) web apps often meant I just didn't bother, or forgot, to start the clock on smaller jobs.  I was also looking for an excuse to use `pendulum` which looked really promising for time and date manipulation.

I created `time_is_money` as a quick and dirty solution to that problem and would be pleased if other people found it useful or wanted to expand it's scope or functionality.  If that's you, please have a look at https://github.com/PFython/time_is_money/issues for some ideas about how to contribute.

## Usage

Start time recording for client MY CLIENT NAME an activity dsecription MY CURRENT TASK:

`C:\> tim.pyw "MY CLIENT NAME" "MY CURRENT TASK"`
`C:\> tim.pyw CLIENT ACTIVITY
(I've used capital letters for emphasis but you can use whatever case you want).

Stop recording time for the latest log entry:

`C:\> tim.pyw STOP`

Calculate all time recorded in current log file (default `tim.csv`):

`C:\> tim.pyw TOTALS`

Calculate all time recorded since "2022-03-10"
`C:\> time.pyw 2022-03-10`
