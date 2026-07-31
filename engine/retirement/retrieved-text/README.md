# Retrieved primary text

Each file here is the text a fetch tool **extracted** from an official source
during a parameter-layer session — not the raw source document. That distinction
is the whole point of `provenance.hash_scope`:

- `hash_scope: "tool_extracted_text"` — `source_hash` is the sha256 of the
  corresponding file in this directory. It detects drift in what we recorded,
  and lets a reviewer recompute the hash. It does **not** detect drift in the
  publisher's document, because the extraction discarded markup, ordering, and
  surrounding context.
- `hash_scope: "raw_source"` — `source_hash` is the sha256 of the source bytes
  as published. This is the real drift detector, and every record in this
  directory is queued for upgrade to it.

Recompute and compare against `parameters.json`:

```bash
py -3.12 engine/retirement/paramlayer.py --verify-hashes
```

Each file's header records the URL and the retrieval timestamp. The body below
the `---` line is the hashed content: hashing covers the body only, so the
header can be corrected without invalidating the hash. Line endings are
normalised to LF before hashing, so a checkout on Windows and one on macOS agree.

A record points at the file carrying its **value** via
`provenance.hash_source_file`, and at any further file it **depends on** via
`provenance.supporting_evidence` — the ULT divisor records take their value from
the CFR extraction but their `valid_from` from the T.D. 9930 extraction, and both
are hashed. `--verify-hashes` also reports any file here that no record
references, so evidence cannot sit unverified.

Nothing in this directory is authority. It is evidence of what was read.
