#!/usr/bin/env python3
"""
generate_lesson.py — Standards-aligned lesson plan generator

Soul Forge License v1.0 — Tend the fire.

Usage:
    python generate_lesson.py --topic circuits --grade 6 --standard NGSS-MS-PS3
    python generate_lesson.py --interactive
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Standards mappings
NGSS_BY_GRADE = {
    "K": ["NGSS-K-PS2-1", "NGSS-K-LS1-1", "NGSS-K-ESS2-1"],
    "1": ["NGSS-1-PS4-1", "NGSS-1-LS1-1", "NGSS-1-ESS1-1"],
    "2": ["NGSS-2-PS1-1", "NGSS-2-LS2-1", "NGSS-2-ESS1-1"],
    "3": ["NGSS-3-PS2-1", "NGSS-3-LS1-1", "NGSS-3-ESS2-1"],
    "4": ["NGSS-4-PS3-1", "NGSS-4-LS1-1", "NGSS-4-ESS3-1"],
    "5": ["NGSS-5-PS1-1", "NGSS-5-LS2-1", "NGSS-5-ESS2-1"],
    "6": ["NGSS-MS-PS3-2", "NGSS-MS-LS1-1", "NGSS-MS-ESS2-1"],
    "7": ["NGSS-MS-PS1-1", "NGSS-MS-LS2-1", "NGSS-MS-ESS3-1"],
    "8": ["NGSS-MS-PS2-1", "NGSS-MS-LS3-1", "NGSS-MS-ESS1-1"],
    "9": ["NGSS-HS-PS3-2", "NGSS-HS-LS1-1", "NGSS-HS-ESS2-1"],
    "10": ["NGSS-HS-PS4-1", "NGSS-HS-LS2-1", "NGSS-HS-ESS3-1"],
    "11": ["NGSS-HS-PS2-1", "NGSS-HS-LS3-1", "NGSS-HS-ESS2-1"],
    "12": ["NGSS-HS-PS4-1", "NGSS-HS-LS4-1", "NGSS-HS-ESS3-1"],
}

CSTA_BY_GRADE = {
    "K": ["CSTA-K-CS-01"],
    "1": ["CSTA-1A-CS-01"],
    "2": ["CSTA-1A-CS-02"],
    "3": ["CSTA-1B-CS-01"],
    "4": ["CSTA-1B-CS-02"],
    "5": ["CSTA-1B-CS-03"],
    "6": ["CSTA-2-AP-01"],
    "7": ["CSTA-2-AP-02"],
    "8": ["CSTA-2-IC-01"],
    "9": ["CSTA-3A-AP-01"],
    "10": ["CSTA-3A-IC-01"],
    "11": ["CSTA-3B-AP-01"],
    "12": ["CSTA-3B-IC-01"],
}

TOPICS = {
    "circuits": {
        "ngss_core": "NGSS-MS-PS3",
        "csta_core": "CSTA-1B-CS",
        "practices": ["Belonging and Relevance", "Investigation", "Stereotype Challenge", "Collaborative Work"],
        "role_models": ["electrical-engineer-001"],
        "materials_base": ["battery", "foil", "LED", "tape"],
    },
    "bridge": {
        "ngss_core": "NGSS-MS-ETS1",
        "csta_core": "CSTA-1B-AP",
        "practices": ["Investigation", "Normalized Struggle", "Collaborative Work"],
        "role_models": ["civil-engineer-001"],
        "materials_base": ["craft sticks", "glue", "weights"],
    },
    "coding": {
        "ngss_core": "NGSS-MS-ETS1",
        "csta_core": "CSTA-1B-AP",
        "practices": ["Investigation", "Normalized Struggle", "Stereotype Challenge"],
        "role_models": ["software-engineer-001"],
        "materials_base": ["computer", "internet"],
    },
    "ecosystems": {
        "ngss_core": "NGSS-MS-LS2",
        "csta_core": "CSTA-1B-DA",
        "practices": ["Belonging and Relevance", "Investigation", "Collaborative Work"],
        "role_models": ["ecologist-001"],
        "materials_base": ["jar", "water", "plants"],
    },
    "earth-systems": {
        "ngss_core": "NGSS-MS-ESS2",
        "csta_core": "CSTA-1B-DA",
        "practices": ["Belonging and Relevance", "Investigation", "Normalized Struggle", "Collaborative Work"],
        "role_models": ["earth-systems-engineer-001"],
        "materials_base": ["soil", "rocks", "water", "plants", "magnifying glass"],
    },
}

ROLE_MODEL_TEMPLATES = {
    "electrical-engineer-001": {
        "name": "Maya",
        "title": "Electrical Engineer",
        "story": "I design power systems for remote villages. As a kid, I loved taking apart my mom's blender — she wasn't thrilled! I also love salsa dancing and cooking tamales with my abuela. My path wasn't straight: I worked at a bakery for two years before engineering school. Now I get to bring light to places that never had it.",
        "stereotypes_challenged": ["Latina", "dancer", "baker", "non-linear path"],
        "hobbies": ["salsa dancing", "cooking"],
    },
    "civil-engineer-001": {
        "name": "Jordan",
        "title": "Civil Engineer",
        "story": "I design bridges that communities walk on every day. I grew up building LEGO cities that took over my bedroom floor. I'm also a competitive rock climber and volunteer at a community garden. Engineering isn't just calculations — it's about people.",
        "stereotypes_challenged": ["climber", "gardener", "community-focused"],
        "hobbies": ["rock climbing", "gardening"],
    },
    "software-engineer-001": {
        "name": "Alex",
        "title": "Software Engineer",
        "story": "I write code that helps scientists track endangered species. I started coding at 28 after teaching yoga for five years. I'm also a queer non-binary person who loves speculative fiction and baking sourdough. Code is just another language for solving puzzles.",
        "stereotypes_challenged": ["late starter", "yoga teacher", "queer", "non-binary", "baker"],
        "hobbies": ["yoga", "speculative fiction", "sourdough"],
    },
    "ecologist-001": {
        "name": "Dr. Chen",
        "title": "Marine Ecologist",
        "story": "I study how kelp forests survive warming oceans. I grew up tide-pooling with my grandfather in Taiwan. I'm also a traditional calligrapher and marathon runner. Science and art both require patience and attention to detail.",
        "stereotypes_challenged": ["Asian scientist", "calligrapher", "runner", "elder-influenced"],
        "hobbies": ["calligraphy", "marathon running"],
    },
    "earth-systems-engineer-001": {
        "name": "Dr. Rivera",
        "title": "Earth Systems Engineer",
        "story": "I design living infrastructure that heals watersheds and rebuilds soil carbon. As a kid, I collected rocks from every hike — my pockets were always full. I'm also a potter and seed saver. My path wasn't straight: I was the first in my family to go to college, and field access was never guaranteed. Now I engineer living systems that heal the critical zone — the skin of the Earth where rock meets life.",
        "stereotypes_challenged": ["first_gen_college", "potter", "seed_saver", "field_access"],
        "hobbies": ["hiking", "pottery", "seed_saving"],
    },
}

TEMPLATE = """---
id: "{id}"
title: "{title}"
grade: {grade}
standards:
{standards}
topic: "{topic}"
subtopic: "{subtopic}"
duration_minutes: {duration}
materials_cost: 0
accessibility:
  visual: true
  auditory: true
  motor: true
  cognitive: true
