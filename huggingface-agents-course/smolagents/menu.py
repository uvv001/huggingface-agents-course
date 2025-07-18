from smolagents import CodeAgent, tool
from helpers import ArgumentsHelper, register_opentelemetry_through_langfuse

register_opentelemetry_through_langfuse()

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

def main():
    # Alfred, the butler, preparing the menu for the party
    agent = CodeAgent(tools=[suggest_menu], model=ArgumentsHelper().getModel())

    # Preparing the menu for the party
    agent.run("Prepare a formal menu for the party.")


if __name__ == "__main__":
    main()

    