# Accessibility Mandate — Soul Forge Vow II

> **"No cage for the flame."** — Soul Forge License Vow II

Accessibility is not optional. It is a covenant requirement.

---

## Target Standards

| Domain | Minimum Standard | Soul Forge Standard |
|--------|------------------|---------------------|
| Web Content (docs, portals) | WCAG 2.2 Level AA | WCAG 2.2 Level AAA where achievable |
| CLI Tools | Self-voicing + screen reader compatible | Mandatory |
| WASM/Interactive Experiences | WCAG 2.2 AA + motor alternatives | WCAG 2.2 AAA + zero-barrier entry |
| PDF Documents | PDF/UA-1 | PDF/UA-1 + tagged structure |
| Video/Audio Content | Captions + transcripts | Captions + transcripts + ASL option + audio description |

---

## Mandatory Checklist for Every Contribution

### Visual
- [ ] Color contrast ≥ 4.5:1 (text), 3:1 (UI components)
- [ ] No color-only information (use patterns/text/icons too)
- [ ] Alt text for all images, diagrams, charts, graphs
- [ ] Responsive text (no fixed px for body text)
- [ ] Focus indicators visible (min 2px, 3:1 contrast)
- [ ] Text spacing override supported (WCAG 2.2 1.4.12)

### Auditory
- [ ] Captions for all video/audio (closed, accurate, synchronized)
- [ ] Transcripts for all audio (including podcasts)
- [ ] Sign language option for key content (priority: onboarding, safety)
- [ ] No auto-playing audio (> 3 seconds requires pause/stop)

### Motor
- [ ] All functionality keyboard accessible (Tab/Shift+Tab navigation)
- [ ] No keyboard traps (focus can always escape)
- [ ] Target size ≥ 44×44 CSS pixels (touch/pointer)
- [ ] Drag-and-drop has keyboard alternative
- [ ] Timing adjustable (no essential time limits)
- [ ] Single-pointer gestures have multi-pointer alternative

### Cognitive
- [ ] Clear heading hierarchy (H1 → H2 → H3 — no skips)
- [ ] Plain language (reading level ≤ grade 9 / Flesch-Kincaid)
- [ ] Consistent navigation and identification
- [ ] Error messages: What + Where + How to fix
- [ ] No flashing content (> 3 flashes/second)
- [ ] Predictable functionality

### Assistive Technology
- [ ] Tested with NVDA (Windows) + Firefox
- [ ] Tested with VoiceOver (macOS/iOS) + Safari
- [ ] Tested with TalkBack (Android) + Chrome
- [ ] ARIA landmarks on all pages (banner, main, navigation, contentinfo)
- [ ] Live regions for dynamic content (status, alerts)
- [ ] Form labels properly associated (`<label for="id">` or `aria-labelledby`)

### Multilingual
- [ ] `lang` attribute on `<html>` element
- [ ] `lang` on content changes (e.g., `<span lang="es">`)
- [ ] RTL support for Arabic/Hebrew/Farsi
- [ ] Character encoding UTF-8

---

## Testing Protocol

### Automated (Every PR)
```bash
# CLI tools
python -m axe_core.cli --path <output>

# Web applications
npx playwright test --project=accessibility

# Documentation
python tools/audit_accessibility.py --path .
```

### Manual (Before Merge)
1. Navigate entire feature with **keyboard only** (no mouse)
2. Test with **NVDA + Firefox** (Windows)
3. Test with **VoiceOver + Safari** (macOS/iOS)
3. Test with **TalkBack + Chrome** (Android)
4. Test **zoom 200%** — no horizontal scroll
5. Test **high contrast mode** (OS level)
6. Test **text spacing** override (CSS `line-height`, `letter-spacing`, `word-spacing`)

### Annual Audit
- Full WCAG 2.2 AA evaluation by third party
- Soul Forge Council review of accessibility debt
- Report published in `audits/accessibility-<year>.md`
- Remediation within 90 days

---

## Soul Forge Vow II Enforcement

**Every accessibility barrier is a P0 bug — Soul Forge Vow II violation.**

Report to: **accessibility@babel-canon.org**

Include:
1. Tool/page/URL
2. Assistive technology (name + version)
3. Exact steps to reproduce
4. Expected vs actual behavior
5. Screenshot/video if possible

**Response SLA:**
- 24-hour acknowledgment
- 7-day triage by Soul Forge Council
- 30-day fix target
- Public tracking in GitHub Issues

---

## Conformance Status (2026-11-16)

| Area | Target | Status |
|------|--------|--------|
| Web content (docs, portal) | WCAG 2.2 AA | 🚧 Auditing |
| CLI tools | Self-voicing + SR compatible | 🚧 Auditing |
| WASM experiences | WCAG 2.2 AA + motor | ✅ Verified (wasm-education) |
| PDF exports | PDF/UA-1 | 🚧 Auditing |
| Video content | Captions + transcripts + ASL | 🚧 Auditing |

---

## Resources

- [Soul Forge License Vow II](LICENSE#vow-ii--no-cage-for-the-flame)
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/Understanding/)
- [axe-core](https://github.com/dequelabs/axe-core)
- [W3C ARIA Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Soul Forge License](LICENSE)

---

*Last audited: 2026-11-16*  
*Next audit: 2027-02-16*  
*Standard: Soul Forge License Vow II + WCAG 2.2 AA*