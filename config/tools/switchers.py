def switch_to_availability_agent():
    from config.agents.types import availability_agent

    return availability_agent


def switch_to_doubt_resolver_agent():
    from config.agents.types import doubt_resolved_agent

    return doubt_resolved_agent


def switch_to_profiling_agent():
    from config.agents.types import profiling_agent

    return profiling_agent
