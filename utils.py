# -*- coding: utf-8 -*-

"""
Installation
     pip install googletrans
"""

import pandas as pd
import pickle as pkl
import re
from googletrans import Translator


def split_sentence(sent):
    middle = int(len(sent)/2)
    while sent[middle] != ' ':
        middle -= 1
    sent1 = sent[:middle]
    sent2 = sent[middle:]
    return sent1, sent2
    
def translete_sent_splited(part1, part2, translator):
    translation_1 = translator.translate(part1)
    translation_2 = translator.translate(part2)
    return translation_1 +' '+ translation_2

def dump_object(dic, dump_sentence_not_translation):
      pkl.dump(dic, open(dump_sentence_not_translation, 'wb'))

def translete_data_from(datas_path, name_seved_datas='translete_test.csv', 
                dump_sentence_not_translation='sentence_not_translation.p'):
    train = pd.read_csv(datas_path, header=None)
    train = train.dropna()

    titles = train[1]
    comments = train[2]
    translator = Translator()
    
    counters = 0
    indexs = []
    sentences = []
    print 'Init...'
    for i, v in enumerate(titles, start=0):
          origin = 'Error index'
          try:
            title = titles[i]
            comment = comments[i]
            origin = text = title + ' ' + comment
            text = re.sub(r",{2,}", ',', text)  
            text = translator.translate(text, dest='pt').text
            train[1][i] =  text
            if i % 10 == 0:
                train.to_csv(name_seved_datas, index=False, header=False)
                print 'Saved - {}'.format(i)
          except:
            counters += 1  
            indexs.append(i)
            sentences.append(origin)
            dic_excpt = {indexs: indexs, sentences: sentences, counters: counters}
            dump_object(dic_excpt, dump_sentence_not_translation)
            print '\n{}: {}|'.format(i, origin)
            raise

    train.to_csv(name_seved_datas, index=False, header=False)
    dic = {indexs: indexs, sentences: sentences, counters: counters}
    dump_object(dic, dump_sentence_not_translation)
    print 'Ended'