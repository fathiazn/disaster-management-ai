from message_schema import AgentMessage


def router_agent(question):
    """
    Routes a user's question to the correct agent.

    Returns:
        AgentMessage object containing:
        sender
        receiver
        task
        data
        status
    """

    question = question.lower().strip()


    # -----------------------------
    # Emergency keywords
    # -----------------------------
    emergency_words = [
        "fire",
        "house is on fire",
        "earthquake",
        "tsunami",
        "rescue",
        "ambulance",
        "injured",
        "bleeding",
        "collapsed",
        "accident",
        "explosion",
        "help",
        "emergency",
        "trapped",
        "flood rescue",
        "cyclone",
        "storm surge"
    ]


    # -----------------------------
    # Situation keywords
    # -----------------------------
    situation_words = [
        "road",
        "street",
        "bridge",
        "blocked",
        "flooded",
        "landslide",
        "location",
        "galle road",
        "i'm on",
        "i am on",
        "i'm at",
        "i am at",
        "where am i",
        "traffic",
        "route",
        "highway",
        "river level",
        "weather here",
        "my area",
        "current situation"
    ]


    # -----------------------------
    # Preparedness keywords
    # -----------------------------
    preparedness_words = [
        "prepare",
        "preparedness",
        "preparation",
        "ready",
        "get ready",
        "ready for",
        "how to ready",
        "how to prepare",

        "emergency kit",
        "kit",
        "first aid",
        "survival",
        "safety",
        "safe",

        "evacuation plan",
        "disaster plan",
        "disaster preparation",

        "before a flood",
        "flood preparation",
        "flood preparedness",

        "before an earthquake",
        "earthquake preparation",

        "before a tsunami",
        "tsunami preparation",

        "before a cyclone",
        "cyclone preparation",

        "before a disaster",

        "supplies",
        "food storage",
        "water storage",
        "checklist",
        "emergency bag",
        "go bag"
    ]


    # -----------------------------
    # Emergency Routing
    # -----------------------------
    for word in emergency_words:
        if word in question:

            return AgentMessage(
                sender="Router Agent",
                receiver="Emergency Agent",
                task="Handle emergency request",
                data={
                    "question": question,
                    "category": "Emergency"
                }
            )


    # -----------------------------
    # Situation Routing
    # -----------------------------
    for word in situation_words:
        if word in question:

            return AgentMessage(
                sender="Router Agent",
                receiver="Situation Agent",
                task="Analyze current situation",
                data={
                    "question": question,
                    "category": "Situation"
                }
            )


    # -----------------------------
    # Preparedness Routing
    # -----------------------------
    for word in preparedness_words:
        if word in question:

            return AgentMessage(
                sender="Router Agent",
                receiver="Preparedness Agent",
                task="Provide preparedness guidance",
                data={
                    "question": question,
                    "category": "Preparedness"
                }
            )


    # -----------------------------
    # Unknown
    # -----------------------------
    return AgentMessage(
        sender="Router Agent",
        receiver="Unknown",
        task="No suitable agent found",
        data={
            "question": question,
            "category": "Unknown"
        }
    )


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    result = router_agent(
        "My house is on fire, I need help"
    )

    print(result)