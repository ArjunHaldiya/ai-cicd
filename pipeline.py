from orchestrator import orchestrator
from sampleCode import GOOD_CODE, BAD_CODE

result_good = orchestrator(GOOD_CODE)
print("GOOD RESULT : ", result_good)

result_bad = orchestrator(BAD_CODE)
print("BAD RESULT : ", result_bad)
