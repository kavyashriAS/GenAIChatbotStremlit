import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from huggingface_hub import hf_hub_download

# Set your Hugging Face API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Load model and tokenizer from Hugging Face Hub
model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def get_chat_response(user_input):
    inputs = tokenizer([user_input], return_tensors="pt")
    reply_ids = model.generate(inputs["input_ids"])
    response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    return response
