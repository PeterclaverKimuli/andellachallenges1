from app import app

# Runs the application
if __name__ == '__main__':
    app.secret_key = 'tSsjT4lW3Y4GfZYChYAThlGJevYvuDf0t'
    app.config['SESSION_TYPE'] = "filesystem"
    app.run(debug=True)