languages: ["en", "es"]
evidence: "{evidence}"
role_model_id: "{role_model_id}"
practices:
{practices}
---

# {title}

**Driving Question:** *{driving_question}*

---

## Learning Targets

By the end of this lesson, learners will be able to:
{learning_targets}

---

## Materials (Cost: $0 - all household items)

{materials_table}

---

## Facilitator Preparation

### Before Session
{pre_session}

### Accessibility Notes
{accessibility_notes}

---

## Session Flow ({duration} minutes)

### 1. Technology Babies Icebreaker (5 min) — *Brite Practice 1*

**Prompt:** *"Think back to your first memory using digital technology. How old were you? What did you use? What else do you remember?"*

**Process:**
1. Think silently (30 sec)
2. Share with elbow partner (1 min each)
3. Volunteer shares to group (2 min)

**Why:** Connects personal identity to technology; builds community.

---

### 2. Role Model Story: {role_model_name} (5 min) — *Brite Practice 3*

**Show/Read:** *{role_model_name}'s Story Card* (in materials)

> "{role_model_story}"

**Discussion (2 min):**
- "What surprised you about {role_model_name}?"
- "What do you have in common with {role_model_name}?"

---

### 3. {investigation_title} (15 min) — *Brite Practice 2*

**Challenge:** *{investigation_challenge}*

