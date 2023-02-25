# ip-logger

A script created to log your IP addresses

If you use a VPN connection without a specific location selected, it can be helpful to keep track of what server location you were connected to at a specific time, how often you are connected to a certain location, how often your server location changes etc.

Example output:
```
{
  "ip": "68.16.90.33",
  "city": "New York City",
  "region": "New York",
  "country": "US",
  "loc": "40.7143,-74.0060",
  "org": "AS9009 M247 Europe SRL",
  "postal": "10004",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth",
  "timestamp": "2023-02-25 00:31:11.432051"
}
```
This script can be scheduled to run periodically with crontab and to update your log file without having to run it manually.
