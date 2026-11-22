import config
import checkers
import resume
import sys

def sub_mainer():
    try:
        if config.resume and config.enum is not None and config.enum != "schema":
            resume.load_resume()
            resume.resume_extraction()
        else:
            checkers.check()
    except KeyboardInterrupt:
        print("[WARN] Extraction was interrupted Ctrl-C")
        sys.exit(1)
        
        