# CloudFront Signed URL generator in Python

## Usage
```python
from cloudfront_signed_url import generate_cloudfront_signed_url

generate_cloudfront_signed_url("https://your-cf-domain.com/path/to/file.txt", 3600)
```
## Prerequisites

* Configured CloudFront Distribution
* An Origin access identity and a CloudFront key
* Origin and Behavior configured to Restrict Viewer Access

Reference: http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html

## Parameters
- Make sure you have a CloudFront key pair and key group created and associated with distribution behavior, [details here](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs))
- Replace newlines with `\\n` in private key and save the result to an SSM Parameter Store paramater named `CF_SIGNED_URL_PRIVATE_KEY`
- Save key ID (key pair ID) to a parameter named `CF_SIGNED_URL_KEY_ID`

## Notes
- Unlike S3 pre-signed URLs, you can use a link generated once multiple times, as long as it is still valid (TTL).
- You can modify `make_policy` to make other policies (not per-url, but broader clauses), or even signed cookies (Policy, Signature, Key-Pair-Id are generated in the same way for cookies too).

## Dependencies
- cryptography
- boto3 (only for SSM)