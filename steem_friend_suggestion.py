#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
import numpy as np

###  TANIMLAR  ####
BigNumberOfLetters = 0
###################

tags1 =[[4, 'steepshot'], [4, 'graphic'], [4, 'desing'], [4, 'creativity'], [4, 'art'], [3, 'women'], [3, 'tr'], [3, 'men'], [2, 'vector'], [2, 'python'], [2, 'linux'], [1, 'web'], [1, 'turkcebilim'], [1, 'talkingballoon'], [1, 'talking'], [1, 'sleep'], [1, 'simulation'], [1, 'shopping'], [1, 'see'], [1, 'script'], [1, 'scientific'], [1, 'programing'], [1, 'howto'], [1, 'dogmatic'], [1, 'difference'], [1, 'commandline'], [1, 'colors']]

tags2 = [[29, 'tr'], [21, 'trliste'], [20, 'life'], [19, 'cointurk'], [14, 'steem'], [13, 'destektr'], [11, 'travel'], [11, 'blog'], [10, 'fun'], [10, 'art'], [8, 'photography'], [6, 'steepshot'], [6, 'love'], [5, 'story'], [5, 'photo'], [5, 'museum'], [4, 'steemit'], [4, 'nature'], [4, 'meme'], [4, 'funny'], [4, 'dmania'], [3, 'technology'], [3, 'science'], [3, 'quraturk'], [3, 'naturephotography'], [3, 'brooklyn'], [2, 'utopian-io'], [2, 'turkcebilim'], [2, 'steemthatshare'], [2, 'steemthat'], [2, 'smartphonephotography'], [2, 'newyork'], [2, 'gaming'], [2, 'cn'], [2, 'cityscapephotography'], [2, 'busy'], [1, 'yesilkart'], [1, 'yesil'], [1, 'work'], [1, 'wordpress'], [1, 'waffle'], [1, 'usa'], [1, 'turkish'], [1, 'translation'], [1, 'timelapse'], [1, 'tgi'], [1, 'swing'], [1, 'sunset'], [1, 'sun'], [1, 'subway'], [1, 'streetphotography'], [1, 'steemshot'], [1, 'steemblog'], [1, 'sports'], [1, 'soccer'], [1, 'snow'], [1, 'ski'], [1, 'seyahat'], [1, 'sanat'], [1, 'redhook'], [1, 'photoshop'], [1, 'photograhpy'], [1, 'nyc'], [1, 'new'], [1, 'logo'], [1, 'landscapephotography'], [1, 'kayak'], [1, 'introduceyourself'], [1, 'greencard'], [1, 'gif'], [1, 'futbol'], [1, 'food'], [1, 'factorio'], [1, 'dtube'], [1, 'drink'], [1, 'design'], [1, 'davinci-application'], [1, 'cuma'], [1, 'crypto'], [1, 'coin'], [1, 'coffee'], [1, 'city'], [1, 'christmas'], [1, 'cat'], [1, 'cappadocia'], [1, 'canal'], [1, 'bisiklet'], [1, 'bicycle'], [1, 'basvuru'], [1, 'animal'], [1, 'analiz'], [1, 'amerika']]

# en uzun tag'ın harf sayısı
# Tüm tag'ları bu uzunlukta yapmak için gerekli
def find_longest_tag(UserTags):
    global BigNumberOfLetters
    for k in UserTags:
        tag = k[1]
        NumberOfLetters = len(tag)
        if NumberOfLetters > BigNumberOfLetters:
            BigNumberOfLetters = NumberOfLetters

# tag'ları binary'e çevir. Liste yap. 0 olan liste elemanlarını -1 yap.
def fingerprint(tag):
    # tag'ı binary'e çevir: 01010101
    A = ''.join(format(ord(x), 'b') for x in tag)
    A_List = list(A)
    # liste öğelerinde 0 olanları -1 yap
    for k in A_List:
        if k == "0":
            A_List[A_List.index(k)] = '-1'
    return A_List

def fingerprint_list_add_null_item(fingerprint_tag):
    nulllist = '0' * ((BigNumberOfLetters * 7) - (len(fingerprint_tag)))
    xxx = list(nulllist)+fingerprint_tag


find_longest_tag(tags1)

for k in tags1:
    tag = k[1]
    fingerprint_list_add_null_item(fingerprint(tag))
    print(tag, len(fingerprint(tag)))
    
print(BigNumberOfLetters)



list1 = ['1', '1', '-1', '-1', '1', '-1', '-1', '1', '1', '-1', '1', '1', '1', '1', '1', '1', '-1', '-1', '1', '1', '1', '1', '1', '-1', '1', '1', '-1', '1', '1', '1', '-1', '-1', '-1', '-1', '1', '1', '1', '1', '-1', '1', '-1', '-1', '1', '1', '-1', '1', '-1', '-1', '1', '1', '1', '-1', '-1', '-1', '1', '1']
list2 = ['1', '1', '-1', '-1', '1', '-1', '-1', '1', '1', '-1', '1', '-1', '-1', '1', '1', '1', '-1', '-1', '1', '1', '-1', '1', '1', '-1', '-1', '1', '1', '-1', '1', '1', '-1', '-1', '1', '-1', '1', '1', '1', '1', '-1', '-1', '1', '-1', '1', '1', '-1', '-1', '1', '-1', '1', '1', '1', '-1', '1', '1', '1', '-1', '1', '1', '-1', '-1', '-1', '1', '1', '1', '1','-1', '-1', '1', '-1', '1']

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

sum_vector = vector1 + vector2
print(sum_vector)
