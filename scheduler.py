import os
import requests
from datetime import datetime, timedelta
from config import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, BOARD_ID, IMAGE_FOLDER

def upload_pin(image_path: str, description: str, schedule_time: int = None) -> dict:
    """Загружает пин на Pinterest."""
    url = "https://api.pinterest.com/v5/pins"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Загрузите изображение на Pinterest
    with open(image_path, "rb") as image_file:
        image_upload = requests.post(
            "https://api.pinterest.com/v5/media",
            headers=headers,
            files={"file": image_file}
        )
    
    media_id = image_upload.json()["media_id"]
    
    # Создайте пин
    payload = {
        "board_id": BOARD_ID,
        "media_source": {
            "source_type": "media_upload",
            "media_id": media_id
        },
        "description": description,
        "title": os.path.basename(image_path).split(".")[0],
    }
    
    if schedule_time:
        payload["scheduled_at"] = schedule_time
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def schedule_pins():
    """Планирует публикацию 10 пинов с интервалом в 1 день."""
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith((".jpg", ".png"))]
    
    for i, image in enumerate(images[:10]):
        image_path = os.path.join(IMAGE_FOLDER, image)
        description = f"Автоматический пин: {image}"
        
        # Установите время публикации (через i дней)
        schedule_time = datetime.now() + timedelta(days=i)
        schedule_timestamp = int(schedule_time.timestamp())
        
        # Загрузите пин
        result = upload_pin(image_path, description, schedule_timestamp)
        print(f"Пин {image} запланирован на {schedule_time} | Ответ: {result}")

if __name__ == "__main__":
    schedule_pins()
