docker run --rm -v "%CD%/../:/local" openapitools/openapi-generator-cli:v5.3.0 generate ^
    -i /local/openapi/openapi.yaml ^
    -g python-flask ^
    -c /local/openapi/config-python-flask.json ^
    -o /local/server

docker run --rm -v "%CD%/../:/local" openapitools/openapi-generator-cli:v5.3.0 generate ^
    -i /local/openapi/openapi.yaml ^
    -g typescript-fetch ^
    -o /local/client/src/api/