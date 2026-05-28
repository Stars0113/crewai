import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

load_dotenv()

search_tool = SerperDevTool()

researcher = Agent(
    role="资深技术研究员",
    goal="使用搜索工具获取指定主题的最新信息，并整理成结构化报告",
    backstory=(
        "你是一名有10年经验的科技研究员，"
        "善于使用搜索工具获取第一手资料，"
        "并从中提炼关键洞察。"
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)

research_task = Task(
    description=(
        "请先用搜索工具搜索「AI Agent 框架 2026 最新进展 crewAI LangGraph」，"
        "基于搜索结果，撰写一份分析报告，必须包含以下三个部分：\n"
        "## 一、核心趋势（不少于3条，每条100字以上）\n"
        "## 二、主流框架对比（crewAI / AutoGen / LangGraph，列表对比）\n"
        "## 三、落地建议（2条，面向企业技术团队）\n"
        "总字数不少于 800 字。"
    ),
    expected_output="结构清晰的中文 Markdown 报告，包含标题、列表和有深度的分析。",
    agent=researcher,
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print("\n===== 最终报告 =====\n")
print(result.raw)
