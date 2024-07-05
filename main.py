"""
Generates a CloudFront signed URL.

Author: Nassredin Wesleti

The script retrieves the CloudFront key pair ID and private key from AWS Systems Manager (SSM) Parameter Store.
It then uses these to generate a signed URL for a given input URL, which expires after a specified number of seconds.

Returns:
    str: A signed URL that can be used to access the specified resource through CloudFront.
"""


from cloudfront_signed_url import generate_cloudfront_signed_url
url_to_sign = "https://your-cf-domain.com/path/to/file.txt"
expire_seconds = 3600  # 1 hour
url = generate_cloudfront_signed_url(url_to_sign, expire_seconds)
print(url)