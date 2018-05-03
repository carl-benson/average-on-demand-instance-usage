#!/usr/bin/env fish

set api_key 'api_key='$argv[1]
set main_url 'https://chapi.cloudhealthtech.com/olap_reports/usage/instance'
set parameters 'interval=monthly' \
    'dimensions\[\]=time' \
    'dimensions\[\]=EC2-Instance-Types' \
    'measures\[\]=usage_quantity' \
    'filters\[\]=AWS-Account:select:'$argv[2] \
    'filters\[\]=time:select:-2,-3,-4,-5,-6,-7,-8,-9,-10,-11'
for x in $parameters:
  set params (string join "&" $parameters $api_key)
end
set url (string join "?" $main_url $params)
set data (curl -H 'Accept: application/json' $url)
python3 ./usage_calc.py $data
