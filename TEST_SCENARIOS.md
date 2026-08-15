# Test Scenarios — Flask Voting Application

## How to Run the Project

### 1. Install dependencies
```powershell
pip install -r requirements.txt
```

### 2. Start the app
```powershell
python app.py
```

App will be available at: `http://127.0.0.1:5000`

### 3. Run all automated tests
```powershell
pytest test_app.py -v
```

---

## Test Scenarios

### TC-01: Home Page
| Field | Detail |
|---|---|
| Endpoint | `GET /` |
| Input | None |
| Expected Status | 200 |
| Expected Response | `Welcome to the App` |
| Test in browser | `http://127.0.0.1:5000/` |

---

### TC-02: Health Check
| Field | Detail |
|---|---|
| Endpoint | `GET /health` |
| Input | None |
| Expected Status | 200 |
| Expected Response | `App is running` |
| Test in browser | `http://127.0.0.1:5000/health` |

---

### TC-03: Vote for a New Candidate
| Field | Detail |
|---|---|
| Endpoint | `GET /vote/<name>` |
| Input | `/vote/alice` |
| Expected Status | 200 |
| Expected Response | `{"candidate": "alice", "message": "Vote recorded for alice", "votes": 1}` |
| Behaviour | New candidate starts at vote count 1 |

---

### TC-04: Vote for the Same Candidate Again
| Field | Detail |
|---|---|
| Endpoint | `GET /vote/<name>` |
| Input | `/vote/alice` (called twice) |
| Expected Status | 200 |
| Expected Response | `{"votes": 2, ...}` on second call |
| Behaviour | Vote count increments by 1 each time |

---

### TC-05: Vote Name is Case-Insensitive
| Field | Detail |
|---|---|
| Endpoint | `GET /vote/<name>` |
| Input | `/vote/Alice` |
| Expected Status | 200 |
| Expected Response | `{"candidate": "alice", ...}` |
| Behaviour | Name is lowercased before storing |

---

### TC-06: Multiple Candidates Are Independent
| Field | Detail |
|---|---|
| Endpoint | `GET /vote/<name>` |
| Input | `/vote/alice` then `/vote/bob` |
| Expected | alice=1, bob=1 |
| Behaviour | Each candidate has its own counter |

---

### TC-07: Results When No Votes Cast
| Field | Detail |
|---|---|
| Endpoint | `GET /results` |
| Input | None (no votes placed) |
| Expected Status | 200 |
| Expected Response | `{}` |
| Behaviour | Empty JSON when no candidates have voted |

---

### TC-08: Results Show All Candidates and Counts
| Field | Detail |
|---|---|
| Endpoint | `GET /results` |
| Input | Vote alice twice, vote bob once, then call `/results` |
| Expected Response | `{"alice": 2, "bob": 1}` |
| Behaviour | Returns accurate count for every candidate |

---

### TC-09: Results Returns JSON Content Type
| Field | Detail |
|---|---|
| Endpoint | `GET /results` |
| Expected Header | `Content-Type: application/json` |
| Behaviour | Response must be valid JSON, not plain text |

---

### TC-10: Reset Clears All Votes (GET)
| Field | Detail |
|---|---|
| Endpoint | `GET /reset` |
| Input | Vote first, then call reset |
| Expected Status | 200 |
| Expected Response | `{"message": "All votes reset successfully"}` |
| Verify | Call `/results` after reset — should return `{}` |

---

### TC-11: Reset via POST Method
| Field | Detail |
|---|---|
| Endpoint | `POST /reset` |
| Expected Status | 200 |
| Expected Response | `{"message": "All votes reset successfully"}` |
| Behaviour | Works with both GET and POST |

---

### TC-12: Vote After Reset Starts Fresh
| Field | Detail |
|---|---|
| Endpoint | `GET /vote/<name>` after `GET /reset` |
| Input | Vote alice, reset, vote alice again |
| Expected | `{"votes": 1, ...}` on the post-reset vote |
| Behaviour | Reset wipes all memory; counts restart from 1 |

---

## Manual Browser Test Sequence

Run these URLs in order in your browser after starting the app:

```
1. http://127.0.0.1:5000/
2. http://127.0.0.1:5000/health
3. http://127.0.0.1:5000/vote/alice
4. http://127.0.0.1:5000/vote/alice
5. http://127.0.0.1:5000/vote/bob
6. http://127.0.0.1:5000/results        ← should show {"alice": 2, "bob": 1}
7. http://127.0.0.1:5000/reset
8. http://127.0.0.1:5000/results        ← should show {}
```

---

## Automated Test Summary

| Test ID | Test Name | Covers |
|---|---|---|
| 1 | `test_home_status_code` | TC-01 |
| 2 | `test_home_response_text` | TC-01 |
| 3 | `test_health_status_code` | TC-02 |
| 4 | `test_health_response_text` | TC-02 |
| 5 | `test_vote_new_candidate_returns_200` | TC-03 |
| 6 | `test_vote_new_candidate_count_starts_at_1` | TC-03 |
| 7 | `test_vote_same_candidate_increments_count` | TC-04 |
| 8 | `test_vote_response_contains_candidate_name` | TC-03 |
| 9 | `test_vote_response_contains_message` | TC-03 |
| 10 | `test_vote_name_is_lowercased` | TC-05 |
| 11 | `test_vote_multiple_candidates_are_independent` | TC-06 |
| 12 | `test_results_empty_when_no_votes` | TC-07 |
| 13 | `test_results_shows_all_candidates` | TC-08 |
| 14 | `test_results_shows_correct_counts` | TC-08 |
| 15 | `test_results_returns_json_content_type` | TC-09 |
| 16 | `test_reset_via_get_returns_200` | TC-10 |
| 17 | `test_reset_via_post_returns_200` | TC-11 |
| 18 | `test_reset_clears_all_votes` | TC-10 |
| 19 | `test_reset_response_message` | TC-10 |
| 20 | `test_reset_then_vote_starts_fresh` | TC-12 |
