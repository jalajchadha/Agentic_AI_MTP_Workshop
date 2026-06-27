import os
import autogen
import datetime
from ADOService import get_file_content

ADO_ORG = "https://jalajchadha.visualstudio.com/"  # Replace with your org URL
ADO_PROJECT = "AIWorkshop"  # Replace with your project name
ADO_REPO = "AIWorkshop"  # Replace with your repo name
FILE_PATH = "/src/CMakeLists.txt"  # Replace with the file path in the repo
BRANCH = "master"  # Replace with the branch name

# Authenticate using AzureCLICredential
access_token = os.environ.get("ADO_ACCESS_TOKEN", "")


def get_current_time():
    """
    Get the current time and fetch a file from Azure DevOps.
    
    Returns:
        str: A message with the current time and file content status
    """
    
    try:
        # Call the get_file_content function from ADOService
        file_content = get_file_content(
            ado_org=ADO_ORG,
            ado_project=ADO_PROJECT,
            ado_repo=ADO_REPO,
            file_path=FILE_PATH,
            branch=BRANCH,
            access_token=access_token
        )
        return f"The current time is {current_time}. Successfully retrieved file content from Azure DevOps."
    except Exception as e:
        return f"The current time is {current_time}. Failed to get file content: {str(e)}"


class AgentWithFunctionCall:
    def __init__(self, llmConfig: list[dict[str, any]]):
        self.llmConfig = llmConfig

    def runUserGoal(self):
        assistant = autogen.AssistantAgent(
            name="TimeAgent",
            system_message="You are an assistant agent that helps users to find the current time.",
            llm_config={  # No "function_call" parameter
                "config_list": self.llmConfig,
            }
        )

        assistant.register_for_llm(name="find_time", description="get the current time.")(get_current_time)
        user = autogen.UserProxyAgent(
            name="User",
            human_input_mode="NEVER",  # Fully automated interaction
            code_execution_config={"use_docker": False},  # Disable Docker
        )
        user.register_for_execution(name="find_time")(get_current_time)
        response = user.initiate_chat(assistant, message="What time is it?", max_turns=2)
        return response

