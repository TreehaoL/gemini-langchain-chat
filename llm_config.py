from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 读取 .env 文件中的 API Key
load_dotenv()

# 创建 Gemini 模型对象
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)