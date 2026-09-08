import geekflare_api
from geekflare_api.api.api_tool_api import ApiToolApi
from geekflare_api.models import PingDto
import json

configuration = geekflare_api.Configuration(host="https://api.geekflare.com")
configuration.api_key["x-api-key"] = "your-api-key-here"

with geekflare_api.ApiClient(configuration) as client:
    api = ApiToolApi(client)
    response = api.ping_without_preload_content(ping_dto=PingDto(url="https://google.com"))
    print(json.loads(response.data))
