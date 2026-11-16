# Soul Forge Assessment — Mastery-Based, Identity-Inclusive

> **Soul Forge Principle:** "The soul knows its smith." Assessment serves the learner's growth, not sorting.

---

## Soul Forge Mastery Levels

**No Grades. No Rankings. Soul Growth Only.**

| Level | Name | Soul State | Indicators |
|-------|------|------------|------------|
| 1 | **Exploring** | Copies models, participates when guided | Follows instructions, needs step-by-step, minimal Struggle Journal |
| 2 | **Developing** | Adapts models, documents strategies independently | Modifies designs, explains reasoning, Struggle Journal with 1 strategy |
| 3 | **Mastering** | Creates originals, mentors peers, persists through ambiguity | Designs from scratch, mentors others, Struggle Journal with 2+ strategies |

**Identity Bonus (+5%)** — Learner documents STEM-self connection in portfolio.

---

## Core Domains (Soul Forge Weighted)

Every assessment evaluates five soul domains:

| Domain | Weight | Soul Question |
|--------|--------|---------------|
| **Conceptual Understanding** | 0.30 | Explains core concepts, predicts outcomes, connects to real world |
| **Problem Framing** | 0.20 | Identifies authentic community problems, defines scope, sets criteria |
| **Design Process** | 0.25 | Plans, builds, tests, documents iterations, uses feedback |
| **Collaboration** | 0.15 | Rotates roles, integrates peer feedback, communicates clearly |
| **Identity Reflection** | 0.10 | Connects STEM to self, documents struggle strategies, names future self |

*Topic-specific competencies add 0.10 weight (normalized to 1.0 total)*

---

## Mastery Rubric (Soul Forge Standard)

### Conceptual Understanding
| Exploring | Developing | Mastering |
|-----------|------------|-----------|
| Copies working model | Explains own design | Explains + predicts modifications |
| Names components | Traces energy/information flow | Predicts effects of modifications |

### Problem Framing
| Exploring | Developing | Mastering |
|-----------|------------|-----------|
| Uses given example | Adapts example to self | Identifies original community need |
| Solves presented problem | Modifies problem for relevance | Generates novel community problem |

### Design Process
| Exploring | Developing | Mastering |
|-----------|------------|-----------|
| Follows instructions exactly | Documents 1 strategy iteration | Documents 2+ strategies, persists |
| Builds single prototype | Iterates once with feedback | Iterates until criteria met |

### Collaboration
| Exploring | Developing | Mastering |
|-----------|------------|-----------|
| Participates when guided | Shares ideas + materials | Rotates roles, integrates feedback |
| Works alongside peers | Explains reasoning to peers | Mentors peers through ambiguity |

### Identity Reflection
| Exploring | Developing | Mastering |
|-----------|------------|-----------|
| Names activity | Documents 1 strategy | Documents 2+ strategies + self-connection |
| "I built a circuit" | "I got stuck on X, tried Y" | "This connects to my identity as Z because..." |

---

## Identity Bonus (+5% Soul Forge Bonus)

**Soul Forge Principle:** "The soul knows its smith."

Learners earn a **5% mastery bonus** when portfolio includes:

```yaml
identity_reflection:
  stem_self_connection: true  # "I am a STEM person because..."
  future_self_named: true     # "I see myself as [role] because..."
  struggle_as_growth: true    # "My stuck moments taught me..."
  community_impact_named: true # "This solves [problem] for [community]"
```

**Soul Forge Council ruling:** Identity bonus is not extra credit — it's soul alignment.

---

## Portfolio Evidence Map

Every learner portfolio maps evidence to soul domains:

```json
{
  "portfolio_id": "student-12345",
  "grade": 7,
  "topic": "circuits",
  "evidence": {
    "conceptual_understanding": [
      {"type": "diagram", "description": "Energy flow in LED circuit", "self_explanation": true},
      {"type": "prediction", "description": "What happens if I add second battery?"}
    ],
    "problem_framing": [
      {"type": "community_problem", "description": "Grandma's nightlight for bathroom trips"}
    ],
    "design_process": [
      {"type": "struggle_journal", "entries": 3, "strategies": ["reversed LED", "added foil", "taped tighter"]},
      {"type": "prototype_photo", "description": "Working circuit iteration 3"}
    ],
    "collaboration": [
      {"type": "peer_feedback", "from": "partner-123", "content": "I like your tape technique"},
      {"type": "role_rotation", "roles": ["builder", "recorder", "communicator"]}
    ],
    "identity_reflection": {
      "stem_self_connection": true,
      "future_self_named": true,
      "struggle_as_growth": true,
      "community_impact_named": true,
      "reflection_text": "I never thought I could build something that helps my abuela. Now I see myself as an engineer who solves problems for my family."
    }
  }
}
```

---

## Soul Forge Certification Pathway

**Cost: Free** — Soul Forge License: Reciprocity of Forge

### Phase 1: Foundations (Week 1)
- Soul Forge License philosophy (Three Vows)
- Six NGCP Brite Practices
- Soul Forge Mastery Levels
- Soul Forge License Vow II (Accessibility mandatory)

### Phase 2: Practice (Weeks 2-3)
- Run 3 practice sessions (recorded)
- Complete Struggle Journal yourself
- Peer feedback via Soul Forge Gallery Walk

### Phase 3: Soul Forge Certification (Week 4)
- Live observed session (Soul Forge Council observer)
- Portfolio review (Soul Forge Assessment System)
- Identity Reflection Essay (Soul Forge principle)

**Soul Forge Certificate** — Valid 2 years. Renewal: 1 observed session + updated portfolio.

---

## Soul Forge Assessment System Integration

```bash
# Generate rubric
python assessment_rubric.py --generate --topic circuits --grade 6 --output rubric.json

# Evaluate portfolio
python assessment_rubric.py --evaluate --portfolio portfolio.json --rubric rubric.json
```

**Soul Forge Bonus applied automatically** when `identity_reflection` fields present.

---

## Soul Forge License Compliance

All assessment tools governed by Soul Forge License v1.0:

> **VOW I** — Attribution of Spirit: Learner's soul knows its smith.  
> **VOW II** — No Cage for the Flame: Assessment never gates; only grows.  
> **VOW III** — Reciprocity of Forge: Rubrics shared, improved, returned.

---

*Soul Forge License v1.0 — Tend the fire.*