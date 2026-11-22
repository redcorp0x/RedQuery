import config
from datetime import datetime
import json

def Category_save(category, results):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(config.filename, 'a') as file:
            file.write(f"\n{'='*15} {category.upper()} {'='*15}\n")
            file.write(f"Date: {timestamp}\n")
            for result in results:
                file.write(f"{result}\n")
    except PermissionError as e:
        print(f"Permission Error: {e}")
        
def General_Save():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(config.filename, 'a') as file:
            file.write(f"\n{'='*15} Process Updates {'='*15}\n")
            file.write("Extraction Process Completed\n")
            file.write(f"Date: {timestamp}\n")
    except PermissionError as e:
        print(f"Permission Error: {e}")
        
def save_resume():
    try:
        data = {
            "schema": [config.schema_result] if config.schema_result else [],
            "table": [config.table_result] if config.table_result else [],
            "column": [config.column_result] if config.column_result else [],
            "row": [config.row_result] if config.row_result else [],
            "password": [config.password_result] if config.password_result else []
        }
        
        with open("redquery.restore", "w") as file:
            json.dump(data,file,indent=4)
    except PermissionError as e:
        print(f"Permission Error: {e}")