from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

class LLMService:
    def __init__(self, config):
        self.config = config
        self.llm = ChatOpenAI(
            model_name=config.GPT_MODEL,
            temperature=0,
            api_key=config.OPENAI_API_KEY
        )

    def get_suggestion(self, raw_transcription: list) -> list:
        """Filter redundant segments using LLM"""
        response_schemas = [
            ResponseSchema(
                name="filtered_transcription",
                description=(
                    "A list of transcription segments to keep, in chronological order. "
                    "Each segment is an object with 'start' (number, seconds), "
                    "'end' (number, seconds), and 'text' (string)."
                )
            )
        ]
        
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt = (
            "You are given a raw JSON transcription of a video as an array of objects. "
            "Remove any segments that are redundant, duplicate, or mistaken. "
            "For segments with duplicate or nearly identical text, keep only the last occurrence. "
            f"\n\nFormat instructions:\n{format_instructions}\n\n"
            f"Raw transcription:\n{raw_transcription}"
        )

        try:
            response = self.llm.predict(prompt)
            parsed_output = output_parser.parse(response)
            return parsed_output.get("filtered_transcription", raw_transcription)
        except Exception as e:
            print(f"Error in LLM processing: {e}")
            return raw_transcription