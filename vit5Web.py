# from flask import Flask, render_template, request
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from transformers import __version__ as transformers_version
# import torch

# # print("PyTorch version:", torch.__version__)
# # print("Transformers version:", transformers_version)

# app = Flask(__name__)

# MODEL_NAME = "VietAI/vit5-base-vietnews-summarization"

# # Load tokenizer
# viT5_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# # Create an instance of the model (without loading weights)
# viT5_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# model_checkpoint_path = "model_checkpoint.pth"
# checkpoint = torch.load(model_checkpoint_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
# # print(checkpoint.keys())
# model_state_dict = checkpoint.get("model_state_dict", checkpoint)
# state_dict = {k[6:]: v for k, v in model_state_dict.items()}
# viT5_model.load_state_dict(state_dict)

# optimizer = torch.optim.AdamW(viT5_model.parameters())
# optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
# epoch = checkpoint['epoch']
# val_loss = checkpoint['val_loss']

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# viT5_model.to(device)
# viT5_model.eval()

# def vit5_generate_summary_short(model, tokenizer, input_text, max_length):
#      if not input_text or not max_length:
#         return  "Please enter news you want to summarize"
#      elif len(input_text) < 100:
#         return "Please enter more words about the new"
#      else:
#           # Encode the input text and move tensors to the specified device
#           inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
#           inputs = {key: value.to(device) for key, value in inputs.items()}

#           # Add attention_mask
#           inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

#           # Generate summary on the specified device
#           summary_ids = model.generate(**inputs, max_length=max_length, min_length=50 ,num_beams=2, repetition_penalty=3.0, length_penalty=1.0, early_stopping=True)
          
#           # Move summary_ids back to CPU for decoding if necessary
#           summary_ids = summary_ids.to("cpu")

#           # Decode and return the summary
#           summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
          
#           # Split summary into sentences
#           sentences = summary.split(". ")

#           # Join sentences back to form the final summary
#           final_summary = '. '.join(sentences[:-1]) + '.'
          
#           return final_summary

# def vit5_generate_summary_medium(model, tokenizer, input_text, max_length):
#    # Encode the input text and move tensors to the specified device
#      if not input_text or not max_length:
#         return "Please enter news you want to summarize"
#      elif len(input_text) < 100:
#         return "Please enter more words about the new"
#      else:
#           inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
#           inputs = {key: value.to(device) for key, value in inputs.items()}

#           # Add attention_mask
#           inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

#           # Generate summary on the specified device
#           summary_ids = model.generate(**inputs, max_length=max_length, min_length=150 ,num_beams=2, repetition_penalty=3.0, length_penalty=1.0, early_stopping=True)
          
#           # Move summary_ids back to CPU for decoding if necessary
#           summary_ids = summary_ids.to("cpu")

#           # Decode and return the summary
#           summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
          
#           # Split summary into sentences
#           sentences = summary.split(". ")

#           # Join sentences back to form the final summary
#           final_summary = '. '.join(sentences[:-1]) + '.'
          
#           return final_summary

# def vit5_generate_summary_long(model, tokenizer, input_text, max_length):
#      if not input_text or not max_length:
#           return  "Please enter news you want to summarize"
#      elif len(input_text) < 100:
#         return "Please enter more words about the new"
#      else:
#           # Encode the input text and move tensors to the specified device
#           inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
#           inputs = {key: value.to(device) for key, value in inputs.items()}

#           # Add attention_mask
#           inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

#           # Generate summary on the specified device
#           summary_ids = model.generate(**inputs, max_length=max_length, min_length=250 ,num_beams=2, repetition_penalty=3.0, length_penalty=1.0, early_stopping=True)
          
#           # Move summary_ids back to CPU for decoding if necessary
#           summary_ids = summary_ids.to("cpu")

#           # Decode and return the summary
#           summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
          
#           # Split summary into sentences
#           sentences = summary.split(". ")

#           # Join sentences back to form the final summary
#           final_summary = '. '.join(sentences[:-1]) + '.'
          
#           return final_summary





from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import __version__ as transformers_version
import torch

app = Flask(__name__)

MODEL_NAME = "VietAI/vit5-base-vietnews-summarization"

# Load tokenizer
viT5_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Create an instance of the model (without loading weights)
viT5_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model_checkpoint_path = "model_checkpoint.pth"
checkpoint = torch.load(model_checkpoint_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
# print(checkpoint.keys())
model_state_dict = checkpoint.get("model_state_dict", checkpoint)
state_dict = {k[6:]: v for k, v in model_state_dict.items()}
viT5_model.load_state_dict(state_dict)

optimizer = torch.optim.AdamW(viT5_model.parameters())
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
val_loss = checkpoint['val_loss']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
viT5_model.to(device)
viT5_model.eval()

def vit5_generate_summary_short(model, tokenizer, input_text, max_length):
     if not input_text or not max_length:
          return  "Please enter news you want to summarize"
     elif len(input_text) < 100:
        return "Please enter more words about the new"
     else:
      # Encode the input text and move tensors to the specified device
      inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
      inputs = {key: value.to(device) for key, value in inputs.items()}

      # Add attention_mask
      inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

      # Generate summary on the specified device
      summary_ids = model.generate(**inputs, max_length=max_length, min_length=50 ,num_beams=2, repetition_penalty=2.0, length_penalty=1.0, early_stopping=True)
      
      # Move summary_ids back to CPU for decoding if necessary
      summary_ids = summary_ids.to("cpu")

      # Decode and return the summary
      summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
      
      # Split summary into sentences
      sentences = summary.split(". ")

      # Join sentences back to form the final summary
      final_summary = '. '.join(sentences[:-1]) + '.'
      
      return final_summary

def vit5_generate_summary_medium(model, tokenizer, input_text, max_length):
     if not input_text or not max_length:
          return  "Please enter news you want to summarize"
     elif len(input_text) < 100:
        return "Please enter more words about the new"
     else:
      # Encode the input text and move tensors to the specified device
      inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
      inputs = {key: value.to(device) for key, value in inputs.items()}

      # Add attention_mask
      inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

      # Generate summary on the specified device
      summary_ids = model.generate(**inputs, max_length=max_length, min_length=100 ,num_beams=2, repetition_penalty=2.0, length_penalty=1.0, early_stopping=True)
      
      # Move summary_ids back to CPU for decoding if necessary
      summary_ids = summary_ids.to("cpu")

      # Decode and return the summary
      summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
      
      # Split summary into sentences
      sentences = summary.split(". ")

      # Join sentences back to form the final summary
      final_summary = '. '.join(sentences[:-1]) + '.'
      
      return final_summary

def vit5_generate_summary_long(model, tokenizer, input_text, max_length):
    
     if not input_text or not max_length:
          return  "Please enter news you want to summarize"
     elif len(input_text) < 100:
        return "Please enter more words about the new"
     else:
      # Encode the input text and move tensors to the specified device
      inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, return_attention_mask = True, add_special_tokens = True)
      inputs = {key: value.to(device) for key, value in inputs.items()}

      # Add attention_mask
      inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)

      # Generate summary on the specified device
      summary_ids = model.generate(**inputs, max_length=max_length, min_length=200 ,num_beams=2, repetition_penalty=2.0, length_penalty=1.0, early_stopping=True)
      
      # Move summary_ids back to CPU for decoding if necessary
      summary_ids = summary_ids.to("cpu")

      # Decode and return the summary
      summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
      
      # Split summary into sentences
      sentences = summary.split(". ")

      # Join sentences back to form the final summary
      final_summary = '. '.join(sentences[:-1]) + '.'
      
      return final_summary