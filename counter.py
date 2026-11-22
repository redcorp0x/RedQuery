import request
import sys

def get_count(payloads):
    try:
        
        counts = 0
        limit_count = 0
        while True:
            contd = False
            final_payload = payloads.replace("{counter}", str(limit_count))
            value = request.dispatch_request(payload=final_payload)
            if value == True:
                counts += 1
                contd = True
            limit_count += 1
            if not contd:
                break
        return counts
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
        

