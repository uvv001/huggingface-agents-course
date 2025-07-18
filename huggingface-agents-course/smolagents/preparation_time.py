from smolagents import CodeAgent
from helpers import ArgumentsHelper, register_opentelemetry_through_langfuse

register_opentelemetry_through_langfuse()

def main():
    agent = CodeAgent(tools=[], model=ArgumentsHelper().getModel(), additional_authorized_imports=['datetime'])
    agent.run(
        """
        Alfred needs to prepare for the party. Here are the tasks:
        1. Prepare the drinks - 30 minutes
        2. Decorate the mansion - 60 minutes
        3. Set up the menu - 45 minutes
        4. Prepare the music and playlist - 45 minutes

        If we start right now, at what time will the party be ready?
        """
    )


if __name__ == "__main__":
    main()