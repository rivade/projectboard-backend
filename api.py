from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import validation


class ProjectCreate(BaseModel):
    """Model for creating a new project"""
    title: str = Field(min_length=3)
    description: str
    status: Literal["planned", "active", "done"]


def init():
    """Initialize and configure the FastAPI application"""
    app = FastAPI(title="API-bron")
    
    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # In-memory storage (replace with database calls)
    projects = []
    
    @app.get("/")
    def home():
        """Health check endpoint"""
        return {"message": "API-bron fungerar"}
    
    @app.get("/api/projects")
    def get_projects():
        """Retrieve all projects"""
        return projects
    
    @app.post("/api/projects", status_code=201)
    def create_project(project: ProjectCreate):
        """Create a new project"""
        new_project = {
            "id": len(projects) + 1,
            **project.model_dump()
        }
        projects.append(new_project)
        return new_project
    
    return app