#!/bin/bash

if [ "${TRAVIS_BRANCH}" == "master" ] ; then
    echo "On \`master' branch - triggering rebuild of docs."
    curl -s -X POST \
         -H "Content-Type: application/json" \
         -H "Accept: application/json" \
         -H "Travis-API-Version: 3" \
         -H "Authorization: token ${TRAVIS_TOKEN}" \
         -d '{"request":{"branch":"master"},"message":"Triggered build via client-examples."}' \
         'https://api.travis-ci.org/repo/BI-Beacon%2Fdocs/requests'
else
    echo "Not on \`master' branch - not triggering rebuild of docs."
fi
