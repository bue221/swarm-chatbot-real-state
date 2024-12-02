from config.agents.types import *
from config.data.context_variables import context_variables
from swarm.repl import run_demo_loop
from swarm import Swarm

import config.db.sqlite as database

# Initialize the database
database.initialize_database()

# Define the client
client = Swarm()

if __name__ == "__main__":
    run_demo_loop(
        triage_agent,
        debug=False,
        stream=True,
        context_variables=context_variables,
    )
    # response = client.run(
    #     agent=triage_agent,
    #     messages=[{"role": "user", "content": "Hello I am search a spot."}],
    # )
    # print(response)
