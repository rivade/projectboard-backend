from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import mongo


class ProjectCreate(BaseModel):
    """Model for creating a new project"""
    title: str = Field(min_length=3)
    description: str
    status: Literal["planned", "active", "done"]


def init():
    """Initialize and configure the FastAPI application"""
    app = FastAPI(title="ProjectBoard API")
    
    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    @app.get("/")
    def home():
        """Health check endpoint"""
        return {"message": "API-bron fungerar"}
    
    @app.get("/api/projects")
    def get_projects():
        """Retrieve all projects"""
        return mongo.get_projects()
    
    @app.post("/api/projects", status_code=201)
    def create_project(project: ProjectCreate):
        """Create a new project"""
        return mongo.post_project(project.model_dump())
    
    return app