#!/usr/bin/python
# -*- coding: utf-8 -*-

import DaVinciResolveScript as bmd

resolve = bmd.scriptapp('Resolve')
mediaStorage = resolve.GetMediaStorage()
projectManager = resolve.GetProjectManager()
proj = projectManager.GetCurrentProject()
mediaPool = proj.GetMediaPool()
tl = proj.GetCurrentTimeline()
startFrame = tl.GetCurrentVideoItem().GetStart()
videoTrackCount = tl.GetTrackCount('video')
video1Clips = tl.GetItemListInTrack('video', 1)
tc = tl.GetCurrentTimecode().replace(':', '.')

print('ok')