import os
from ufc import app

if __name__ == "__main__":
    
    host = os.environ.get("IP", "127.0.0.1")
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", True)

    app.run(host=host, port=port, debug=debug)