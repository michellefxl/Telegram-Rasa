# Telegram-Rasa

Python script to run Telegram chatbot and send user input to Rasa.


### 1. To run Telegram chatbot:
```
python telegram_chatbot.py
```

### 2. To run Rasa:
1. run rasa model, set TF_FORCE_GPU_ALLOW_GROWTH to True: to prevent rasa nlu modules that uses gpu to take up entire gpu:
```
TF_FORCE_GPU_ALLOW_GROWTH=true rasa run -m models --enable-api --cors "*" --debug
```
2. run rasa custom actions. Note: for the current rasa model not needed
```
rasa run actions --cors "*" --debug
```

### To run multiple Rasa models:
```
TF_FORCE_GPU_ALLOW_GROWTH=true rasa run -m models --enable-api --cors "*" --debug --port {SET PORT NUMBER, e.g. 5006}
```

### To train Rasa model:
Navigate to the rasa_chatbot folder
```
rasa train
```

### Folder structure:
```
.
|
├── telegram_chatbot.py     # telegram chatbot 
├── rasa_chatbot            # rasa chatbot files
├── requirements.txt        # exported pip package list
├── environment.yml         # exported conda env package list 
└── README.md
```
