from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import re
import json

app = FastAPI()

# Enable CORS (allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/execute")
def execute(q: str = Query(...)):
    q = q.strip()

    # Ticket Status
    match = re.match(r"What is the status of ticket (\d+)\?", q)
    if match:
        ticket_id = int(match.group(1))
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": ticket_id
            })
        }

    # Meeting Scheduling
    match = re.match(
        r"Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.",
        q
    )
    if match:
        date, time, room = match.groups()
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": date,
                "time": time,
                "meeting_room": room
            })
        }

    # Expense Balance
    match = re.match(r"Show my expense balance for employee (\d+)\.", q)
    if match:
        employee_id = int(match.group(1))
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": employee_id
            })
        }

    # Performance Bonus
    match = re.match(
        r"Calculate performance bonus for employee (\d+) for (\d{4})\.",
        q
    )
    if match:
        employee_id, year = match.groups()
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(employee_id),
                "current_year": int(year)
            })
        }

    # Office Issue Reporting
    match = re.match(
        r"Report office issue (\d+) for the (.+) department\.",
        q
    )
    if match:
        issue_code, department = match.groups()
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue_code),
                "department": department
            })
        }

    return {
        "error": "Query not recognized"
    }