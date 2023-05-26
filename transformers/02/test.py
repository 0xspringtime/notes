from datasets import list_datasets
from datasets import load_dataset
emotions = load_dataset("emotion")
import pandas as pd
emotions.set_format(type="pandas")
df = emotions["train"][:]
df.head()

import torch
import torch.nn.functional as F

from transformers import DistilBertTokenizer
distilbert_tokenizer = DistilBertTokenizer.from_pretrained(model_ckpt)
