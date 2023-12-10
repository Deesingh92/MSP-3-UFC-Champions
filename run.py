import os
from ufc import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
        secret_key=os.environ.get("SECRET_KEY", "your_secret_key_here")
    )