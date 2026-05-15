from langchain_core.messages import HumanMessage, AIMessage, SystemMessage,BaseMessage
from chat_service import ask_ai_stream


def main():
    chat_history : list[BaseMessage] = [ #base包括这三种
    SystemMessage(content="你是一个耐心、清晰的中文 AI 助手。")
]

    print("连续对话已启动，输入 exit 退出。")

    while True:
        question = input("\n你：").strip()

        if question.lower() in ["exit", "quit", "q"]:
            print("对话结束。")
            break

        # 把用户本轮问题加入历史
        chat_history.append(HumanMessage(content=question))

        print("\nAI 正在思考中...\n")

        # 把完整历史发给模型
        answer, usage = ask_ai_stream(chat_history)

        # 把 AI 本轮回答也加入历史
        chat_history.append(AIMessage(content=answer))

        print("\n")

        if usage:
            print("Token 统计：")
            print("输入 tokens:", usage.get("input_tokens"))
            print("输出 tokens:", usage.get("output_tokens"))
            print("总 tokens:", usage.get("total_tokens"))


if __name__ == "__main__":
    main()