from base import *

printh("<span style='color:green'>Importing paraphrase code: 0%</span>")
with io.capture_output() as captured:
  subprocess.call("pip install transformers", shell=True)

printh("<span style='color:green'>Importing paraphrase code: 50%</span>",True)
with io.capture_output() as captured:
  from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  
  model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")
  model.to("cuda")
  model.eval()

printh("<span style='color:green'>Importing paraphrase code: 100%</span>",True)

def paraphrase_sent(sentence):
  text =  "paraphrase: " + sentence + " </s>"
  encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
  input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")

  outputs = model.generate(
      input_ids=input_ids, attention_mask=attention_masks,
      max_length=256,
      do_sample=True,
      top_k=300,
      top_p=0.99,
      early_stopping=True,
      num_return_sequences=10
      #repetition_penalty=1.0
  )
  #top_k = 120 and top_p = 0.95
 
  r = []
  printh("Current sentence: "+sentence)
  for i,output in enumerate(outputs):
      line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
      r.append(line)
      printh(str(i+1)+": "+line)

  return r

def paraphrase(paragraph):
  sentences = paragraph.split(". ")
  output = []
  temp = []
  for i,sentence in enumerate(sentences):
    printh("Paraphrasing sentence "+str(i+1))
    temp = [sentence] + paraphrase_sent(sentence)
    output.append(temp)
    printh("")
  return output
