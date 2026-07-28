from router import router_agent

from preparedness_agent import preparedness_agent
from emergency_agent import emergency_agent
from situation_agent import situation_agent
from planner import planner_agent
from reflection_agent import reflection_agent


def orchestrator(question):

    # Router decides which agent handles the request
    route = router_agent(question)


    # Initial structured message
    message = {
        "sender": "RouterAgent",
        "receiver": route + "Agent",
        "task": "handle_disaster_query",
        "question": question,
        "route": route,
        "answer": "",
        "plan": ""
    }


    # Send task to selected agent
    if route == "Preparedness":

        message["answer"] = preparedness_agent(
            message["question"]
        )


    elif route == "Emergency":

        message["answer"] = emergency_agent(
            message["question"]
        )


    elif route == "Situation":

        message["answer"] = situation_agent(
            message["question"]
        )


    else:
        return (
            "Sorry, I can only answer disaster management questions.\n\n"
            "You can ask me about:\n"
            "• Disaster preparedness\n"
            "• Emergency response\n"
            "• Disaster situations"
        )


    # Agent-to-agent structured message:
    # Disaster Agent → Planner Agent
    planner_message = {
        "sender": route + "Agent",
        "receiver": "PlannerAgent",
        "task": "create_action_plan",
        "content": {
            "question": message["question"],
            "answer": message["answer"]
        }
    }


    # Planner receives structured message
    message["plan"] = planner_agent(
        planner_message
    )


    # Combine outputs
    combined_response = f"""
{message['answer']}


==============================
Recommended Action Plan
==============================

{message['plan']}
"""


    # Agent-to-agent structured message:
    # Planner Agent → Reflection Agent
    reflection_message = {
        "sender": "PlannerAgent",
        "receiver": "ReflectionAgent",
        "task": "review_final_response",
        "content": combined_response
    }


    # Reflection receives message content
    final_answer = reflection_agent(
        reflection_message
    )


    return final_answer