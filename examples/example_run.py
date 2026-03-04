"""
Example run for the AI evaluation framework.
"""

def evaluate_response(prompt, response):
    score = {
        "clarity": 4,
        "correctness": 5,
        "completeness": 4
    }

    return score


if __name__ == "__main__":

    prompt = "Explain what artificial intelligence is."
    response = "Artificial intelligence is the field of creating machines that simulate human intelligence."

    result = evaluate_response(prompt, response)

    print("Evaluation result:")
    print(result)
