from selenium import webdriver
import time

def sbmm():
    driver = webdriver.Chrome()
    url_gon = 'https://sbmmwarzone.com/profile/Gon%2312995/platform/battle'
    url_badar = 'https://sbmmwarzone.com/profile/Badar326/platform/psn'
    url_robot = 'https://sbmmwarzone.com/profile/TheMar%252311115/platform/battle'
    url_seeb = 'https://sbmmwarzone.com/profile/jseeby%231137/platform/battle'
    driver.get(url_badar)

    time.sleep(5)
    element = driver.find_element_by_css_selector('body')
    body = element.text
    body = body[400:]
    #print(body)
    tiers = {
        'Bronze 1'   : countFreq('BRONZE 1',body),
        'Bronze 2'   : countFreq('BRONZE 2',body),
        'Bronze 3'   : countFreq('BRONZE 3',body),
        'Bronze 4'   : countFreq('BRONZE 4',body),
        'Silver 1'   : countFreq('SILVER 1',body),
        'Silver 2'   : countFreq('SILVER 2',body),
        'Silver 3'   : countFreq('SILVER 3',body),
        'Silver 4'   : countFreq('SILVER 4',body),
        'Gold 1'     : countFreq('GOLD 1 ' ,body),
        'Gold 2'     : countFreq('GOLD 2 ' ,body),
        'Gold 3'     : countFreq('GOLD 3 ' ,body),
        'Gold 4'     : countFreq('GOLD 4 ' ,body),
        'Platinum 1' : countFreq('PLATINUM 1',body),
        'Platinum 2' : countFreq('PLATINUM 2',body),
        'Platinum 3' : countFreq('PLATINUM 3',body),
        'Platinum 4' : countFreq('PLATINUM 4',body),
        'Diamond 1'  : countFreq('DIAMOND 1', body),
        'Diamond 2'  : countFreq('DIAMOND 2', body),
        'Diamond 3'  : countFreq('DIAMOND 3', body),
        'Diamond 4'  : countFreq('DIAMOND 4', body)
    }

    print('\nThese are your games statistics : \n')

    sortedTiers = dict(sorted(tiers.items(), key=lambda item: item[1],reverse=True))
    total = 0
    for x in sortedTiers.values():
        total+= x

    for y,z in sortedTiers.items():
        if z == 0:
            print(0.00,'  % ',y)
        elif int((z/total)*100) < 10:
            print(round((z/total)*100,2),' % ',y)
        else:
            print(round((z/total)*100,2),'% ',y)

    # #print(body)
    # total = 0
    # counts = word_count(body)
    # bronze = key_check('BRONZE',counts)
    # total+=bronze
    # silver = key_check('SILVER', counts)
    # total+=silver
    # gold = key_check('GOLD', counts)
    # total+=gold
    # platinum = key_check('PLATINUM', counts)
    # total+=platinum
    # diamond = key_check('DIAMOND', counts)
    # total+=diamond
    # print((bronze/total)*100,'% Bronze')
    # print((silver/total)*100,'% Silver')
    # print((gold/total)*100,'% Gold')
    # print((platinum/total)*100,'% Platinum')
    # print((diamond/total)*100,'% Diamond')

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def key_check(key_to_lookup,dictionary):
    if key_to_lookup in dictionary:
        return dictionary[key_to_lookup]
    else:
        return 0


def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    for i in range(N - M + 1):

        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            res += 1
            j = 0
    return res

def main():
    sbmm()
    #input(':')
main()