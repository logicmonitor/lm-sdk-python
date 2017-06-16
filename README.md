# lm-sdk-python

Getting Started
---------------

```python
import logicmonitor


def new_lm_client(id, key, company):
    # Configure API key authorization: LMv1
    logicmonitor.configuration.host = logicmonitor.configuration.host.replace(
        'localhost',
        company + '.logicmonitor.com'
    )
    logicmonitor.configuration.api_key['id'] = id
    logicmonitor.configuration.api_key['Authorization'] = key

    # create an instance of the API class
    return logicmonitor.DefaultApi(logicmonitor.ApiClient())


def main():
    client = new_lm_client('access_id', 'access_key', 'my_account')


if __name__ == '__main__':
    main()

```

### License
[![license](https://img.shields.io/github/license/logicmonitor/lm-sdk-go.svg?style=flat-square)](https://github.com/logicmonitor/lm-sdk-go/blob/master/LICENSE)
