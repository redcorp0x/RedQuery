import json
import sys
import config
import getpayload
import counter
import engine

def openfile():
    try:
        with open("redquery.restore", "r") as resumefile:
            data = json.load(resumefile)
        return data
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
    except FileNotFoundError:
        print("[WARN] Extraction was interrupted. File Not Found")
        sys.exit(1)
    except FileExistsError:
        print("[WARN] Extraction was interrupted. File exist error")
        sys.exit(1)
    except PermissionError:
        print("[WARN] Extraction was interrupted. File doesn't have read permission")
        sys.exit(1)


def load_resume():
    try:
        data = openfile()
        if config.enum == "table":
            config.schema_result = data["schema"][0]
        if config.enum == "column":
            config.schema_result = data["schema"][0]
            config.table_result = data["table"][0]
        if config.enum == "row":
            config.schema_result = data["schema"][0]
            config.table_result = data["table"][0]
            config.column_result = data["column"][0]
        if config.enum == "password":
            config.schema_result = data["schema"][0]
            config.table_result = data["table"][0]
            config.column_result = data["column"][0]
            config.row_result = data["row"][0]
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)


def resume_extraction():
    try:
        print("[!] Initializing Resume Mode...")
        print("[!] Resume Mode Started")
        if config.enum == "table":
            if config.schema_result is not None:
                table_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="table"))
                engine.heart(payload=getpayload.get_payload(extraction="table"),counts=table_count, extraction_type="table")
                
                if config.table_result is not None:
                    column_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="column"))
                    engine.heart(payload=getpayload.get_payload(extraction="column"),counts=column_count, extraction_type="column")
                    
                    if config.column_result is not None:
                        row_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="row"))
                        engine.heart(payload=getpayload.get_payload(extraction="row"),counts=row_count, extraction_type="row")
                
                        if config.row_result is not None:
                            password_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="password"))
                            engine.heart(payload=getpayload.get_payload(extraction="password"),counts=password_count, extraction_type="password")
            
        if config.enum == "column":
                if config.schema_result is not None and config.table_result is not None:
                    column_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="column"))
                    engine.heart(payload=getpayload.get_payload(extraction="column"),counts=column_count, extraction_type="column")
                        
                    if config.column_result is not None:
                        row_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="row"))
                        engine.heart(payload=getpayload.get_payload(extraction="row"),counts=row_count, extraction_type="row")
                    
                        if config.row_result is not None:
                            password_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="password"))
                            engine.heart(payload=getpayload.get_payload(extraction="password"),counts=password_count, extraction_type="password")
            
        if config.enum == "row":
            if config.schema_result is not None and config.table_result is not None and config.column_result is not None:  
                row_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="row"))
                engine.heart(payload=getpayload.get_payload(extraction="row"),counts=row_count, extraction_type="row")
                        
                if config.row_result is not None:
                    password_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="password"))
                    engine.heart(payload=getpayload.get_payload(extraction="password"),counts=password_count, extraction_type="password")
            
        if config.enum == "password":
            if config.schema_result is not None and config.table_result is not None and config.column_result is not None and config.row_result is not None:  
                password_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="password"))
                engine.heart(payload=getpayload.get_payload(extraction="password"),counts=password_count, extraction_type="password")
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1) 
 