#!/bin/bash
launchctl load /Users/danielkato/Code/bear-scripts/com.dmkato.daily-bear-notes.plist
launchctl start com.dmkato.daily-bear-notes
launchctl list | grep "dmkato"