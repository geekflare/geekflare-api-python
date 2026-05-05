# geekflare_api.ApiToolApi

All URIs are relative to *https://api.geekflare.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broken_link**](ApiToolApi.md#broken_link) | **POST** /brokenlink | Check if a webpage contains broken links
[**dns_record**](ApiToolApi.md#dns_record) | **POST** /dnsrecord | Retrieve DNS records for a given domain
[**dns_sec**](ApiToolApi.md#dns_sec) | **POST** /dnssec | Check if DNSSEC is enabled for a domain
[**lighthouse**](ApiToolApi.md#lighthouse) | **POST** /lighthouse | Run Lighthouse audit on a website
[**load_time**](ApiToolApi.md#load_time) | **POST** /loadtime | Measure the page load time for a given URL
[**meta_scrape**](ApiToolApi.md#meta_scrape) | **POST** /metascraping | Scrape a webpage meta with custom options
[**mixed_content**](ApiToolApi.md#mixed_content) | **POST** /mixedcontent | Check for mixed content on a site
[**mtr**](ApiToolApi.md#mtr) | **POST** /mtr | Perform MTR (My Traceroute) network diagnostic test
[**open_ports**](ApiToolApi.md#open_ports) | **POST** /openport | Scan a website for open ports
[**ping**](ApiToolApi.md#ping) | **POST** /ping | Perform ICMP Ping test on a given URL or IP
[**redirect_check**](ApiToolApi.md#redirect_check) | **POST** /redirectcheck | Check the redirection chain of a given URL
[**screenshot**](ApiToolApi.md#screenshot) | **POST** /screenshot | Capture a full-page screenshot of a website
[**search**](ApiToolApi.md#search) | **POST** /search | Search API for AI Agents &amp; LLMs
[**site_status**](ApiToolApi.md#site_status) | **POST** /up | Check if a site is up or down
[**tls_scan**](ApiToolApi.md#tls_scan) | **POST** /tlsscan | Perform TLS scan for a given domain
[**url2_pdf**](ApiToolApi.md#url2_pdf) | **POST** /url2pdf | Capture a full-page Url2Pdf of a website
[**web_scrape**](ApiToolApi.md#web_scrape) | **POST** /webscraping | Scrape a webpage with custom options


# **broken_link**
> BrokenLinkResponseDto broken_link(broken_link_dto)

Check if a webpage contains broken links

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.broken_link_dto import BrokenLinkDto
from geekflare_api.models.broken_link_response_dto import BrokenLinkResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    broken_link_dto = geekflare_api.BrokenLinkDto() # BrokenLinkDto | 

    try:
        # Check if a webpage contains broken links
        api_response = api_instance.broken_link(broken_link_dto)
        print("The response of ApiToolApi->broken_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->broken_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broken_link_dto** | [**BrokenLinkDto**](BrokenLinkDto.md)|  | 

### Return type

[**BrokenLinkResponseDto**](BrokenLinkResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully checked for broken links |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_record**
> DnsRecordResponseDto dns_record(dns_record_dto)

Retrieve DNS records for a given domain

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.dns_record_dto import DnsRecordDto
from geekflare_api.models.dns_record_response_dto import DnsRecordResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    dns_record_dto = geekflare_api.DnsRecordDto() # DnsRecordDto | 

    try:
        # Retrieve DNS records for a given domain
        api_response = api_instance.dns_record(dns_record_dto)
        print("The response of ApiToolApi->dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_record_dto** | [**DnsRecordDto**](DnsRecordDto.md)|  | 

### Return type

[**DnsRecordResponseDto**](DnsRecordResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved DNS records |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_sec**
> DnsSecResponseDto dns_sec(dns_sec_dto)

Check if DNSSEC is enabled for a domain

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.dns_sec_dto import DnsSecDto
from geekflare_api.models.dns_sec_response_dto import DnsSecResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    dns_sec_dto = geekflare_api.DnsSecDto() # DnsSecDto | 

    try:
        # Check if DNSSEC is enabled for a domain
        api_response = api_instance.dns_sec(dns_sec_dto)
        print("The response of ApiToolApi->dns_sec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->dns_sec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_sec_dto** | [**DnsSecDto**](DnsSecDto.md)|  | 

### Return type

[**DnsSecResponseDto**](DnsSecResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DNSSEC test result retrieved successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lighthouse**
> LighthouseResponseDto lighthouse(lighthouse_dto)

Run Lighthouse audit on a website

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.lighthouse_dto import LighthouseDto
from geekflare_api.models.lighthouse_response_dto import LighthouseResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    lighthouse_dto = geekflare_api.LighthouseDto() # LighthouseDto | 

    try:
        # Run Lighthouse audit on a website
        api_response = api_instance.lighthouse(lighthouse_dto)
        print("The response of ApiToolApi->lighthouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->lighthouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lighthouse_dto** | [**LighthouseDto**](LighthouseDto.md)|  | 

### Return type

[**LighthouseResponseDto**](LighthouseResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully ran Lighthouse audit |  -  |
**400** | Bad request (e.g. invalid URL or parameters) |  -  |
**500** | Internal server error while running Lighthouse audit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_time**
> LoadTimeResponseDto load_time(load_time_dto)

Measure the page load time for a given URL

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.load_time_dto import LoadTimeDto
from geekflare_api.models.load_time_response_dto import LoadTimeResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    load_time_dto = geekflare_api.LoadTimeDto() # LoadTimeDto | 

    try:
        # Measure the page load time for a given URL
        api_response = api_instance.load_time(load_time_dto)
        print("The response of ApiToolApi->load_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->load_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_time_dto** | [**LoadTimeDto**](LoadTimeDto.md)|  | 

### Return type

[**LoadTimeResponseDto**](LoadTimeResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load time retrieved successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_scrape**
> MetaScrapeResponseDto meta_scrape(meta_scrape_dto)

Scrape a webpage meta with custom options

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.meta_scrape_dto import MetaScrapeDto
from geekflare_api.models.meta_scrape_response_dto import MetaScrapeResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    meta_scrape_dto = geekflare_api.MetaScrapeDto() # MetaScrapeDto | 

    try:
        # Scrape a webpage meta with custom options
        api_response = api_instance.meta_scrape(meta_scrape_dto)
        print("The response of ApiToolApi->meta_scrape:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->meta_scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_scrape_dto** | [**MetaScrapeDto**](MetaScrapeDto.md)|  | 

### Return type

[**MetaScrapeResponseDto**](MetaScrapeResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully scraped webpage meta |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mixed_content**
> MixedContentResponseDto mixed_content(mixed_content_dto)

Check for mixed content on a site

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.mixed_content_dto import MixedContentDto
from geekflare_api.models.mixed_content_response_dto import MixedContentResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    mixed_content_dto = geekflare_api.MixedContentDto() # MixedContentDto | 

    try:
        # Check for mixed content on a site
        api_response = api_instance.mixed_content(mixed_content_dto)
        print("The response of ApiToolApi->mixed_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->mixed_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mixed_content_dto** | [**MixedContentDto**](MixedContentDto.md)|  | 

### Return type

[**MixedContentResponseDto**](MixedContentResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site status retrieved successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mtr**
> MtrResponseDto mtr(mtr_dto)

Perform MTR (My Traceroute) network diagnostic test

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.mtr_dto import MtrDto
from geekflare_api.models.mtr_response_dto import MtrResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    mtr_dto = geekflare_api.MtrDto() # MtrDto | 

    try:
        # Perform MTR (My Traceroute) network diagnostic test
        api_response = api_instance.mtr(mtr_dto)
        print("The response of ApiToolApi->mtr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->mtr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mtr_dto** | [**MtrDto**](MtrDto.md)|  | 

### Return type

[**MtrResponseDto**](MtrResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MTR test completed successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_ports**
> OpenPortResponseDto open_ports(open_port_dto)

Scan a website for open ports

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.open_port_dto import OpenPortDto
from geekflare_api.models.open_port_response_dto import OpenPortResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    open_port_dto = geekflare_api.OpenPortDto() # OpenPortDto | 

    try:
        # Scan a website for open ports
        api_response = api_instance.open_ports(open_port_dto)
        print("The response of ApiToolApi->open_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->open_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_port_dto** | [**OpenPortDto**](OpenPortDto.md)|  | 

### Return type

[**OpenPortResponseDto**](OpenPortResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Open ports retrieved successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> PingResponseDto ping(ping_dto)

Perform ICMP Ping test on a given URL or IP

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.ping_dto import PingDto
from geekflare_api.models.ping_response_dto import PingResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    ping_dto = geekflare_api.PingDto() # PingDto | 

    try:
        # Perform ICMP Ping test on a given URL or IP
        api_response = api_instance.ping(ping_dto)
        print("The response of ApiToolApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_dto** | [**PingDto**](PingDto.md)|  | 

### Return type

[**PingResponseDto**](PingResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping test completed successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_check**
> RedirectCheckResponseDto redirect_check(redirect_check_dto)

Check the redirection chain of a given URL

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.redirect_check_dto import RedirectCheckDto
from geekflare_api.models.redirect_check_response_dto import RedirectCheckResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    redirect_check_dto = geekflare_api.RedirectCheckDto() # RedirectCheckDto | 

    try:
        # Check the redirection chain of a given URL
        api_response = api_instance.redirect_check(redirect_check_dto)
        print("The response of ApiToolApi->redirect_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->redirect_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_check_dto** | [**RedirectCheckDto**](RedirectCheckDto.md)|  | 

### Return type

[**RedirectCheckResponseDto**](RedirectCheckResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved redirect chain |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screenshot**
> ScreenshotResponseDto screenshot(screenshot_dto)

Capture a full-page screenshot of a website

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.screenshot_dto import ScreenshotDto
from geekflare_api.models.screenshot_response_dto import ScreenshotResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    screenshot_dto = geekflare_api.ScreenshotDto() # ScreenshotDto | 

    try:
        # Capture a full-page screenshot of a website
        api_response = api_instance.screenshot(screenshot_dto)
        print("The response of ApiToolApi->screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->screenshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenshot_dto** | [**ScreenshotDto**](ScreenshotDto.md)|  | 

### Return type

[**ScreenshotResponseDto**](ScreenshotResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully captured screenshot |  -  |
**400** | Bad request (e.g. invalid URL or parameters) |  -  |
**500** | Internal server error while capturing screenshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> Search200Response search(search_request_dto)

Search API for AI Agents & LLMs

Search the web for AI, remove noise like ads and unnecessary HTML, and return clean data in JSON, Markdown, or HTML formats, with support for image search and news.

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.search200_response import Search200Response
from geekflare_api.models.search_request_dto import SearchRequestDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    search_request_dto = geekflare_api.SearchRequestDto() # SearchRequestDto | 

    try:
        # Search API for AI Agents & LLMs
        api_response = api_instance.search(search_request_dto)
        print("The response of ApiToolApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**Search200Response**](Search200Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results (format depends on request) |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_status**
> SiteStatusResponseDto site_status(site_status_dto)

Check if a site is up or down

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.site_status_dto import SiteStatusDto
from geekflare_api.models.site_status_response_dto import SiteStatusResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    site_status_dto = geekflare_api.SiteStatusDto() # SiteStatusDto | 

    try:
        # Check if a site is up or down
        api_response = api_instance.site_status(site_status_dto)
        print("The response of ApiToolApi->site_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->site_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_status_dto** | [**SiteStatusDto**](SiteStatusDto.md)|  | 

### Return type

[**SiteStatusResponseDto**](SiteStatusResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site status retrieved successfully |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tls_scan**
> TlsScanResponseDto tls_scan(tls_scan_dto)

Perform TLS scan for a given domain

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.tls_scan_dto import TlsScanDto
from geekflare_api.models.tls_scan_response_dto import TlsScanResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    tls_scan_dto = geekflare_api.TlsScanDto() # TlsScanDto | 

    try:
        # Perform TLS scan for a given domain
        api_response = api_instance.tls_scan(tls_scan_dto)
        print("The response of ApiToolApi->tls_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->tls_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_scan_dto** | [**TlsScanDto**](TlsScanDto.md)|  | 

### Return type

[**TlsScanResponseDto**](TlsScanResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved TLS scan information |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url2_pdf**
> Url2PdfResponseDto url2_pdf(url2_pdf_dto)

Capture a full-page Url2Pdf of a website

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.url2_pdf_dto import Url2PdfDto
from geekflare_api.models.url2_pdf_response_dto import Url2PdfResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    url2_pdf_dto = geekflare_api.Url2PdfDto() # Url2PdfDto | 

    try:
        # Capture a full-page Url2Pdf of a website
        api_response = api_instance.url2_pdf(url2_pdf_dto)
        print("The response of ApiToolApi->url2_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->url2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url2_pdf_dto** | [**Url2PdfDto**](Url2PdfDto.md)|  | 

### Return type

[**Url2PdfResponseDto**](Url2PdfResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully captured Url2Pdf |  -  |
**400** | Bad request (e.g. invalid URL or parameters) |  -  |
**500** | Internal server error while capturing Url2Pdf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_scrape**
> WebScrapeResponseDto web_scrape(web_scrape_dto)

Scrape a webpage with custom options

### Example

* Api Key Authentication (x-api-key):

```python
import geekflare_api
from geekflare_api.models.web_scrape_dto import WebScrapeDto
from geekflare_api.models.web_scrape_response_dto import WebScrapeResponseDto
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    web_scrape_dto = geekflare_api.WebScrapeDto() # WebScrapeDto | 

    try:
        # Scrape a webpage with custom options
        api_response = api_instance.web_scrape(web_scrape_dto)
        print("The response of ApiToolApi->web_scrape:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiToolApi->web_scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_scrape_dto** | [**WebScrapeDto**](WebScrapeDto.md)|  | 

### Return type

[**WebScrapeResponseDto**](WebScrapeResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully scraped webpage |  -  |
**400** | Bad request (invalid parameters) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

