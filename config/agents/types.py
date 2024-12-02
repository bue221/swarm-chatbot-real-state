from swarm import Agent
from config.tools.tools import *
from config.tools.switchers import *
from config.prompts import *

# INDEPENDENT AGENTS --------------------------------
availability_agent = Agent(
    name="Availability Agent",
    instructions=availability_instructions,
    functions=[
        check_date_availability,
        get_available_slots,
        get_calendar_info,
        get_operating_hours,
        book_visit,
    ],
)

doubt_resolved_agent = Agent(
    name="Doubt Resolved Instructions",
    instructions=doubt_resolved_instructions,
    functions=[get_spot_data],
)

profiling_agent = Agent(
    name="Profiling Agent",
    instructions=profiling_instructions,
    functions=[],
)
# ---------------------------------------------------

# This is the orchestrator agent that will switch between the other agents
triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions,
    functions=[
        switch_to_availability_agent,
        switch_to_doubt_resolver_agent,
        switch_to_profiling_agent,
        get_spot_data,
    ],
)
