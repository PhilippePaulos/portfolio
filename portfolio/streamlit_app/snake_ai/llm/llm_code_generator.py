import os
import re

import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import BaseModel
from pydantic import Field

dotenv.load_dotenv()

snake_prompt_path = os.path.join(os.path.dirname(__file__), "main_prompt.md")
with open(snake_prompt_path) as f:
    MAIN_PROMPT = f.read()


class SnakeCode(BaseModel):
    code: str = Field(description="Python code to play to the snake game")
    description: str = Field(description="Description of the code")


def get_strategy_from_llm(
    user_prompt: str, model: str, temperature: float
) -> SnakeCode:
    llm = ChatOpenAI(model_name=model, temperature=temperature).with_structured_output(
        SnakeCode
    )
    prompt = PromptTemplate(
        template="{main_prompt}\n\n{user_prompt}\n",
        input_variables=["main_prompt", "user_prompt"],
    )
    chain = prompt | llm
    result: SnakeCode = chain.invoke(
        {"main_prompt": MAIN_PROMPT, "user_prompt": user_prompt}
    )
    print(f"LLM response: \n{result}")

    return result


def _clean_generated_code(self, code: str) -> str:
    def extract_function_code(llm_response: str) -> str:
        pattern = r"def\s+\w+\(.*?\):.*"
        match = re.search(pattern, llm_response, re.DOTALL)

        if match:
            start = match.start()
            return llm_response[start:].strip()
        else:
            raise ValueError("No valid Python function found in the LLM response.")

    code = code.replace("```python", "").replace("```", "").strip()
    code = extract_function_code(code)
    return code
