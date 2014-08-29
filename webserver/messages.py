import random

occupied_messages = [
    "Wait your turn.", 
    "Get back to work.",
    "Hopefully not for too much longer...",
    "Saved you a walk over there.",
]

vacant_messages = [
    "It's calling your name!", 
    "Boomshakalaka!",
    "Nature abhors a vaccuum.",
    "Isn't your workplace the best?",
]

def current_message(occupied):
    if occupied:
        return random.choice(occupied_messages)
    else:
        return random.choice(vacant_messages)
