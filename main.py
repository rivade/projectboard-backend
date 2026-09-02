import mongo
import api
import uvicorn

if __name__ == "__main__":
    # Initialize MongoDB
    mongo.init()
    mongo.test_connection()
    
    # Initialize FastAPI app
    app = api.init()
    
    # Start server
    uvicorn.run(app, port=8001)