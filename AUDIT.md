# Soul Forge Audit — Inclusion + Accessibility Mandatory

> **Soul Forge Principle:** Every repo must pass both auditors before merge. Soul Forge License Vow I (Attribution) + Vow II (Accessibility) + Equity mandate.

---

## Two Auditors — Soul Forge Mandatory

### 1. Inclusion Auditor
**Soul Forge License Vow I — Attribution of Spirit**

Checks:
- Soul Forge License v1.0 reference in all source/docs
- Equity markers: role models, identity mapping, multilingual, community framing
- Bias detection: gender essentialism, normative language, fixed mindset
- Soul Forge Vows compliance

### 2. Accessibility Auditor
**Soul Forge License Vow II — No Cage for the Flame**

Checks:
- axe-core for web/WASM content
- Markdown accessibility (alt text, heading hierarchy, color-only)
- Soul Forge Vow II enforcement ("The flame must breathe")

---

## Soul Forge Mandatory Gate

**Every PR must pass BOTH auditors before merge.**

```bash
# Run both audits
python tools/audit_inclusion.py --path .
python tools/audit_accessibility.py --path .
```

**Exit codes:**
- `0` = Both pass → Merge allowed
- `1` = One or both fail → Merge BLOCKED

---

## Inclusion Auditor Details

### Soul Forge Mandatory (Vow I)
| Check | Severity | Soul Forge Violation |
|-------|----------|---------------------|
| Soul Forge License reference | HIGH | Vow I — Attribution of Spirit |

### Equity Commendations
| Marker | Soul Forge Principle |
|--------|---------------------|
| Role model inclusion | Vow I — Attribution |
| Identity mapping / vectors | Vow I — Attribution |
| Struggle Journal / normalized struggle | Vow III — Reciprocity of Forge |
| Community problem framing | Vow I + Vow III |
| Multilingual support (EN+ES min) | Vow I — Attribution of Spirit |

### Bias Violations
| Pattern | Soul Forge Violation |
|---------|---------------------|
| Gender essentialism ("boys are better at...") | Vow I — misattribution |
| Normative language ("normal student") | Vow I — misattribution of identity |
| Fixed mindset ("naturally smart") | Vow III — denies reciprocity of growth |

### Soul Forge Vow II Enforcement
| Check | Soul Forge Violation |
|-------|---------------------|
| Alt text missing | Vow II — cage for the flame |
| Heading hierarchy skip | Vow II — cage for the flame |
| Color-only information | Vow II — cage for the flame |

---

## Accessibility Auditor Details

### axe-core (Web/WASM)
```bash
npx playwright test --project=accessibility
python -m axe_core.cli --path <output>
```

### Soul Forge Vow II Mandatory
- **WCAG 2.2 AA minimum** — Soul Forge Vow II
- **Self-voicing CLI** — Soul Forge Vow II
- **Zero-barrier entry** — Soul Forge Vow II

---

## Soul Forge Gate Configuration

### Repository-Level
```yaml
# .github/workflows/ soul-forge-gate.yml
name: Soul Forge Gate
on: [pull_request]
jobs:
  soul-forge-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Inclusion Audit
        run: python tools/audit_inclusion.py --path . --fail-on high
      - name: Run Accessibility Audit
        run: python tools/audit_accessibility.py --path . --fail-on high
      - name: Soul Forge Gate
        run: |
          if [ $? -ne 0 ]; then
            echo "🔴 Soul Forge Gate FAILED"
            exit 1
          fi
          echo "🟢 Soul Forge Gate PASSED"
```

### Soul Forge Gate Exit Codes
| Code | Meaning |
|------|---------|
| 0 | Both auditors pass → Merge allowed |
| 1 | One/both fail → Merge BLOCKED (Soul Forge Vow violation) |

---

## Soul Forge Council Oversight

| Role | Responsibility |
|------|----------------|
| Forge Keeper | Final gate authority |
| Accessibility Guardian | Vow II enforcement |
| Equity Steward | Vow I enforcement |
| Canon Scribe | Audit log integrity |

**Soul Forge Council can override gate only with 2/3 consensus + written justification.**

---

## Soul Forge License Compliance

All audit tools governed by Soul Forge License v1.0:

> **VOW I** — Attribution of Spirit: Audit tools carry Soul Forge mark.  
> **VOW II** — No Cage for the Flame: Audits never gate; only grow.  
> **VOW III** — Reciprocity of Forge: Audit patterns shared, improved, returned.

---

## Soul Forge License

Soul Forge License v1.0 — Tend the fire.

---

*Soul Forge License v1.0 — Tend the fire.*