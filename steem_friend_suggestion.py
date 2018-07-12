#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
import yaml # string'i sözlüğe çevirmek için
from steem import Steem
s = Steem()

account_name = "aytekinaygun"

# Kişiye ait blog girdilerini sözlük olarak al.
# En son 500 blog yazısını çekebiliyoruz.
List_Blog_Entries = s.get_blog_entries(account_name, 0, 500)
List_All_Tag = []
for i in List_Blog_Entries:
    if i['author'] == account_name: # resteem yapılan poslar hariç tutulur
        entry_link = i['permlink']
        blog_metadata = s.get_content(account_name, entry_link)['json_metadata']
        # metadata bilgileri (sözlük şeklinde) tırnak içinde olduğundan, string olarak geliyor. Önce sözlüğe çevir.
        Dict_Blog_Metadata = yaml.load(blog_metadata)
        # Blog yazısındaki taglar liste olarak alınır.
        List_Entry_Tag = Dict_Blog_Metadata['tags']
        # Listeler birleştirilir.
        List_All_Tag = List_All_Tag + List_Entry_Tag
        #print(List_All_Tag)

Set_Tags = set(List_All_Tag)
List_Tag_Statistic = []
for tag in Set_Tags:
    Sum_Tag = List_All_Tag.count(tag)
    List_Tag_Statistic.append([Sum_Tag, tag])

List_Tag_Statistic.sort(reverse=True)
pprint(List_Tag_Statistic)
