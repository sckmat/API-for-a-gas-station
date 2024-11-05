from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пример модели для колонки (Pump)
class Pump(BaseModel):
    id: int
    fuel_type: str
    status: str
    price_per_liter: float

# Хранилище для данных о колонках
pumps = []

# Создание новой колонки
@app.post("/pumps/", response_model=Pump)
def create_pump(pump: Pump):
    pumps.append(pump)
    return pump

# Получение всех колонок
@app.get("/pumps/", response_model=List[Pump])
def read_pumps():
    return pumps

# Получение информации о конкретной колонке
@app.get("/pumps/{pump_id}", response_model=Pump)
def read_pump(pump_id: int):
    for pump in pumps:
        if pump.id == pump_id:
            return pump
    raise HTTPException(status_code=404, detail="Pump not found")

# Обновление информации о колонке
@app.put("/pumps/{pump_id}", response_model=Pump)
def update_pump(pump_id: int, updated_pump: Pump):
    for i, pump in enumerate(pumps):
        if pump.id == pump_id:
            pumps[i] = updated_pump
            return updated_pump
    raise HTTPException(status_code=404, detail="Pump not found")

# Удаление колонки
@app.delete("/pumps/{pump_id}")
def delete_pump(pump_id: int):
    for i, pump in enumerate(pumps):
        if pump.id == pump_id:
            del pumps[i]
            return {"message": "Pump deleted"}
    raise HTTPException(status_code=404, detail="Pump not found")
