#!/bin/bash
launchctl stop com.dmkato.daily-bear-notes
launchctl unload /Users/danielkato/Code/bear-scripts/com.dmkato.daily-bear-notes.plist
launchctl list | grep "dmkato"