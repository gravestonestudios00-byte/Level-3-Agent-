# Changelog

## Filled Start #17
- Added runtime Scenario Executor (no-vision playtest):
  - Unity: unity_bridge/Runtime/Level3ScenarioExecutor.cs
  - Unity: unity_bridge/Runtime/MiniJson.cs (parse+serialize)
- Scenario Executor reads scenario_manifest.json and writes scenario_result.json with:
  - action results
  - check results
  - exception capture
- Updated InteractionSweeper to use shared MiniJson (removed embedded duplicate)
- Ensured BatchEntry.Smoke creates a ScenarioExecutor if missing
