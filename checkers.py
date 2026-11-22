import config
import counter
import engine
import getpayload
import sys

def check():
    try:
        schema_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="schema"))
        if schema_count:
            payload = getpayload.get_payload(extraction="schema")
            engine.heart(payload=payload, counts=schema_count, extraction_type="schema")
            
            #START TABLE EXTRACTION WHEN SCHEMA IS DONE AND CONFIG.SCHEMA_RESULT IS NOT NONE
            if config.schema_result is not None:
                table_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="table"))
                payload = getpayload.get_payload(extraction="table")
                engine.heart(payload=payload, counts=table_count, extraction_type="table")
                
                #START COLUMN EXTRACTION WHEN TABLE IS DONE AND CONFIG.TABLE_RESULT IS NOT NONE
                if config.table_result is not None:
                    column_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="column"))
                    payload = getpayload.get_payload(extraction="column")
                    engine.heart(payload=payload, counts=column_count, extraction_type="column")
                    
                    #START ROW EXTRACTION WHEN COLUMN IS DONE AND CONFIG.COLUMN_RESULT IS NOT NONE
                    if config.column_result is not None:
                        row_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="row"))
                        payload = getpayload.get_payload(extraction="row")
                        engine.heart(payload=payload, counts=row_count, extraction_type="row")
                       
                        #START ROW EXTRACTION WHEN COLUMN IS DONE AND CONFIG.COLUMN_RESULT IS NOT NONE
                        if config.row_result is not None:
                            passwd_count = counter.get_count(payloads=getpayload.get_counter_payoad(extraction="password"))
                            payload = getpayload.get_payload(extraction="password")
                            engine.heart(payload=payload, counts=passwd_count, extraction_type="password")
        sys.exit(1)
                        
                    #THE PROGRAM ENDS HERE, IT WILL TERMINATE BY ITSELF IN THE PASSWORD FUNCTION
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
        
    