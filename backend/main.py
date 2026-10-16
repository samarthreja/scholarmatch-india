
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from scholarships import scholarships, find_eligible_scholarships

app = FastAPI(
    title="ScholarMatch India API",
    description="Discover scholarships that match Indian students.",
    version="1.0.0"
)


# Student profile model
class StudentProfile(BaseModel):
    percentage: float = Field(ge=0, le=100)
    income: float = Field(ge=0)
    level: str = Field(min_length=1)


@app.get("/")
def home():
    return {
        "message": "Welcome to ScholarMatch India!",
        "status": "API is running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/scholarships")
def get_scholarships():
    return {
        "total": len(scholarships),
        "scholarships": scholarships
    }


@app.get("/scholarships/eligible")
def get_eligible_scholarships(
    percentage: float = Query(..., ge=0, le=100),
    income: float = Query(..., ge=0),
    level: str = Query(...)
):
    eligible = find_eligible_scholarships(
        percentage, income, level
    )

    return {
        "total": len(eligible),
        "scholarships": eligible
    }


@app.post("/students/profile")
def create_student_profile(profile: StudentProfile):
    return {
        "message": "Student profile received successfully",
        "profile": profile.model_dump()
    }





@app.post("/students/matches")
def get_student_matches(profile: StudentProfile):
    eligible = find_eligible_scholarships(
        profile.percentage,
        profile.income,
        profile.level
    )

    return {
        "message": "Scholarship matching completed",
        "total": len(eligible),
        "scholarships": eligible
    }