**Structure:**
1. **Plan** (3 min): Sketch 2 designs in journal
2. **Build** (5 min): Try Design 1
3. **Test & Debug** (5 min): Struggle Journal entry
4. **Iterate** (2 min): Try Design 2 if needed

**Struggle Journal Prompt:**
> **Stuck point:** _________________________
> **Strategy tried:** _____________________
> **Result:** _____________________________
> **Next strategy:** ______________________

**Facilitator moves:**
- "Three before me" — self → peer → resource → facilitator
- Celebrate failed attempts: "That's data! What did it tell you?"
- Document successful {investigation_noun} (photo for gallery)

---

### 4. Design for Community (12 min) — *Brite Practice 1 + 5*

**Prompt:** *Now design a {design_noun} that solves a real problem WHERE YOU LIVE.*

**Examples from past learners:**
{community_examples}

**Process:**
1. **Pair up** — Different strengths (builder + drawer + writer)
2. **Choose problem** — Each shares one community need
3. **Co-design** — One {design_noun} that helps both
4. **Document** — Sketch + 3-sentence explanation

**Roles (rotate):**
- **Builder** — Assembles {design_noun}
- **Recorder** — Sketches + Struggle Journal
- **Communicator** — Explains to group

---

### 5. Gallery Walk + Reflection (8 min) — *Brite Practice 6*

**Gallery Walk (4 min):**
- Half groups display {design_noun}s; half visit
- **Visitor gives:** One "I like..." + One "What if..."
- **Host records:** Feedback in Struggle Journal

**Switch & repeat (4 min)**

**Closing Reflection (whole group):**
> "One thing I learned about {topic_lower}: _________"
> "One thing I learned about MYSELF: _________"

---

## Assessment

### Mastery Indicators
{mastery_table}

### Portfolio Artifacts
- Struggle Journal (required)
- {design_noun} sketch + community problem statement (required)
- Peer feedback received (required)
- Photo of working {design_noun} (optional)

---

## Extensions

{extensions_table}

---

## Family Connection (send home)

**Family {topic_title} Challenge:**
> "{family_challenge}"

Return photo/drawing for **Community Gallery**.

---

## Standards Alignment Detail

{standards_table}

---

## Role Model Integration

**{role_model_name}** (ID: {role_model_id})
- **Story source:** First-person interview (2026)
- **Media:** 2-min video + story card + photo
- **Stereotypes challenged:** {stereotypes_challenged}
- **Pathway:** {pathway}
- **Hobbies:** {hobbies}
- **Challenge shared:** "{challenge_shared}"

---

## Materials for Facilitator

### Required
{facilitator_required}

### Optional
{facilitator_optional}

---

