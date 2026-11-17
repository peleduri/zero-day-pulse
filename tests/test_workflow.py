import re
import unittest
from pathlib import Path

import yaml

WORKFLOW = Path(__file__).resolve().parent.parent / ".github" / "workflows" / "zero-day-pulse.yml"


def _steps(wf):
    for job in wf["jobs"].values():
        yield from job.get("steps", [])


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wf = yaml.safe_load(WORKFLOW.read_text())
        cls.steps = {s.get("id") or s["name"]: s for s in _steps(cls.wf)}

    def test_concurrency_group(self):
        self.assertEqual(self.wf["concurrency"],
                         {"group": "zero-day-pulse", "cancel-in-progress": False})

    def test_every_action_pinned_to_sha(self):
        uses = [s["uses"] for s in _steps(self.wf) if "uses" in s]
        self.assertTrue(uses)
        for u in uses:
            self.assertRegex(u, r"^[\w.-]+/[\w./-]+@[0-9a-f]{40}$", u)

    def test_tracker_gated_on_step_outcomes(self):
        tracker = self.steps["Update tracking issue"]
        cond = tracker["if"]
        self.assertNotIn("always()", cond)
        self.assertIn("steps.pulse.outcome == 'success'", cond)
        self.assertIn("steps.commit.outcome == 'success'", cond)
        self.assertEqual(tracker["env"]["RUN_ID"], "${{ github.run_id }}")
        script = tracker["with"]["script"]
        self.assertIn("process.env.RUN_ID", script)
        self.assertNotIn("${{", script)  # nothing interpolated into JS source
        self.assertIn("issues.update", script)
        self.assertIn("🚨 Zero Day Pulse — Active Vulnerability Tracker", script)

    def test_commit_stages_state_and_changes(self):
        run = self.steps["commit"]["run"]
        add = next(l for l in run.splitlines() if l.strip().startswith("git add"))
        self.assertIn("state/", add.split())
        self.assertIn("reports/changes.json", add.split())

    def test_state_not_gitignored(self):
        ignore = (WORKFLOW.parent.parent.parent / ".gitignore").read_text().splitlines()
        rules = [l.strip() for l in ignore if l.strip() and not l.startswith("#")]
        self.assertFalse(any(re.match(r"^/?state/?$", r) or r in ("state/last_run.json", "reports/changes.json")
                             for r in rules))


if __name__ == "__main__":
    unittest.main()
