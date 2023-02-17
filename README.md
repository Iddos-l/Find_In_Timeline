# Find_In_Timeline

This script searches for a flagged clip in the media pool of a DaVinci Resolve project and adds a marker to the timeline
for each occurrence of the clip. The clip must have a 'Cream' flag set in order to be recognized by the script.

The script searches for the flagged source clip in the media pool. If no flagged clip is found, the script exits. Otherwise, the script iterates over all video items
in the timeline and checks if their name matches the name of the flagged source clip. If a match is found, the script adds a marker to the timeline at the start of the matched item.