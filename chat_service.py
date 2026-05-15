from google.genai.errors import ServerError
from llm_config import llm


def ask_ai(question):
    """
    调用 Gemini 模型回答用户问题

    :param question: 用户输入的问题
    :return: 模型回答内容和 token 使用情况
    """
    try:
        response = llm.invoke(question)

        answer = response.content
        usage = response.usage_metadata

        return answer, usage

    except ServerError as e:
        return f"Gemini 服务器当前繁忙，请稍后再试。\n错误信息：{e}", None

    except Exception as e:
        return f"程序发生未知错误：{e}", None

def ask_ai_stream(messages):#question 改成messages一组消息
    """
    流式调用：模型边生成，控制台边输出
    """
    full_answer = ""
    usage = None

    try:
        for chunk in llm.stream(messages):
            if chunk.content:
                print(chunk.content, end="", flush=True)
                full_answer += chunk.content

            # 有些模型会在流式输出的 chunk 中附带 token 信息
            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                usage = chunk.usage_metadata

        return full_answer, usage

    except ServerError as e:
        error_msg = f"Gemini 服务器当前繁忙，请稍后再试。\n错误信息：{e}"
        print(error_msg)
        return error_msg, None

    except Exception as e:
        error_msg = f"程序发生未知错误：{e}"
        print(error_msg)
        return error_msg, None