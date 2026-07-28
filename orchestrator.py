from router import router_agent

from preparedness_agent import preparedness_agent
from emergency_agent import emergency_agent
from situation_agent import situation_agent
from planner import planner_agent
from reflection_agent import reflection_agent


def orchestrator(question):

    # Router returns structured AgentMessage
    route = router_agent(question)


    # Initial structured message
    message = {
        "sender": route.sender,
        "receiver": route.receiver,
        "task": route.task,
        "question": route.data["question"],
        "route": route.data["category"],
        "answer": "",
        "plan": ""
    }


    # Send task to selected agent
    if route.receiver == "Preparedness Agent":

        message["answer"] = preparedness_agent(
            message["question"]
        )


    elif route.receiver == "Emergency Agent":

        message["answer"] = emergency_agent(
            message["question"]
        )


    elif route.receiver == "Situation Agent":

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


    # Disaster Agent → Planner Agent
    planner_message = {
        "sender": route.receiver,
        "receiver": "Planner Agent",
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


    # Planner Agent → Reflection Agent
    reflection_message = {
        "sender": "Planner Agent",
        "receiver": "Reflection Agent",
        "task": "review_final_response",
        "content": combined_response
    }


    # Reflection receives structured message
    final_answer = reflection_agent(
        reflection_message
    )


    return final_answer



# Testing
if __name__ == "__main__":

    result = orchestrator(
        "My house is on fire, I need help"
    )

    print(result)