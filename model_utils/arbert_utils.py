import sys
sys.path.insert(1,"G:\Gender_ReWriting")
from transformers import AutoTokenizer, AutoModel
from arabert.preprocess import ArabertPreprocessor


model_name = "aubmindlab/bert-base-arabertv2"
arabert_tokenizer = AutoTokenizer.from_pretrained(model_name)
arabert_model = AutoModel.from_pretrained(model_name)

arabert_prep = ArabertPreprocessor(model_name=model_name)

text = "ولن نبالغ إذا قلنا إن هاتف أو كمبيوتر المكتب في زمننا هذا ضروري"
print(arabert_prep.preprocess(text))

