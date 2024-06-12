from project import create_app

DEVELOPMENT_PORT = 5000
HOST = "127.0.0.1"
DB_URI = "sqlite:///project.db"

app = create_app(DB_URI)

@app.route("/")
def root():
    return "GPS Tracker project"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=DEVELOPMENT_PORT, debug=True)