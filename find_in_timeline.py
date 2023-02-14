#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import DaVinciResolveScript as bmd

resolve = bmd.scriptapp('Resolve')
mediaStorage = resolve.GetMediaStorage()
projectManager = resolve.GetProjectManager()
proj = projectManager.GetCurrentProject()
mediaPool = proj.GetMediaPool()
folder = mediaPool.GetCurrentFolder()
tl = proj.GetCurrentTimeline()
videoTrackCount = tl.GetTrackCount('video')
mediaPoolClips = []
timelineItems = []

for clip in folder.GetClipList():
    if clip.GetClipProperty()['Flags'] == 'Cream':
        mediaPoolClips.append(clip)
        
if not len(mediaPoolClips):
    print('No Clips found.\nPlease add flag "Cream" to the desire clip.')
    sys.exit()

for trackNumber in range(videoTrackCount):
    timelineItems.extend(tl.GetItemListInTrack('video', trackNumber+1))

for clip in mediaPoolClips:
    for item in timelineItems:
        if item.GetMediaPoolItem() == clip:
            print(item.GetName())
            item.SetClipColor("Cream")
