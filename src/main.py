from typing import Union
from fastapi import FastAPI

app = FastAPI()
 
import debugpy
debugpy.listen(("0.0.0.0", 5678))

class Pancake:
    def __init__(self, cook_time, radius, location):
        self.cook_time, self.radius, self.location = cook_time, radius, location
        pass
    
    def eu_us(self):
        if (self.location == "eu"):
            return "the pancake is from EU"
        elif (self.location == "us"):
            return "the pancake is from US"


@app.get("/")
def read_item():
    food = Pancake(200, 20, "us")
    return {"food": food.location, "location": food.eu_us(), "cook_time": food.cook_time, "radius": food.radius}
