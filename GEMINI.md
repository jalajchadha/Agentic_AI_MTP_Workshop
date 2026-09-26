

<!-- scout-routing:begin -->
## Scout MCP routing

This repo is indexed by Scout MCP (semantic code search / investigate / call-graph /
impact analysis tools, exposed via the MCP gateway). Prefer Scout tools over native
search/read tools whenever they can answer the question - Scout is pre-indexed and
much cheaper token-wise than scanning files directly.

Swap native calls for Scout equivalents:
- `grep_search` / `find_by_name` -> `scout__keyword_search` / `scout__search` / `scout__regex_search`
- Understanding a subsystem / "how does X work" -> `scout__investigate` (+ `scout__investigate_expand`)
- Jump to a symbol's definition -> `scout__go_to_definition` / `scout__find_references`
- File structure without reading the whole file -> `scout__file_outline`
- "What breaks if I change this" -> `scout__impact` / `scout__call_graph` / `scout__changes_affected_tests`
- Dead code / coverage gaps -> `scout__dead_code` / `scout__coverage_gaps`

If tool names appear with a different MCP-server prefix (e.g. `docker-mcp__scout__...`),
use whichever variant is listed - it is the same Scout tool.

A `PreToolUse` hook in `.agents/hooks.json` will visibly ask for confirmation before
`grep_search`/`find_by_name` run, as a reminder to consider Scout first - it is not a
silent fallback. Proceed with native search when Scout genuinely cannot answer
(binary/generated/untracked files, etc).
<!-- scout-routing:end -->

