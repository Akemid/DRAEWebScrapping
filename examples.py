from draews.draews import DRAEws as drae
from draews.models import MeaningList


drae = drae()

#Finding the meaning of a word
meaning_list: MeaningList = drae.find_word('gramatical')

# Obtaining the meaning on dictionary format 
meaning_dict = meaning_list.model_dump()
