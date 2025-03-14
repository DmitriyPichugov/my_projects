import json
from main.models import Apartment

with open("cian_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    Apartment.objects.create(
        title=item["title"],
        rooms=item["rooms"],
        square=item["square"],
        price=item["price"],
        address=item["address"],
        district=item["district"],
        commission=item["commission"],
        deposit=item["deposit"],
        link=item["link"]
    )

print("Данные успешно загружены в базу!")
