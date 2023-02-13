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
    print('No Clips found.\nPlease add flag "Cream" to the desire clips.')
    sys.exit()

for clip in mediaPoolClips:
    print(clip.GetMediaId())


timelineItems.append(tl.GetItemListInTrack('video', 1))
print(timelineItems[0][0].GetName())
# for trackNumber in range(videoTrackCount):
#     timelineItems.append(tl.GetItemListInTrack('video', trackNumber))

# print(len(timelineItems))
