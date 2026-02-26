"""
LangGraph workflow definition for the compliance engine.
"""

def build_graph():
    """
    Builds and returns the LangGraph workflow.
    """
    # Placeholder for future LangGraph state machine
    return None


from agents.compliance_auditor import ComplianceAuditor


def run_workflow(initial_inputs: dict):

    # Simulated transcript
    transcript = "This product offers a 100% guarantee."

    # Simulated policy list
    policies = [
        {"rule": "No absolute guarantees allowed."}
    ]

    auditor = ComplianceAuditor()

    audit_results = auditor.evaluate(transcript, policies)

    return {
        **initial_inputs,
        **audit_results,
        "final_report": "Compliance evaluation completed."
    }
