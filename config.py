import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6325577627:AAEJ3fKnszJrVv8CrcfWIusR-iojxFBdH50")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20648127"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ddb67c85c65a2af745fe9d9ea7cfcd77")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://starboy:shivanshudeo@starboy.ht38vde.mongodb.net/?retryWrites=true&w=majority")
