import json
from pathlib import Path
#AFTER cdk deploy --outputs-file outputs.json
# Take the api url and update the html file

def update_api_html(cdk_json: str, html_file: str):
    outputs_path = Path(cdk_json)
    html_path = Path(html_file)
    
        
    with outputs_path.open("r", encoding="utf-8") as f:
        outputs = json.load(f)
        
    url = outputs["BuildingExperienceStack"]["ApiGatewayUrl"]

    html = html_path.read_text(encoding="utf-8")
    placeholder = "https://YOUR_API_ID.execute-api.ap-southeast-2.amazonaws.com/prod/contact"

    if placeholder in html:
        html = html.replace(placeholder, url)
    else:
        raise ValueError("Temp URL String not found")
        #html = html.replace('data-api-url="https://YOUR_API_ID.execute-api.ap-southeast-2.amazonaws.com/prod/contact"', f'data-api-url="{url}"')

    html_path.write_text(html, encoding="utf-8")

    print(f"Updated API URL to: {url}")
    
    
if __name__ == '__main__':
    update_api_html('outputs.json', "../index.html")