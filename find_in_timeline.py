#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This script searches for a flagged clip in the Media Pool active bin and adds a marker to the active timeline for each occurrence of the clip.

The clip must have a 'Cream' flag set in order to be recognized by the script.

The script searches for the flagged source clip in the current bin in the Media Pool. If no flagged clip is found, the script exits. Otherwise, the script iterates over all video items
in the timeline and checks if their name matches the name of the flagged source clip. If a match is found, the script adds a marker to the timeline at the start of the matched item.

Note:
The script expects only one clip to be flagged as 'Cream'. If more than one clip is flagged the script will only look for the first item it founds.

Iddolahman@gmail.com
https://www.opus-tv.com/
"""

import sys

def get_flagged_clip(folder):
    """Returns the first clip in the given media folder that has the 'Cream' flag set.
    Args:
        folder (MediaPoolFolder): The media pool folder to search for the flagged clip.
    Returns:
        Media Pool Item: The first flagged clip found in the folder, or None if no clip is found.
    """
    for clip in folder.GetClipList():
        if 'Cream' in clip.GetClipProperty()['Flags']:
            return clip
    return None

def main():
    """Main function that searches for a flagged clip in the media pool and adds a marker to its occurrences in the timeline."""
    try:
        # Get the current Resolve project and media pool.
        resolve = bmd.scriptapp('Resolve')
        project_manager = resolve.GetProjectManager()
        proj = project_manager.GetCurrentProject()
        media_pool = proj.GetMediaPool()

        # Get the current media pool folder, timeline, and video track count.
        folder = media_pool.GetCurrentFolder()
        tl = proj.GetCurrentTimeline()
        offset = tl.GetStartFrame()
        video_track_count = tl.GetTrackCount('video')

        # Find the flagged source clip in the media pool.
        source_clip = get_flagged_clip(folder)

        # If no flagged clip is found, print a message and return.
        if source_clip is None:
            print('No clips flagged')
            return

        # Find all video items in the timeline and check if they match the flagged source clip.
        timeline_items = []
        for track_number in range(video_track_count):
            timeline_items.extend(tl.GetItemListInTrack('video', track_number+1))

        for item in timeline_items:
            if item.GetName() == source_clip.GetName():
                # If an item matches the flagged source clip, add a marker to the timeline.
                record_frame = item.GetStart()
                tl.AddMarker(record_frame - offset, 'Cream', 'Found One', '', 1, '')

        # Save the project to disk.
        project_manager.SaveProject()
    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":
    main()
