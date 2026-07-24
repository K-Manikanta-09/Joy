from enum import Enum


class Provider(Enum):

    OLLAMA = "ollama"

    OPENAI = "openai"

    GEMINI = "gemini"

    CLAUDE = "claude"