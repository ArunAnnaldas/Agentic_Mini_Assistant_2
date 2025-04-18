from langchain.agents import initialize_agent, Tool
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
    

def calculator_tool(query: str) -> str:
    try:
        return str(eval(query))
    except Exception as e:
        return f"Error: {str(e)}"


def ai_student_advisor(_: str) -> str:
    return (
        "As an AI student, here are some things you can do today:\n"
        "1. Explore LangChain and build a simple agent.\n"
        "2. Learn prompt engineering.\n"
        "3. Take a mini project using OpenAI API.\n"
        "4. Watch a video on transformers or embeddings.\n"
        "5. Try building a chatbot using RAG architecture."
    )


tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for evaluating basic math expressions like '2 + 2' or '10 * 5'.",
        return_direct=True
    ),
    Tool(
        name="AIStudentAdvisor",
        func=ai_student_advisor,
        description="Gives advice and ideas on what an AI/ML student can work on.",
        return_direct=True
    )
]


llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
    openai_api_key=""
)


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# response = agent.run("My name is Arun. What would you suggest I do today as an AI student?")
response = agent.run("I want to calculate output of 2+2")
print("\n AI Suggestion:\n", response)