# Local Web Server

Overall Version: V1.3

Project that will be hopefully used for control of the Pi away from the Terminal

## Meal Planner
Local meal planner to help with weekly meal planning inspiration

### Changelog
 - V0.2
	- Shuffled output
 - V0.1
	- Initial Release

### Features
 - Meal Ideas
 - Add Meal ideas

## Show Tracker
Local show tracker to track all TV series currently being watched. Resolved issue of in-market apps using US show/release times which are normally ahead of UK

### Changelog
 - V1.3 (Patch)
	- Daily Notification URL for Flask - ready for use with Daily Systemd timer
	- Fix scroll issue on "all shows" table where table would appear on "What's on today" screen
 - V1.2 (Patch)
	- Code Tidy
	- Fix Scroll issue with "all shows" table
 - V1 - SQL Migration
 	- Migrate to SQL to make everything tidier in backend
 - V0.2 - User Centered
 	- Add 3 Screens:
 		- 1 For On today (on launch)
 		- 1 for "What should I watch - Based on OD shows and uses tags
 		- 1 for all shows
 - V0.1
	- Initial Release

### Features
 - View on tonight based on time
 - Get "What should I watch" shows based on tags
 - View all current shows
	- Includes Title, Duration, Service, Release Day/Time (if required)
 - Add new show
 - Daily reminder URL for Systemd daily run (e.g. at 7pm) to summarise what's on tonight
 
## Photo Backup Server
Local Photo backup server to keep full-quality photo backups of good images. 

Trying to resolve the issue of relying on Google Photos to store photos as this reduces the quality...

#Change Log
 - V0.1
 	- Initial Release
 	- Limited release includes Photo uploading, Error photos go into Error. Future development planned
 




