import asyncio
import uvicorn
from fastapi import FastAPI
import read_file

app = FastAPI()


@app.get("/")
async def process_data():
    await asyncio.sleep(0)

    data = read_file.read_file()
    sellers, customers, sales = read_file.filter_data(data)
    read_file.create_report(sellers, customers, sales)
    read_file.sales_per_salesman(sales)
    print(35 * '-')
    return {"message": "Data processed successfully."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
