import json
import sys

# Create a JSON string from the report passed in as a command line argument.
report = json.loads(sys.argv[1])
dimensions = report["dimensions"]

# Since we're only interested in the last full 12 month period, we remove the
# last month from the list because it's the current, partial month. We also
# remove the first item in the list because it's not a month value.
months = dimensions[0]["time"][1:][:-1]

# Removing the first item in the instance types list gives us the correct, full
# list of instance types.
instance_types = dimensions[1]["EC2-Instance-Types"][1:]

# Currently only interested in the total instance usage, i.e. the first entry.
# We can expand on this later to get the total usage of the last 3-month or
# 6-month period.
data = report["data"][0]

# Here, we're building the result string to be printed to the console.
result = []
for counter, instance in enumerate(instance_types):
    # We don't care about null values because that means that instance type
    # was never used.
    if not data[counter][0]:
        continue
    average = "{:0.3f}".format(data[counter][0] / 12)
    result.append(str.format("{0}\t{1}", instance['name'], average))

# Make it pretty.
result.sort()
result.insert(0, "INSTANCE TYPE\tAVERAGE USAGE\n" + '=' * 29)
for x in result:
    print(x)
