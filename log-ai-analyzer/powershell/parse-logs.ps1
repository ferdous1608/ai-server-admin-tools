# Export 50 latest system event logs
Get-WinEvent -LogName System -MaxEvents 50 |
    Export-Csv -Path "../logs/system_logs.csv" -NoTypeInformation