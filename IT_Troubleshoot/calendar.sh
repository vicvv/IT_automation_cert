
meeting_info=($zenity --form --title 'Meeting' --text 'Remidnder' \
--add-calendar 'Date' --add-entry 'Title' --add-entry 'Emails'\
--forms-date-format='%Y-%m-%d'\
> /dev/null 2>&1)

echo $meeting_info
if [[ -n $meeting_info ]]; then
    python send_remider.py "$meeting_info"
fi