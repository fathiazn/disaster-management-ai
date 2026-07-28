def router_agent(question):
    """
    Routes a user's question to the correct agent.

    Returns:
        "Emergency"
        "Situation"
        "Preparedness"
        "Unknown"
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


    # Check Emergency
    for word in emergency_words:
        if word in question:
            return "Emergency"


    # Check Situation
    for word in situation_words:
        if word in question:
            return "Situation"


    # Check Preparedness
    for word in preparedness_words:
        if word in question:
            return "Preparedness"


    return "Unknown"