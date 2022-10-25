# Telegram-Rasa

Python script to run Telegram chatbot and communicate user input to Rasa

### Create conda env for Telegram and Rasa:
```
conda env create -n ENVNAME --file ENV.yml
```

### 1. To run Telegram chatbot:
Activate conda environment
```
conda activate TELEGRAM_ENVNAME
```
Create Telegram chatbot and get Bot token: [link](https://core.telegram.org/bots#how-do-i-create-a-bot) Note: Insert token on line 90
```
python telegram_chatbot.py
```

### 2. To run Rasa:
Activate conda environment
```
conda activate RASA_ENVNAME
```
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

### Interaction with chatbot:
1. in Telegram chat with bot, start conversation with "/start": creates new conversation log folder for logging

### Folder structure:
```
.
|
├── telegram_chatbot.py       # telegram chatbot 
├── rasa_chatbot              # rasa chatbot files
├── environment_rasa.yml      # exported rasa conda env package list
├── environment_telegram.yml  # exported telegram conda env package list 
└── README.md
```
