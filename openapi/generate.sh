docker run --rm -v "${PWD}/../:/local" openapitools/openapi-generator-cli:v5.3.0 generate \
    -i /local/openapi/openapi.yaml \
    -g python-flask \
    -o /local/server

docker run --rm -v "${PWD}/../:/local" openapitools/openapi-generator-cli:v5.3.0 generate \
    -i /local/openapi/openapi.yaml \
    -g typescript-fetch \
    -o /local/client/src/api/