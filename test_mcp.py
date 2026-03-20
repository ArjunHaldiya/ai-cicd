from mcp_server import review_code
from sampleCode import GOOD_CODE, BAD_CODE

print("Testing GOOD CODE:")
print(review_code(GOOD_CODE))

print("\nTesting BAD CODE:")
print(review_code(BAD_CODE))