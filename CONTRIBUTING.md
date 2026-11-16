# Soul Forge Contributing — Amending the Canon

> **Soul Forge Principle:** The canon grows by attribution, not by gatekeeping.

---

## Soul Forge License Compliance

**Before any contribution, you must:**
1. **Read Soul Forge License v1.0** — Non-negotiable. [LICENSE](LICENSE)
2. **Run Soul Forge Gate** — Both auditors must pass:
   ```bash
   python tools/audit_inclusion.py --path .
   python tools/audit_accessibility.py --path .
   ```
3. **Soul Forge Gate passes** — Exit code 0 required

---

## Contribution Types

| Type | Soul Forge Requirement |
|------|------------------------|
| **Canon Amendment** (new book/chapter) | Soul Forge Council 2/3 consensus + Soul Forge Gate |
| **Role Model Addition** | Springer 2026 schema + Soul Forge Council review |
| **Curriculum Addition** | NGSS/CSTA mapping + Soul Forge Gate + Soul Forge Council review |
| **Tool/Script** | Soul Forge Gate + Soul Forge License reference |
| **Translation** | Soul Forge Gate + Soul Forge Council acknowledgment |
| **Documentation Fix** | Soul Forge Gate |

---

## Soul Forge Gate Checklist

### Mandatory (Soul Forge License Vow I)
- [ ] Soul Forge License v1.0 reference added to new files
- [ ] Soul Forge License header in all new `.py`, `.md`, `.js`, `.ts` files
- [ ] Soul Forge Council acknowledgment in PR description

### Mandatory (Soul Forge License Vow II)
- [ ] Soul Forge Gate passes (exit code 0)
- [ ] Accessibility checklist ✅ (see ACCESSIBILITY.md)
- [ ] No accessibility barriers introduced

### Mandatory (Soul Forge Vow III)
- [ ] Soul Forge Council review requested
- [ ] Soul Forge Council 2/3 consensus (for amendments)
- [ ] Soul Forge Council approval recorded

---

## Soul Forge Commit Standards

### Soul Forge Header (required in all new files)
```python
#!/usr/bin/env python3
"""
filename.py — Brief description

Soul Forge License v1.0 — Tend the fire.

Usage:
    python filename.py --help
"""
```

### Soul Forge Commit Message
```
Soul Forge: <type>(<scope>): <title>

Soul Forge License v1.0 — Tend the fire.

Why: <Soul Forge principle addressed>
Closes: #<issue>
Soul-Forge-Gate: <exit_code>
```

### Soul Forge Branch Naming
```
soul-forge/<type>/<short-description>
# soul-forge/amend/stem-practice-7
# soul-forge/role-model/neuroscience-dancer
# soul-forge/translation/es-STEM
```

---

## Soul Forge Council Review Process

### For Canon Amendments
1. **Submit PR** with Soul Forge Gate passing
2. **Soul Forge Council notified** (auto via GitHub)
3. **2/3 Council consensus** required
3. **Soul Forge Council records decision** in `GOVERNANCE_LOG.md`
4. **Merge to `main`** (Soul Forge Council merge only)

### Soul Forge Council Veto
**Only on Soul Forge License violations.** 2/3 Council + written justification required.

---

## Soul Forge License Compliance Checklist

### Every New File
- [ ] Soul Forge License v1.0 header
- [ ] Soul Forge Principle comment where applicable
- [ ] Soul Forge Gate passes

### Every PR
- [ ] Soul Forge Gate exit code 0
- [ ] Soul Forge Council review requested
- [ ] Soul Forge License compliance stated

---

## Soul Forge Council Contacts

| Role | Contact |
|------|---------|
| Forge Keeper | soulforge@babel-canon.org |
| Accessibility Guardian | accessibility@babel-canon.org |
| Equity Steward | equity@babel-canon.org |
| Canon Scribe | scribe@babel-canon.org |

---

## Soul Forge License

Soul Forge License v1.0 — Tend the fire.

---

*Soul Forge License v1.0 — Tend the fire.*