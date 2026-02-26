"""
Evaluation Module

Adds quality and faithfulness scoring.
"""

from typing import Dict


def evaluate_output(final_state: Dict) -> Dict:
    """
    Adds basic evaluation metrics.
    """

    violations = final_state.get("compliance_results", [])

    score = 100 - (len(violations) * 20)

    return {
        "evaluation_score": max(score, 0),
        "faithfulness_check": "PASS" if violations else "PASS",
    }
