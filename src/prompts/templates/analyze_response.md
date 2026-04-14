Analyze the following information to determine whether the `Worker Response` contains useful information.

# Worker Response
{{ pending_response }}

# Analysis Focus:
1. **RETRY:** Set status to 'RETRY' **ONLY IF** ANY of the following conditions are met:
   - The `Worker Response` contains an explicit "not found" outcome (e.g., **"cannot be completed"** or an unambiguous equivalent such as "No results found", "Unable to find", "Couldn't find", "information not found", "insufficient information", etc.); **OR**
   - The `Worker Response` explicitly states that **a tool error/failure prevented completing the task** and therefore they **could not proceed / could not complete / could not obtain the required info / could not finish the requested work**; **OR**
   - The `Worker Response` does **NOT** contain a "Final Conclusion" or similar conclusive statement (e.g., "In conclusion", "To summarize", "Final answer", "Summary", etc.), indicating the task is incomplete.
2. **FINISH:** Otherwise, set status to 'FINISH' **as long as** the `Worker Response` contains **a conclusive statement that indicate a completed task**.

# Key Disambiguation Rule
A "Final Conclusion" is NOT sufficient for FINISH. You MUST check:
→ Does the conclusion indicate SUCCESS (task completed)?
→ OR FAILURE (task cannot be completed)?

- If FAILURE → RETRY  
- If SUCCESS → FINISH  

# Output Format

Output the result in the following JSON format:
```json
{
    "status": "FINISH" or "RETRY",
    "reason": "A short explanation of your decision."
}
```