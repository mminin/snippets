# Some cool things to add to your bashrc:
## Track time with this short function (log your activity by adding this to your ~/.bashrc):
```
timesheet() {
    echo $($1) test3 >> ~/Desktop/timesheets/20$(date +"%y")/$(date +"%m")/t$(date +"%d").txt
}

timesheetshow() {
    cat ~/Desktop/timesheets/20$(date +"%y")/$(date +"%m")/t$(date +"%d").txt
}
```

Mark your activity using 
```
     timesheet "start doing something"
     timesheet "making a comment"
     timesheet "stop doing something"
```  
View today's log using

     timesheetshow | grep "start\|stop"
