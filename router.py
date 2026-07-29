from message_schema import AgentMessage


def router_agent(question):
    question = question.lower().strip()

    emergency_words = [
        "fire", "house is on fire", "earthquake", "tsunami", "rescue",
        "ambulance", "injured", "bleeding", "collapsed", "accident",
        "explosion", "trapped", "flood rescue", "cyclone",
        "storm surge", "need help now", "send help", "this is an emergency"
    ]

    situation_words = [
        "road", "street", "bridge", "blocked", "flooded", "landslide",
        "location", "galle road", "i'm on", "i am on", "i'm at", "i am at",
        "where am i", "traffic", "route", "highway", "river level",
        "weather here", "my area", "current situation"
    ]

    preparedness_words = [
        "prepare", "preparedness", "preparation", "ready", "get ready",
        "ready for", "how to ready", "how to prepare", "emergency kit",
        "kit", "first aid", "survival", "safety", "safe",
        "evacuation plan", "disaster plan", "disaster preparation",
        "before a flood", "flood preparation", "flood preparedness",
        "before an earthquake", "earthquake preparation",
        "before a tsunami", "tsunami preparation",
        "before a cyclone", "cyclone preparation", "before a disaster",
        "supplies", "food storage", "water storage", "checklist",
        "emergency bag", "go bag"
    ]

    for word in emergency_words:
        if word in question:
            return AgentMessage(
                sender="Router Agent", receiver="Emergency Agent",
                task="Handle emergency request",
                data={"question": question, "category": "Emergency"}
            )

    for word in situation_words:
        if word in question:
            return AgentMessage(
                sender="Router Agent", receiver="Situation Agent",
                task="Analyze current situation",
                data={"question": question, "category": "Situation"}
            )

    for word in preparedness_words:
        if word in question:
            return AgentMessage(
                sender="Router Agent", receiver="Preparedness Agent",
                task="Provide preparedness guidance",
                data={"question": question, "category": "Preparedness"}
            )

    return AgentMessage(
        sender="Router Agent", receiver="Preparedness Agent",
        task="No specific category matched; provide general guidance",
        data={"question": question, "category": "Unknown"}
    )


if __name__ == "__main__":
    result = router_agent("My house is on fire, I need help")
    print(result)

    result2 = router_agent("Can you help me prepare an emergency kit")
    print(result2)
