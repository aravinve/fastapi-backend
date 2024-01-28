import json
import yaml

def yaml_to_json_from_file(yaml_content: bytes) -> bytes:
    try:
        yaml_data = yaml.safe_load(yaml_content)
        json_data = json.dumps(yaml_data, indent=2, ensure_ascii=False)
        print(f"Converted from YAML to JSON")
        return json_data
    except yaml.YAMLError as e:
        return {"error": f"Failed to parse YAML: {str(e)}"}
    
def json_to_yaml_from_file(json_content: bytes) -> bytes:
    try:
        json_data = json.loads(json_content)
        yaml_data = yaml.dump(json_data, default_flow_style=False, allow_unicode=True)
        print(f"Converted from JSON to YAML")
        return yaml_data
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse JSON: {str(e)}"}

def yaml_to_json(yaml_content: str) -> str:
    try:
        yaml_data = yaml.safe_load(yaml_content)
        json_data = json.dumps(yaml_data, indent=2, ensure_ascii=False)
        print(f"Converted from YAML to JSON")
        return json_data
    except yaml.YAMLError as e:
        return {"error": f"Failed to parse YAML: {str(e)}"}
    
def json_to_yaml(json_content: str) -> str:
    try:
        json_data = json.loads(json_content)
        yaml_data = yaml.dump(json_data, default_flow_style=False, allow_unicode=True)
        print(f"Converted from JSON to YAML")        
        return yaml_data
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse JSON: {str(e)}"}