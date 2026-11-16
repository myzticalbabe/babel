# Assessment Techniques — Mastery-Based, Identity-Inclusive

> **Soul Forge Principle:** "The soul knows its smith." Assessment serves growth, not sorting.

---

## Mastery Level Definitions

| Level | Name | Soul State | Observable Indicators |
|-------|------|------------|----------------------|
| 1 | **Exploring** | Copies models, participates when guided | Follows instructions, needs step-by-step, minimal Struggle Journal |
| 2 | **Developing** | Adapts models, documents strategies independently | Modifies designs, explains reasoning, Struggle Journal with 1 strategy |
| 3 | **Mastering** | Creates originals, mentors peers, persists through ambiguity | Designs from scratch, mentors others, Struggle Journal with 2+ strategies |

**Identity Bonus (+5% mastery)** — Documented STEM-self connection in portfolio.

---

## Five Core Domains (Soul Forge Weighted)

| Domain | Weight | Soul Question |
|--------|--------|---------------|
| **Conceptual Understanding** | 0.30 | Explains core concepts, predicts outcomes, connects to real world |
| **Problem Framing** | 0.20 | Identifies authentic community problems, defines scope, sets criteria |
| **Design Process** | 0.25 | Plans, builds, tests, documents iterations, uses feedback |
| **Collaboration** | 0.15 | Rotates roles, integrates peer feedback, communicates clearly |
| **Identity Reflection** | 0.10 | Connects STEM to self, documents struggle strategies, names future self |

*Topic-specific competencies add 0.10 (normalized to 1.0 total)*

---

## Mastery Rubric (Observable Behaviors)

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

## Identity Bonus (+5% Mastery)

**Soul Forge Principle:** "The soul knows its smith."

Learner earns **+5% mastery** when portfolio includes all four:

```yaml
identity_reflection:
  stem_self_connection: true      # "I am a STEM person because..."
  future_self_named: true         # "I see myself as [role] because..."
  struggle_as_growth: true        # "My stuck moments taught me..."
  community_impact_named: true    # "This solves [problem] for [community]"
```

**Soul Forge Ruling:** Identity bonus is not extra credit — it's soul alignment.

---

## Portfolio Evidence Map (Template)

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

## Assessment Conversation Scripts

### Formative Check-In (5 min, during build)
> **Facilitator:** "Walk me through your design. What's the energy path?"
> **Learner:** [Explains]
> **Facilitator:** "What would happen if you changed [component]?"
> **Learner:** [Predicts]
> **Facilitator:** "Test it. What did you learn?"

### Summative Portfolio Review (15 min, end of unit)
> **Facilitator:** "Show me your Struggle Journal. Which entry are you proudest of?"
> **Learner:** [Shares]
> **Facilitator:** "How does this connect to who you want to become?"
> **Learner:** [Identity reflection]
> **Facilitator:** "What would you tell someone starting this project?"

### Identity Reflection Prompt (End of unit)
> "Write or record: **I never thought I could ______. Now I see myself as ______ because ______.**"

---

## Assessment Conversation Quick-Reference Card

| Question Type | Prompt | Listen For |
|---------------|--------|------------|
| **Conceptual** | "What would happen if...?" | Causal reasoning, not guessing |
| **Metacognitive** | "What did you try when stuck?" | Specific strategy, not "I thought harder" |
| **Identity** | "How does this connect to you?" | Personal connection, not "it's cool" |
| **Collaborative** | "What did your partner teach you?" | Specific skill/insight, not "they helped" |
| **Community** | "Who does this help?" | Specific person/group, not "everyone" |

---

## Mastery Determination (Algorithm)

```python
def determine_mastery(domain_scores: dict, identity_bonus: bool) -> dict:
    """Domain scores are 0-1 per domain."""
    composite = sum(score * weight for score, weight in zip(domain_scores.values(), DOMAIN_WEIGHTS))
    if identity_bonus:
        composite = min(composite + 0.05, 1.0)
    
    if composite >= 0.80:
        return {"level": 3, "name": "Mastering"}
    elif composite >= 0.50:
        return {"level": 2, "name": "Developing"}
    else:
        return {"level": 1, "name": "Exploring"}
```

---

## Growth Edges (Auto-Generated)

| Domain Score | Auto-Generated Growth Edge |
|--------------|----------------------------|
| < 0.50 | "Focus on [domain]: currently [score]%" |
| 0.50-0.70 | "Strengthen [domain]: add iteration documentation" |
| > 0.70 | "Mentor others in [domain]: share your strategies" |

---

## No-Grade Policy

**Soul Forge Principle:** "The soul knows its smith."

- No letter grades, no rankings, no curves
- Mastery levels describe soul state, not performance
- Portfolios travel with learner (not locked in LMS)
- Identity bonus = soul alignment, not extra credit

---

*Soul Forge License v1.0 — Tend the fire.*