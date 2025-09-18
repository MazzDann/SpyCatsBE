import requests
from fastapi import HTTPException
# funny to see requests in be after using it for data scraping for two months

def validate_breed(breed: str) -> str:
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch breeds")
    breeds = [b["name"] for b in response.json()]
    if breed not in breeds:
        raise HTTPException(status_code=400, detail="Invalid cat breed")
    return breed