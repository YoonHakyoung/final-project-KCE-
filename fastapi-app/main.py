from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import subprocess

from . import models, crud, database, config

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def get_test_html():
    return FileResponse("static/index.html")

@app.get("/{test_id}/execute")
async def get_runner_html(test_id: int):
    return FileResponse("static/runner.html")

@app.get("/testcase")
async def read_list(db: Session = Depends(database.get_db)):
    try:
        tests = crud.get_tests(db)
        test_data = [{"test_id": test.test_id, "test_name": test.test_name} for test in tests]
        return {"testData": test_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/testcase")
async def create_test(data: models.TestData, db: Session = Depends(database.get_db)):
    try:
        test = crud.create_test(db, data)
        return {"test_id": test.test_id, "test_name": test.test_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.delete("/testcase/{test_id}")
async def delete_test(test_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_test(db, test_id)
        return {"message": "Test deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

def run_load_testing_script(url, initial_user_count, additional_user_count, interval_time, repeat_count, test_id):
    command = [
        "python",
        "runner.py",
        "--url", url,
        "--initial_user_count", str(initial_user_count),
        "--additional_user_count", str(additional_user_count),
        "--interval_time", str(interval_time),
        "--repeat_count", str(repeat_count),
        "--test_id", str(test_id)
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

@app.get("/testcase/{test_id}/execute/")
async def execute_test(test_id: int, db: Session = Depends(database.get_db)):
    try:
        test_data = crud.get_test_by_id(db, test_id)
        if test_data:
            run_load_testing_script(
                test_data.target_url, 
                test_data.user_num, 
                test_data.user_plus_num, 
                test_data.interval_time, 
                test_data.plus_count, 
                test_id
            )
            return {
                "test_id": test_data.test_id,
                "target_url": test_data.target_url,
                "test_name": test_data.test_name,
                "user_num": test_data.user_num,
                "user_plus_num": test_data.user_plus_num,
                "interval_time": test_data.interval_time,
                "plus_count": test_data.plus_count,
            }
        else:
            raise HTTPException(status_code=404, detail="Testcase not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
