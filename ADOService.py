import os
import requests
from azure.identity import AzureCliCredential

# Set your Azure DevOps details
ADO_ORG = "https://jalajchadha.visualstudio.com/"  # Replace with your org URL
ADO_PROJECT = "AIWorkshop"  # Replace with your project name
ADO_REPO = "AIWorkshop"  # Replace with your repo name
FILE_PATH = "/src/CMakeLists.txt"  # Replace with the file path in the repo
BRANCH = "master"  # Replace with the branch name

# Authenticate using AzureCLICredential
credential = AzureCliCredential()
access_token = os.environ.get("ADO_ACCESS_TOKEN", "")

# Headers for authentication
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

def get_file_content(ado_org, ado_project, ado_repo, file_path, branch, access_token):
    """
    Fetch file content from Azure DevOps repository.
    
    Args:
        ado_org (str): Azure DevOps organization URL
        ado_project (str): Project name
        ado_repo (str): Repository name
        file_path (str): Path to the file in the repository
        branch (str): Branch name
        access_token (str): Authentication token
        
    Returns:
        str: Content of the file if successful
        
    Raises:
        Exception: If the file cannot be fetched
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Construct URL to fetch file contents
    file_url = f"{ado_org}/{ado_project}/_apis/git/repositories/{ado_repo}/items?path={file_path}&versionType=branch&version={branch}&includeContent=True&api-version=7.1-preview.1"

    # Send GET request
    response = requests.get(file_url, headers=headers)

    if response.status_code == 200:
        file_content = response.text
        print(file_content)
        return response.text
    else:
        raise Exception(f"Failed to fetch file: {response.status_code}, {response.text}")

# Call the function to get file content
try:
    file_content = get_file_content(ADO_ORG, ADO_PROJECT, ADO_REPO, FILE_PATH, BRANCH, access_token)
    print(f"Contents of {FILE_PATH}:\n")
    print(file_content)
except Exception as e:
    print(e)
