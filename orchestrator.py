from concurrent.futures import ThreadPoolExecutor
import agents.security as security
import agents.performance as performance
import agents.style as style


def orchestrator(code: str) -> dict:

    with ThreadPoolExecutor() as executor:
        future_security = executor.submit(security.review, code)
        future_performance = executor.submit(performance.performance, code)
        future_style = executor.submit(style.style, code)

    security_result = future_security.result()
    performance_result = future_performance.result()
    style_result = future_style.result()


    if security_result["passed"] and performance_result["passed"] and style_result["passed"]:
        return {"status" : "Approved : DEPLOYED", "security" : security_result, "performance" : performance_result, "style" : style_result}
    else:
        return {"status" : "BLOCKED : NOT DEPLOYED", "security" : security_result, "performance" : performance_result, "style" : style_result}


