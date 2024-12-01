from config.agents.types import *
from swarm.repl import run_demo_loop

if __name__ == "__main__":
    run_demo_loop(triage_agent, debug=False, stream=True)