*Generated: {generated_date}*  
*Review: {review_date}*  
*Source: Soul Forge License + NGCP Brite Practices + NGSS + CSTA*
"""


def generate_lesson(
    topic: str,
    grade: str,
    standard: str = None,
    duration: int = 45,
    output_dir: str = None,
) -> str:
    """Generate a lesson plan from template."""
    
    if topic not in TOPICS:
        raise ValueError(f"Unknown topic: {topic}. Available: {list(TOPICS.keys())}")
    
    if grade not in NGSS_BY_GRADE:
        raise ValueError(f"Grade must be K-12, got: {grade}")
    
    t = TOPICS[topic]
    role_model_id = t["role_models"][0]
    role_model = ROLE_MODEL_TEMPLATES[role_model_id]
    
    # Build standards list
    ngss_standards = NGSS_BY_GRADE[grade]
    csta_standards = CSTA_BY_GRADE[grade]
    
    if standard:
        # Use specific standard if provided
        if standard.startswith("NGSS"):
            ngss_standards = [standard]
        elif standard.startswith("CSTA"):
            csta_standards = [standard]
    
    standards_yaml = ""
    for s in ngss_standards:
        standards_yaml += f"  - {s}\n"
    for s in csta_standards:
        standards_yaml += f"  - {s}\n"
    
    # Generate unique ID
    import datetime
    import uuid
    short_uuid = str(uuid.uuid4())[:8]
    lesson_id = f"{topic}-ngss-{grade}-{short_uuid}"
    
    # Topic-specific content
    topic_configs = {
        "circuits": {
            "investigation_title": "Circuit Investigation",
            "investigation_challenge": "Light the LED using ONLY the materials at your table.",
            "investigation_noun": "circuit",
            "design_noun": "circuit",
            "community_examples": "- \"Grandma's nightlight for bathroom trips\"\n- \"Bike light for dark streets\"\n- \"Study lamp for shared bedroom\"\n- \"Chicken coop sensor for abuelo\"",
            "family_challenge": "Together, find one thing in your home that uses a circuit. Draw it together. Talk about: What problem does it solve for your family?",
            "topic_lower": "circuits",
            "topic_title": "Circuit",
            "design_noun_plural": "circuits",
        },
        "bridge": {
            "investigation_title": "Bridge Building",
            "investigation_challenge": "Build a bridge that spans 30cm and holds 500g.",
            "investigation_noun": "bridge",
            "design_noun": "bridge",
            "community_examples": "- \"Safe path over neighborhood ditch\"\n- \"Bike bridge over park stream\"\n- \"Access ramp for community garden\"\n- \"Crossing for elderly neighbor\"",
            "family_challenge": "Together, find one bridge in your community. Draw it together. Talk about: Who uses it? What would happen without it?",
            "topic_lower": "bridges",
            "topic_title": "Bridge",
            "design_noun_plural": "bridges",
        },
        "coding": {
            "investigation_title": "Code Exploration",
            "investigation_challenge": "Create a program that tells an interactive story.",
            "investigation_noun": "program",
            "design_noun": "program",
            "community_examples": "- \"App for abuela's medication reminders\"\n- \"Game teaching little cousin colors\"\n- \"Website for family recipe sharing\"\n- \"Tool for neighbor's garden planning\"",
            "family_challenge": "Together, think of one thing in your daily life that could be easier with a simple program. Draw the screens together.",
            "topic_lower": "programming",
            "topic_title": "Program",
            "design_noun_plural": "programs",
        },
        "ecosystems": {
            "investigation_title": "Ecosystem in a Jar",
            "investigation_challenge": "Build a self-sustaining micro-ecosystem.",
            "investigation_noun": "ecosystem",
            "design_noun": "ecosystem",
            "community_examples": "- \"Balcony garden for apartment\"\n- \"Water filter for camping\"\n- \"Compost system for kitchen\"\n- \"Butterfly habitat for neighborhood\"",
            "family_challenge": "Together, observe one small ecosystem near your home (puddle, garden, park corner). Draw and label what you see.",
            "topic_lower": "ecosystems",
            "topic_title": "Ecosystem",
            "design_noun_plural": "ecosystems",
        },
        "rockets": {
            "investigation_title": "Rocket Launch",
            "investigation_challenge": "Launch a film-canister rocket using chemical reaction.",
            "investigation_noun": "rocket",
            "design_noun": "rocket",
            "community_examples": "- \"Signal rocket for family camping\"\n- \"Science demo for little cousin's class\"\n- \"Launch for neighborhood block party\"\n- \"Competition for after-school club\"",
            "family_challenge": "Together, design a paper rocket. Test different fin shapes. Which flies farthest?",
            "topic_lower": "rockets",
            "topic_title": "Rocket",
            "design_noun_plural": "rockets",
        },
    }
    
    tc = topic_configs[topic]
    
    # Build template variables
    practices_yaml = ""
    for p in t["practices"]:
        practices_yaml += f"  - \"{p}\"\n"
    
    standards_table = ""
    for s in ngss_standards:
        standards_table += f"| {s} | Learners engage with this standard through hands-on {topic} design. |\n"
    for s in csta_standards:
        standards_table += f"| {s} | Learners apply this computing concept in {topic} context. |\n"
    
    mastery_rows = [
        "| Indicator | Emerging | Developing | Mastery |",
        "|-----------|----------|------------|---------|",
        f"| **{topic_title} understanding** | Copies working model | Explains own design | Explains + predicts modifications |",
        f"| **Problem framing** | Uses given example | Adapts example to self | Identifies original community need |",
        "| **Collaboration** | Participates when asked | Shares ideas + materials | Rotates roles, integrates feedback |",
        "| **Struggle strategy** | Gives up / waits | Tries 1 strategy | Documents 2+ strategies, persists |",
    ]
    mastery_table = "\n".join(mastery_rows)
    
    materials_rows = ["| Item | Qty per group | Alternative |", "|------|---------------|-------------|"]
    for item in t["materials_base"]:
        materials_rows.append(f"| {item} | 1 | Household alternative |")
    materials_table = "\n".join(materials_rows)
    
    extensions_rows = [
        "| Learner Need | Extension |",
        "|--------------|-----------|",
        "| **More challenge** | Add complexity (sensor, switch, parallel design) |",
        "| **Less motor** | Pre-assembled base; focus on problem framing |",
        "| **ELL** | Bilingual Struggle Journal; visual sequence cards |",
        "| **Advanced** | Micro:bit/Arduino version; sensor integration |",
    ]
    extensions_table = "\n".join(extensions_rows)
    
    # Fill template
    content = TEMPLATE.format(
        id=lesson_id,
        title=f"Design a {tc['topic_title'].lower()}",
        grade=[int(grade)] if grade.isdigit() else grade,
        standards=standards_yaml,
        topic=topic,
        subtopic=tc["investigation_noun"].title(),
        duration=duration,
        driving_question=f"How can I use {topic} to solve a problem in my community?",
        learning_targets="\n".join([
            f"1. **Explain** how {topic} transfers energy/information (NGSS)",
            f"2. **Design** a {tc['design_noun']} that solves a personal/community need (CSTA)",
            f"3. **Collaborate** with a team to iterate on a design",
            f"4. **Reflect** on how their identity connects to {topic} professions",
        ]),
        materials_table=materials_table,
        pre_session="- [ ] Test one {investigation_noun} yourself\n- [ ] Print/access role model story: **{role_model_name}**\n- [ ] Prepare \"Technology Babies\" icebreaker materials\n- [ ] Set up materials stations".format(
            investigation_noun=tc["investigation_noun"],
            role_model_name=role_model["name"]
        ),
        accessibility_notes="- **Visual**: High-contrast diagram provided; components pre-identified tactilely\n- **Auditory**: Verbal step-by-step; no audio-only instructions\n- **Motor**: Pre-prepped components; tape pre-teared\n- **Cognitive**: Visual sequence cards; chunked instructions (max 3 steps)\n- **Language**: All text in EN + ES; key terms glossary",
        role_model_story=role_model["story"],
        investigation_title=tc["investigation_title"],
        investigation_challenge=tc["investigation_challenge"],
        investigation_noun=tc["investigation_noun"],
        design_noun=tc["design_noun"],
        community_examples=tc["community_examples"],
        family_challenge=tc["family_challenge"],
        topic_lower=tc["topic_lower"],
        topic_title=tc["topic_title"],
        design_noun_plural=tc["design_noun_plural"],
        role_model_id=role_model_id,
        mastery_table=mastery_table,
        standards_table=standards_table,
        role_model_name=role_model["name"],
        stereotypes_challenged=", ".join(role_model["stereotypes_challenged"]),
        pathway="Non-linear: " + " → ".join(role_model["story"].split(". ")[2:4]),
        hobbies=", ".join(role_model["hobbies"]),
        challenge_shared=role_model["story"].split(". ")[-1],
        facilitator_required="- [ ] Role model story cards (printed/digital)\n- [ ] Struggle Journal template (one per learner)\n- [ ] Visual sequence cards ({investigation_noun} steps)\n- [ ] Bilingual glossary (EN/ES)".format(investigation_noun=tc["investigation_noun"]),
        facilitator_optional="- [ ] Micro:bit extension kit\n- [ ] Digital gallery platform (Padlet/GitHub Discussions)\n- [ ] Family take-home packets",
        generated_date=datetime.date.today().isoformat(),
        review_date=(datetime.date.today().replace(year=datetime.date.today().year + 1)).isoformat(),
        extensions_table=extensions_table,
    )
    
    # Write output
    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        output_path = Path(output_dir) / f"{lesson_id}.md"
        output_path.write_text(content, encoding="utf-8")
        return str(output_path)
    
    return content


def main():
    parser = argparse.ArgumentParser(
        description="Generate standards-aligned STEM lesson plans",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Use --help for more options"
    )
    parser.add_argument("--topic", choices=list(TOPICS.keys()), help="Lesson topic")
    parser.add_argument("--grade", help="Grade level (K-12)")
    parser.add_argument("--standard", help="Specific standard (e.g., NGSS-MS-PS3)")
    parser.add_argument("--duration", type=int, default=45, help="Duration in minutes")
    parser.add_argument("--output-dir", help="Output directory")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--list-topics", action="store_true", help="List available topics")
    parser.add_argument("--list-role-models", action="store_true", help="List role models")
    
    # --help is auto-added by argparse
    
    args = parser.parse_args()
    
    if args.list_topics:
        print("Available topics:")
        for t, cfg in TOPICS.items():
            print(f"  {t:15} - {cfg['ngss_core']} + {cfg['csta_core']}")
        return
    
    if args.list_role_models:
        print("Available role models:")
        for rid, rm in ROLE_MODEL_TEMPLATES.items():
            print(f"  {rid:30} - {rm['name']} ({rm['title']})")
        return
    
    if args.interactive:
        print("STEM Lesson Generator — Interactive Mode")
        print("=" * 50)
        topic = input(f"Topic {list(TOPICS.keys())}: ").strip()
        grade = input("Grade (K-12): ").strip()
        standard = input("Specific standard (optional): ").strip() or None
        duration = int(input("Duration minutes [45]: ") or "45")
        output_dir = input("Output directory [curriculum/grade/X]: ").strip() or None
    else:
        if not args.topic or not args.grade:
            parser.error("--topic and --grade required (or use --interactive)")
        topic = args.topic
        grade = args.grade
        standard = args.standard
        duration = args.duration
        output_dir = args.output_dir
    
    # Default output dir
    if not output_dir:
        grade_dir = f"curriculum/grade/{grade}-{int(grade)+2 if grade.isdigit() else grade}"
        output_dir = grade_dir
    
    try:
        path = generate_lesson(topic, grade, standard, duration, output_dir)
        print(f"[OK] Generated: {path}")
    except Exception as e:
        print(f"[FAIL] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()