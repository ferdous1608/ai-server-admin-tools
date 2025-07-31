# Placeholder: Simulate alerts for testing
@"
Subject,Body
Disk Failure,Drive D: on Server1 has failed.
CPU Alert,CPU usage above 95% on Server2.
Info,Backup completed successfully.
"@ | Out-File ../output/log.csv -Encoding utf8