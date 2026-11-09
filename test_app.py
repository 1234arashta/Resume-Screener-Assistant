import pytest
from pydantic import ValidationError
from app import MatchReport

def test_report_valid():
    report=MatchReport(match_score=72,
      matching_skills=["Python","SQL","Excel","Communication","Analytics"],
      skill_gaps=["Cloud","Docker","Deployment"],
      interview_questions=["Q1","Q2","Q3"])
    assert report.match_score == 72

def test_score_out_of_range():
    with pytest.raises(ValidationError):
        MatchReport(match_score=101,matching_skills=["a"]*5,
                    skill_gaps=["b"]*3,interview_questions=["c"]*3)
