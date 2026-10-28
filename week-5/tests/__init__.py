
"""Exercise 11: organize checks that prove your implementation works.

Purpose
-------
This initializer marks tests as a package; it is not itself a test suite. There
are intentionally no finished tests here. Add test modules beside this file as
you complete each feature, rather than waiting until the entire app is built.

Suggested checks to write
-------------------------
1. test_models.py: reject blank requests, invalid actions, missing tool fields,
   and extra arguments; verify state/response lists are not shared.
2. test_tools.py: known and unknown account ids, no-match search, invalid dispatch,
   an awaited async handler, and normalized error results.
3. test_approval.py: sensitive tools require approval; denied approval leaves a
   spy handler's call count at zero. Also cover approval_required decisions.
4. test_agent.py: substitute a sequence of decisions (tool, then final), check
   observations are passed forward and all exits retain the steps. A never-ending
   fake decision source must stop at the configured attempt budget, even on errors.
5. test_api.py: after wiring routes, check /health, valid /api/agent JSON, invalid
   input, and generic server errors that do not leak exception details.

How to keep checks local
-----------------------
Use standard-library unittest (including IsolatedAsyncioTestCase for async code)
and unittest.mock to start without another test dependency. Use an async fake or
AsyncMock for awaited functions. Replace dependencies where the module under
test looks them up, not only where the original function was defined.

Supply explicit test settings and fake provider responses. No test should need
a real API key, send an actual message, or make a paid model call. If you choose
FastAPI's TestClient for HTTP checks, add its required httpx dependency first.
Run checks from week-5 so app resolves to this week's package (see README.md).
"""
