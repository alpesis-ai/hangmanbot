def get_result(client, sessionId):
    result = client.get_result(sessionId)
    wrongWordCount = int(result['data']['totalWordCount']) - int(result['data']['correctWordCount'])
    print "***************************************************************"
    print "Performance"
    print "***************************************************************"
    print "Result:"
    print result
    print "- totalWordCount: %s" % result['data']['totalWordCount']
    print "- correctWordCount: %s" % result['data']['correctWordCount']
    print "- wrongWordCount: %s" % str(wrongWordCount)
    print "- totalWrongGuessCount: %s" % result['data']['totalWrongGuessCount']
    print "- score: %s" % result['data']['score']
    print "***************************************************************"
    return result
