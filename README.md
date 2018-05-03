# average-on-demand-instance-usage

Just a quick way to find the average on-demand instance usage for a particular account over the course of the past year without having to mess around with CloudHealth's filters. Enter your api-key and the AWS account number of the account you're interested in to get a simple breakdown of each instance type.

## Usage
```
instance_usage.sh [api-key] [account-number]
```
## Example output
```
INSTANCE TYPE	AVERAGE USAGE
=============================
c3.large	0.021
c4.large	25.332
c4.xlarge	5.827
m3.xlarge	0.596
m4.2xlarge	1.431
m4.4xlarge	1.612
r3.large	6.661
t2.large	4.999
t2.medium	3.351
t2.xlarge	0.834
```
