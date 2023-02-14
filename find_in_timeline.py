#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import DaVinciResolveScript as bmd

def get_flaged_clip(folder):
    for clip in folder.GetClipList():
        if clip.GetClipProperty()['Flags'] == 'Cream':
            return clip

def main():
    resolve = bmd.scriptapp('Resolve')
    projectManager = resolve.GetProjectManager()
    proj = projectManager.GetCurrentProject()
    mediaPool = proj.GetMediaPool()
    folder = mediaPool.GetCurrentFolder()
    tl = proj.GetCurrentTimeline()
    videoTrackCount = tl.GetTrackCount('video')
    timelineItems = []
    sourceClip = get_flaged_clip(folder)
    if sourceClip == None:
        print('No clips flaged')
        sys.exit()

    for trackNumber in range(videoTrackCount):
        timelineItems.extend(tl.GetItemListInTrack('video', trackNumber+1))

    for item in timelineItems:
        if item.GetName() == sourceClip.GetName():
            print(item.GetName())
            print(tl.GetStartFrame())
            recordFrame = item.GetStart()
            print(recordFrame)
            tl.AddMarker(90000, 'Cream', 'Found One', '', 1, '')

    projectManager.SaveProject()


if __name__ == "__main__":
    main()
