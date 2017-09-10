# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import utils


datas_path = 'datas_transletion/2translete_train.csv'
save_name_csv = 'datas_transletion/3translete_train.csv'
dump_errors = 'datas_transletion/3sentence_not_translation_train.p'

'''
datas_path = 'datas_transletion/translete_test.csv'
save_name_csv = 'datas_transletion/1translete_test.csv'
dump_errors = 'datas_transletion/1sentence_not_translation_test.p'
'''

print datas_path
utils.translete_data_from(datas_path, name_seved_datas=save_name_csv, dump_sentence_not_translation=dump_errors)