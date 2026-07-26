from ai.conversation import Conversation
from ai.context import Context
from ai.memory_manager import MemoryManager
from ai.intent_detector import IntentDetector
from ai.planner import Planner
from ai.reasoning import Reasoning
from ai.response_generator import ResponseGenerator
from ai.personality import Personality
from ai.prompts import SYSTEM_PROMPT
from ai.learning import Learning
from ai.summarizer import Summarizer


conversation = Conversation()

conversation.add_user("Hello")

conversation.add_assistant("Hi Captain!")

print(conversation.get_history())


context = Context()

context.set("app", "chrome")

print(context.get("app"))


memory = MemoryManager()

memory.remember("Captain likes coffee")

print(memory.recall())

detector = IntentDetector()

planner = Planner()

reasoning = Reasoning()


message = "Open Chrome"

intent = detector.detect(message)

print(intent)


plan = planner.create_plan(intent, message)

print(plan)


decision = reasoning.evaluate(plan)

print(decision)

generator = ResponseGenerator()

personality = Personality()

print(generator.generate(decision))

print(personality.introduce())

print(SYSTEM_PROMPT)

learning = Learning()

learning.learn("Captain prefers offline AI.")

print(learning.get_knowledge())

summarizer = Summarizer()

print(
    summarizer.summarize(
        conversation.get_history()
    )
)