#!/usr/bin/env python3
"""Helper script to analyze if a task name is outcome-focused."""

import re
import sys


def is_outcome_focused(task_name: str) -> tuple[bool, str]:
    """
    Determine if a task name is outcome-focused.
    
    Returns: (is_outcome: bool, reason: str)
    """
    task_lower = task_name.lower().strip()
    
    # Already marked
    if task_name.startswith("⚠️ NOT OUTCOME:"):
        return True, "Already marked"
    
    # Red flags
    activity_verbs = ["meet", "review", "check", "follow up", "update", "discuss"]
    vague_terms = ["daily tasks", "weekly", "general", "housekeeping"]
    
    # Too short
    if len(task_lower) < 3:
        return False, "Too short/vague"
    
    # Question
    if task_name.endswith("?"):
        return False, "Question, not outcome"
    
    # Vague terms
    for term in vague_terms:
        if term in task_lower:
            return False, f"Vague term: {term}"
    
    # Activity verb without outcome
    words = task_lower.split()
    if words and words[0] in activity_verbs:
        if not any(char.isdigit() for char in task_name):
            return False, f"Activity verb: {words[0]}"
    
    # All caps
    if task_name.isupper() and len(words) <= 3:
        return False, "All caps category"
    
    # Single word
    if len(words) <= 1:
        return False, "Single word/abbreviation"
    
    # Measurable (has numbers or specific deliverables)
    if any(char.isdigit() for char in task_name):
        return True, "Has measurable component"
    
    # Deliverable keywords
    deliverable_words = ["complete", "deliver", "launch", "secure", "achieve", 
                         "finalize", "submit", "approve", "sign"]
    if any(word in task_lower for word in deliverable_words):
        return True, "Has deliverable keyword"
    
    # Default
    return False, "No clear outcome"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        is_outcome, reason = is_outcome_focused(task)
        print(f"{'✅ OUTCOME' if is_outcome else '❌ NOT OUTCOME'}: {reason}")
        sys.exit(0 if is_outcome else 1)
