# DRAEWebScrapping
A proyect to find words from the web page of Real Academia Española 

[![Downloads](https://static.pepy.tech/badge/draews)](https://pepy.tech/project/draews)
[![Downloads](https://static.pepy.tech/badge/draews/month)](https://pepy.tech/project/draews)
[![Downloads](https://static.pepy.tech/badge/draews/week)](https://pepy.tech/project/draews)
# Usage
A simple example to find a word

```
from draews.draews import DRAEws as drae    
from draews.models import MeaningList 

drae = drae() 

# Finding the meaning of a word 
meaning_list: MeaningList = drae.find_word("sustantivo")

# Obtaining the meaning on dictionary format
meaning_dict = meaning_list.model_dump()
```
