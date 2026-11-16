#!/usr/bin/env python3
"""
Neuroaffirming Lesson Generator — UDL+ Lesson Generation per Cognitive Profile

Soul Forge License v1.0 — Tend the fire.

Generates lessons that leverage cognitive profiles as assets, not deficits.
Universal Design for Learning (UDL) + neurodiversity-specific creative extensions.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .cognitive_profile_registry import CognitiveProfileSpec, CognitiveProfile, CognitiveProfileEngine

@dataclass
class LessonComponent:
    name: str
    content: str
    accessibility_notes: List[str]
    neuroaffirming_notes: List[str]

@dataclass
class NeuroaffirmingLesson:
    id: str
    title: str
    topic: str
    grade_band: str
    cognitive_profile_focus: List[str]  # Primary profiles this lesson optimizes for
    driving_question: str
    learning_targets: List[str]
    investigation: 'LessonComponent'
    design_challenge: 'LessonComponent'
    identity_reflection: 'LessonComponent'
    collaboration_structure: 'LessonComponent'
    family_connection: 'LessonComponent'
    assessment_rubric: Dict[str, Any]
    materials: List[Dict[str, Any]]
    accessibility_plan: Dict[str, Any]
    neuroaffirming_adaptations: Dict[str, Any]  # Per cognitive profile
    identity_bonus_criteria: Dict[str, Any]

class NeuroaffirmingLessonGenerator:
    """
    Generates neuroaffirming lessons that leverage cognitive profiles as assets.
    
    Universal Design for Learning (UDL) + neurodiversity-specific creative extensions.
    
    Principles:
    - Multiple means of engagement (interest-based, choice, relevance)
    - Multiple means of representation (multimodal, multisensory)
    - Multiple means of action/expression (varied output modalities)
    - Neurodiversity-specific: strengths-based framing, identity affirmation
    """
    
    # Grade-band specific configurations
    GRADE_BANDS = {
        "K-2": {"duration": 30, "complexity": "concrete", "scaffolding": "high"},
        "3-5": {"duration": 45, "complexity": "semi-abstract", "scaffolding": "medium"},
        "6-8": {"duration": 60, "complexity": "abstract", "scaffolding": "medium"},
        "9-12": {"duration": 90, "complexity": "complex", "scaffolding": "low"}
    }
    
    # Topic templates with neuroaffirming framing
    TOPIC_TEMPLATES = {
        "patterns": {
            "ngss_core": "NGSS-1-LS1-1 / NGSS-4-PS4-1",
            "csta_core": "CSTA-1A-AP-08",
            "autistic_focus": ["Pattern Recognition", "Systems Thinking"],
            "adhd_focus": ["Divergent Thinking", "Rapid Iteration"],
            "dyslexic_focus": ["Holistic Thinking", "Spatial Reasoning"],
            "dyspraxic_focus": ["Strategic Thinking", "Empathetic Communication"],
            "driving_question": "How can patterns help us understand and create?",
            "investigation": "Discover patterns in nature, data, and design",
            "design_challenge": "Create a pattern system that solves a community problem",
            "materials": ["pattern blocks", "grid paper", "natural objects", "digital tools"]
        },
        "structures": {
            "ngss_core": "NGSS-2-PS1-2 / NGSS-3-5-ETS1-1",
            "csta_core": "CSTA-1B-IC-18",
            "autistic_focus": ["Systems Thinking", "Detail Precision"],
            "adhd_focus": ["Rapid Iteration", "Novelty Seeking"],
            "dyslexic_focus": ["Spatial Reasoning", "Holistic Thinking"],
            "dyspraxic_focus": ["Strategic Thinking", "Empathetic Communication"],
            "driving_question": "How can we build structures that serve our community?",
            "investigation": "Explore natural and human-made structures",
            "design_challenge": "Design a structure that solves a community need",
            "materials": ["craft sticks", "straws", "clay", "recycled materials", "digital modeling"]
        },
        "data_stories": {
            "ngss_core": "NGSS-3-LS3-1 / NGSS-MS-LS3-1",
            "csta_core": "CSTA-1B-DA-06",
            "autistic_focus": ["Pattern Recognition", "Detail Precision"],
            "adhd_focus": ["Divergent Thinking", "Rapid Iteration"],
            "dyslexic_focus": ["Narrative Reasoning", "Holistic Thinking"],
            "dyspraxic_focus": ["Verbal Reasoning", "Empathetic Communication"],
            "driving_question": "What stories does data tell about our community?",
            "investigation": "Collect, organize, and visualize community data",
            "design_challenge": "Create a data story that inspires action",
            "materials": ["data sets", "chart paper", "digital tools", "art supplies"]
        },
        "energy_systems": {
            "ngss_core": "NGSS-4-PS3-2 / NGSS-MS-PS3-5",
            "csta_core": "CSTA-1B-AP-10",
            "autistic_focus": ["Systems Thinking", "Pattern Recognition"],
            "adhd_focus": ["Rapid Iteration", "Hyperfocus"],
            "dyslexic_focus": ["Systems Visualization", "Holistic Thinking"],
            "dyspraxic_focus": ["Strategic Thinking", "Verbal Reasoning"],
            "driving_question": "How does energy flow through our world?",
            "investigation": "Trace energy transformations in everyday systems",
            "design_challenge": "Design an energy solution for a community need",
            "materials": ["circuits", "solar cells", "motors", "recycled materials", "sensors"]
        },
        "ecosystems": {
            "ngss_core": "NGSS-2-LS2-1 / NGSS-MS-LS2-3",
            "csta_core": "CSTA-1B-DA-07",
            "autistic_focus": ["Systems Thinking", "Pattern Recognition"],
            "adhd_focus": ["Investigation", "Normalized Struggle"],
            "dyslexic_focus": ["Spatial Reasoning", "Holistic Thinking"],
            "dyspraxic_focus": ["Strategic Thinking", "Collaborative Work"],
            "driving_question": "How do living things depend on each other?",
            "investigation": "Build and observe a micro-ecosystem",
            "design_challenge": "Design a solution that supports local biodiversity",
            "materials": ["jar", "water", "plants", "soil", "magnifying glass", "journal"]
        }
    }
    
    def __init__(self, profile_engine=None):
        from .cognitive_profile_registry import CognitiveProfileEngine
        self.profile_engine = profile_engine or CognitiveProfileEngine()
    
    def generate(self, 
                topic: str,
                grade: str,
                target_profiles: List[str] = None,
                context: Dict[str, Any] = None) -> 'NeuroaffirmingLesson':
        """
        Generate a neuroaffirming lesson for a topic and grade band.
        
        Args:
            topic: Topic key (patterns, structures, data_stories, energy_systems, ecosystems)
            grade: Grade level (K-2, 3-5, 6-8, 9-12)
            target_profiles: List of cognitive profiles to optimize for
            context: Additional context (community, place, standards, etc.)
        """
        if topic not in self.TOPIC_TEMPLATES:
            raise ValueError(f"Unknown topic: {topic}. Available: {list(self.TOPIC_TEMPLATES.keys())}")
        
        if grade not in self.GRADE_BANDS:
            raise ValueError(f"Invalid grade band: {grade}")
        
        template = self.TOPIC_TEMPLATES[topic]
        grade_config = self.GRADE_BANDS[grade]
        context = context or {}
        
        # Determine target profiles
        if target_profiles is None:
            # Default: optimize for all four core profiles
            target_profiles = ["autistic", "adhd", "dyslexic", "dyspraxic"]
        
        # Generate lesson ID
        import uuid
        import datetime
        lesson_id = f"{topic}-{grade}-{datetime.datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
        
        # Build lesson components
        lesson = NeuroaffirmingLesson(
            id=lesson_id,
            title=self._generate_title(topic, grade),
            topic=topic,
            grade_band=grade,
            cognitive_profile_focus=target_profiles,
            driving_question=self._generate_driving_question(template, context),
            learning_targets=self._generate_learning_targets(template, grade),
            investigation=self._generate_investigation(template, grade, target_profiles),
            design_challenge=self._generate_design_challenge(template, grade, target_profiles, context),
            identity_reflection=self._generate_identity_reflection(template, target_profiles),
            collaboration_structure=self._generate_collaboration_structure(target_profiles, grade),
            family_connection=self._generate_family_connection(template, context),
            assessment_rubric=self._generate_assessment_rubric(target_profiles),
            materials=self._generate_materials(template, grade),
            accessibility_plan=self._generate_accessibility_plan(target_profiles),
            neuroaffirming_adaptations=self._generate_neuroaffirming_adaptations(target_profiles),
            identity_bonus_criteria=self._generate_identity_bonus_criteria(target_profiles)
        )
        
        return lesson
    
    def _generate_title(self, topic: str, grade: str) -> str:
        titles = {
            "patterns": f"Pattern Detectives: Finding Order in Chaos",
            "structures": f"Community Architects: Building for Belonging",
            "data_stories": f"Data Detectives: Stories Numbers Tell",
            "energy_systems": f"Energy Explorers: Powering Our World",
            "ecosystems": f"Ecosystem Engineers: Designing for Life"
        }
        return f"{titles.get(topic, topic.title())} ({grade})"
    
    def _generate_driving_question(self, template: Dict, context: Dict) -> str:
        base = template["driving_question"]
        community = context.get("community", "")
        if community:
            return f"{base} How does this connect to {community}?"
        return base
    
    def _generate_learning_targets(self, template: Dict, grade: str) -> List[str]:
        base_targets = [
            f"Identify and describe patterns/structures/data/energy/ecosystems in {template.get('topic', 'the world')}",
            f"Design a solution using {template.get('topic', 'STEM concepts')} that helps a community",
            f"Collaborate with peers using your unique cognitive strengths",
            f"Reflect on how your unique thinking style contributes to STEM"
        ]
        
        # Grade-specific adjustments
        grade_adjustments = {
            "K-2": ["Use pictures and words to share ideas", "Work with a partner"],
            "3-5": ["Explain reasoning with evidence", "Give and receive feedback"],
            "6-8": ["Critique and improve designs", "Connect to real-world problems"],
            "9-12": ["Evaluate solutions against criteria", "Communicate to authentic audiences"]
        }
        
        return base_targets + grade_adjustments.get(grade, [])
    
    def _generate_investigation(self, template: Dict, grade: str, 
                               target_profiles: List[str]) -> Dict[str, Any]:
        profile_focus = []
        for profile in target_profiles:
            if profile in template:
                profile_focus.extend(template.get(f"{profile}_focus", []))
        
        return {
            "name": "Investigation",
            "content": template["investigation"],
            "accessibility_notes": [
                "Multiple entry points: visual, hands-on, digital, verbal",
                "Chunked instructions with visual supports",
                "Flexible pacing with check-in points",
                "Multiple representation options (draw, build, write, speak)"
            ],
            "neuroaffirming_notes": [
                f"Strengths leveraged: {', '.join(set(sum([template.get(f'{p}_focus', []) for p in target_profiles], [])))}",
                "Struggle normalized: 'Getting stuck is data. What did it teach you?'",
                "Multiple solution paths celebrated",
                "Interest-based entry points available"
            ],
            "profile_focus": list(set(profile_focus)),
            "duration_minutes": 20
        }
    
    def _generate_design_challenge(self, template: Dict, grade: str,
                                  target_profiles: List[str], context: Dict) -> Dict[str, Any]:
        community = context.get("community", "your community")
        return {
            "name": "Design Challenge",
            "content": f"{template['design_challenge']} in {context.get('place', community)}.",
            "accessibility_notes": [
                "Multiple prototype modalities: physical, digital, drawn, verbal",
                "Flexible materials: low-tech to high-tech options",
                "Clear success criteria with flexible achievement paths",
                "Peer feedback structured with sentence stems"
            ],
            "neuroaffirming_notes": [
                "Iteration framed as 'data gathering' not failure",
                "Multiple valid solutions celebrated",
                "Identity connection: 'How does this connect to who you are?'",
                "Community impact measured, not just technical correctness"
            ],
            "duration_minutes": 25
        }
    
    def _generate_identity_reflection(self, template: Dict, target_profiles: List[str]) -> Dict[str, Any]:
        prompts = [
            "What thinking style helped you most today? (visual, verbal, hands-on, pattern, story)",
            "When did you feel most 'in your element'? What were you doing?",
            "What unique perspective did you bring to your team?",
            "How does this connect to who you want to become?"
        ]
        
        # Add profile-specific prompts
        profile_prompts = {
            "autistic": "What pattern or system did you understand deeply today?",
            "adhd": "What novel connection or rapid iteration worked for you?",
            "dyslexic": "What big picture or spatial insight did you discover?",
            "dyspraxic": "What strategic insight or empathetic connection did you make?"
        }
        
        for p in target_profiles:
            if p in profile_prompts:
                prompts.append(profile_prompts[p])
        
        return {
            "name": "Identity Reflection",
            "content": "Reflect on your STEM identity and cognitive strengths",
            "prompts": prompts,
            "neuroaffirming_notes": [
                "No 'right' answers — your perspective is the data",
                "Identity bonus (+5% mastery) for documenting STEM-self connection",
                "Struggle normalized: document strategies, not just successes"
            ],
            "duration_minutes": 10
        }
    
    def _generate_collaboration_structure(self, target_profiles: List[str], grade: str) -> Dict[str, Any]:
        # Determine optimal collaboration structure based on profiles
        structures = {
            "autistic": "Parallel deep work with structured check-ins",
            "adhd": "Burst collaboration with async check-ins",
            "dyslexic": "Visual-verbal collaboration with big-picture framing",
            "dyspraxic": "Verbal-strategic collaboration with empathy focus"
        }
        
        primary = target_profiles[0] if target_profiles else "general"
        primary_structure = structures.get(primary, "Flexible collaborative groups")
        
        return {
            "name": "Collaboration Structure",
            "content": f"Primary structure: {primary_structure}. Flexible grouping with role rotation.",
            "roles": [
                {"name": "Pattern Seeker", "description": "Finds patterns and connections", "profiles": ["autistic"]},
                {"name": "Idea Generator", "description": "Generates novel ideas rapidly", "profiles": ["adhd"]},
                {"name": "Big Picture Weaver", "description": "Connects concepts to big picture", "profiles": ["dyslexic"]},
                {"name": "Strategy Weaver", "description": "Plans strategy and ensures empathy", "profiles": ["dyspraxic"]}
            ],
            "neuroaffirming_notes": [
                "Roles are lenses, not labels — learners rotate",
                "Each role leverages cognitive strengths",
                "No role is 'better' — all essential for complete solutions"
            ],
            "duration_minutes": "Throughout"
        }
    
    def _generate_family_connection(self, template: Dict, context: Dict) -> Dict[str, Any]:
        community = context.get("community", "your community")
        return {
            "name": "Family Connection",
            "content": f"Together, find one {template['topic']} in {context.get('place', community)}. Draw it together. Talk about: What problem does it solve?",
            "multilingual": {
                "en": template.get("family_challenge", "Find one example in your home..."),
                "es": f"Juntos, encuentren un {template['topic']} en su hogar. Dibújenlo juntos. ¿Qué problema resuelve?"
            },
            "accessibility_notes": [
                "Zero-cost materials (household items only)",
                "Offline option: paper version sent home",
                "Audio option: WhatsApp voice note with challenge",
                "Visual supports included"
            ]
        }
    
    def _generate_assessment_rubric(self, target_profiles: List[str]) -> Dict[str, Any]:
        return {
            "mastery_levels": {
                "Exploring": "Follows model, participates with guidance, minimal struggle journal",
                "Developing": "Adapts model, documents 1 strategy, explains reasoning",
                "Mastering": "Creates original, mentors peers, 2+ strategies, identity connection"
            },
            "domains": {
                "Conceptual Understanding": 0.30,
                "Problem Framing": 0.20,
                "Design Process": 0.25,
                "Collaboration": 0.15,
                "Identity Reflection": 0.10
            },
            "identity_bonus": {
                "criteria": [
                    "STEM self-connection documented",
                    "Future self named",
                    "Struggle as growth documented",
                    "Community impact named"
                ],
                "bonus": "5% mastery boost when all 4 criteria met"
            },
            "neuroaffirming_criteria": {
                "strengths_leveraged": "Evidence of leveraging cognitive strengths",
                "struggle_documented": "Struggle journal with 2+ strategies per challenge",
                "identity_connection": "Explicit STEM-self connection",
                "community_impact": "Authentic community problem addressed"
            }
        }
    
    def _generate_materials(self, template: Dict, grade: str) -> List[Dict[str, Any]]:
        base = template.get("materials", [])
        grade_additions = {
            "K-2": ["large manipulatives", "picture guides"],
            "3-5": ["measurement tools", "recording sheets"],
            "6-8": ["digital sensors", "data analysis tools"],
            "9-12": ["microcontrollers", "fabrication tools"]
        }
        materials = [{"item": m, "cost": 0, "alternatives": ["household items"]} for m in base]
        for m in grade_additions.get(grade, []):
            materials.append({"item": m, "cost": 0, "alternatives": ["household items"]})
        return materials
    
    def _generate_accessibility_plan(self, target_profiles: List[str]) -> Dict[str, Any]:
        plan = {
            "visual": ["High contrast", "Large text option", "Alt text for all images", "Color-blind safe palette"],
            "auditory": ["Captions for video", "Transcripts for audio", "No auto-play audio"],
            "motor": ["Keyboard navigation", "No drag-and-drop required", "Large click targets"],
            "cognitive": ["Plain language", "Chunked instructions", "Visual sequence cards", "Progress indicators"],
            "language": ["EN/ES minimum", "Key terms glossary", "Bilingual instructions"]
        }
        
        # Profile-specific additions
        if "autistic" in target_profiles:
            plan["autistic_specific"] = [
                "Predictable structure with visual schedule",
                "Sensory break options",
                "Clear transition warnings",
                "Literal language option"
            ]
        if "adhd" in target_profiles:
            plan["adhd_specific"] = [
                "Movement breaks built in",
                "Chunked tasks with timers",
                "Interest-based entry points",
                "Fidget-friendly design"
            ]
        if "dyslexic" in target_profiles:
            plan["dyslexic_specific"] = [
                "Audio alternatives for all text",
                "Visual mapping tools",
                "Speech-to-text option",
                "Dyslexia-friendly fonts"
            ]
        if "dyspraxic" in target_profiles:
            plan["dyspraxic_specific"] = [
                "Alternative output modes (voice, video, diagram)",
                "Extended time defaults",
                "Ergonomic tool options",
                "Motor-free assessment options"
            ]
        
        return plan
    
    def _generate_neuroaffirming_adaptations(self, target_profiles: List[str]) -> Dict[str, Any]:
        """Generate profile-specific adaptations."""
        adaptations = {}
        
        profile_adaptations = {
            "autistic": {
                "engagement": ["Interest-based entry points", "Predictable routine", "Choice within structure"],
                "representation": ["Visual supports", "Explicit step-by-step", "Pattern highlighting"],
                "action_expression": ["Multiple modalities", "Pattern-based expression", "System modeling"],
                "identity_affirmation": "Your pattern-seeking mind is a STEM superpower"
            },
            "adhd": {
                "engagement": ["Novelty injection", "Movement integration", "Interest-based switching"],
                "representation": ["Chunked info", "Multimodal", "Interactive elements"],
                "action_expression": ["Rapid prototyping", "Movement-based", "Verbal + visual"],
                "identity_affirmation": "Your rapid-idea brain is an innovation engine"
            },
            "dyslexic": {
                "engagement": ["Big picture first", "Strength-based entry", "Spatial entry points"],
                "representation": ["Audio + visual", "Concept maps", "Narrative framing"],
                "action_expression": ["Verbal explanation", "Visual models", "Story-based"],
                "identity_affirmation": "Your big-picture mind sees connections others miss"
            },
            "dyspraxic": {
                "engagement": ["Strategic entry", "Empathy-led", "Verbal reasoning first"],
                "representation": ["Verbal + visual", "Conceptual over motor", "Strategic framing"],
                "action_expression": ["Voice dictation", "Strategic planning", "Verbal reasoning"],
                "identity_affirmation": "Your empathy and strategy make better human-centered STEM"
            }
        }
        
        for profile in target_profiles:
            if profile in profile_adaptations:
                adaptations[profile] = profile_adaptations[profile]
        
        return adaptations
    
    def _generate_identity_bonus_criteria(self, target_profiles: List[str]) -> Dict[str, Any]:
        return {
            "criteria": [
                {"id": "stem_self_connection", "description": "Documents 'I am a STEM person because...'", "weight": 0.25},
                {"id": "future_self_named", "description": "Names future STEM self: 'I see myself as...'", "weight": 0.25},
                {"id": "struggle_as_growth", "description": "Documents struggle strategies as growth", "weight": 0.25},
                {"id": "community_impact_named", "description": "Names specific community impact", "weight": 0.25}
            ],
            "bonus": "5% mastery boost when all 4 criteria met",
            "neuroaffirming_note": "Identity bonus is not extra credit — it's soul alignment. Your cognitive profile IS your STEM asset."
        }
    
    def generate_multiple(self, topics: List[str], grade: str, 
                         target_profiles: List[str] = None) -> List['NeuroaffirmingLesson']:
        """Generate multiple lessons for a unit."""
        return [self.generate(topic, grade, target_profiles) for topic in topics]
    
    def generate_unit(self, unit_topic: str, grade: str, 
                     target_profiles: List[str] = None,
                     num_lessons: int = 5) -> Dict[str, Any]:
        """Generate a full unit with multiple lessons."""
        # For now, generate same lesson multiple times with variations
        # In production, would sequence lessons
        lessons = []
        for i in range(num_lessons):
            lesson = self.generate(unit_topic, grade, target_profiles)
            lesson.id = f"{lesson.id}-lesson-{i+1}"
            lessons.append(lesson)
        
        return {
            "unit_id": f"{unit_topic}-{grade}-unit",
            "topic": unit_topic,
            "grade": grade,
            "lessons": lessons,
            "total_duration_minutes": sum(self.GRADE_BANDS[grade]["duration"] for _ in range(num_lessons)),
            "profile_focus": target_profiles or ["autistic", "adhd", "dyslexic", "dyspraxic"]
        }

if __name__ == "__main__":
    import uuid
    generator = NeuroaffirmingLessonGenerator()
    
    # Generate a sample lesson
    lesson = generator.generate(
        topic="patterns",
        grade="6-8",
        target_profiles=["autistic", "adhd", "dyslexic", "dyspraxic"],
        context={"community": "your neighborhood", "place": "your city"}
    )
    
    print(f"Generated: {lesson.title}")
    print(f"ID: {lesson.id}")
    print(f"Topic: {lesson.topic}")
    print(f"Grade: {lesson.grade_band}")
    print(f"Profiles: {lesson.cognitive_profile_focus}")
    print(f"Driving Question: {lesson.driving_question}")
    print(f"\nLearning Targets:")
    for t in lesson.learning_targets:
        print(f"  - {t}")
    print(f"\nNeuroaffirming Adaptations:")
    for profile, adaptations in lesson.neuroaffirming_adaptations.items():
        print(f"  {profile}: {adaptations['identity_affirmation']}")