
from api.routes import app

if __name__=="__main__":
    app.run(host='0.0.0.0', port=app.config.get("PORT"), debug=app.config.get("DEBUG"))