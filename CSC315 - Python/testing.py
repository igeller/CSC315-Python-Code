#!/bin/python3

import array, calendar, collections, copy, datetime, decimal, doctest, enum, functools, itertools, json, logging, math, math, numbers, operator, os, pprint, pydoc, random, re, string, struct, sys, time, types, typing

# Helper Functions for convenience

def convertContentData(contentData):
    """Takes in a JSON String of content data and returns a list of content objects"""
    return json.loads(contentData)

def convertPreferences(preferences):
    """Takes in a JSON String preferences object and returns a dictionary of preferences"""
    return json.loads(preferences)

def getDate(dateString):
    """Takes a JSON Date string (ISO8601) and returns a datetime object"""
    return datetime.datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S.%fZ')


#
# Complete the 'getTopTitles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING contentData
#  2. STRING brandPreferences
#  3. STRING contentTypePreferences
#

def getTopTitles(contentData, brandPreferences, contentTypePreferences):
    # Write your code here
    # content must be available in the US on or before 1/1/2020 to receive a score
    # sort content alphabetically by title if there is a tie
    #fewer then 5 titles retorn all by score
    prefValues = {'dislike': -20, 'indifferent': 0, 'like': 10, 'adore': 30, 'love': 50}
    bPrefObj = convertPreferences(brandPreferences)
    tPrefObj = convertPreferences(contentTypePreferences)
    #index = score and title is the value
    scoreTitle = dict()
    totalScore = 0;
    contentObj = (convertContentData(contentData))
    cdict = dict()
    i = 0
    for x in contentObj:
        # check brand and type
        if('US' in x['availability'] and x['availableDate'] <= '2020-01-01T00:00:00.000Z'):
            brnd = x['brand']
            typ = x['contentType']
            if brnd in bPrefObj:
                totalScore += prefValues[bPrefObj[brnd]]
            if typ in tPrefObj:
                totalScore += prefValues[tPrefObj[typ]]

            if totalScore in cdict:
                cdict[totalScore].add(x['title'])
            else:
                cdict[totalScore] = {x['title']}
            totalScore = 0

    # indifferent means add 0
    srtDict = reversed(sorted(cdict.keys()))
    titleList = list()
    for y in srtDict:
        for x in cdict[y]:
            if len(titleList) != 5:
                titleList.append(x)
        print('******', titleList)

    title = convertContentData(contentData)
    return list()

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    contentData = input()
    convertContentData(contentData)
    brandPreferences = input()
    convertPreferences(brandPreferences)
    contentTypePreferences = input()
    convertPreferences(contentTypePreferences)
    result = getTopTitles(contentData, brandPreferences, contentTypePreferences)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
