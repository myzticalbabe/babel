#!/usr/bin/env python3
"""
Neurodiversity-Affirming STEM Engine — Core Module

Soul Forge License v1.0 — Tend the fire.

Cognitive diversity as creative asset, not deficit.
Maps neurodivergent profiles to STEM creative contributions.

Research:
- Armstrong (2010) - Neurodiversity as competitive advantage
- Silberman (2015) - Neurotribes: autism as different operating system
- Singer (2017) - Neurodiversity paradigm shift
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
from pathlib import Path
import json

class CognitiveProfile(Enum):
    AUTISTIC = "autistic"
    ADHD = "adhd"
    DYSLEXIC = "dyslexic"
    DYSPRAXIC = "dyspraxic"
    TOURETTE = "tourette"
    OCD = "ocd"
    GIFTED = "gifted"
    CUSTOM = "custom"

@dataclass
class CognitiveStrength:
    name: str
    description: str
    stem_applications: List[str]
    creative_contributions: List[str]

@dataclass
class CognitiveSupport:
    name: str
    description: str
    implementation: str

@dataclass
class CreativeContribution:
    domain: str
    description: str
    evidence: str

@dataclass
class CognitiveProfileSpec:
    profile: CognitiveProfile
    name: str
    strengths: List[CognitiveStrength]
    supports: List[CognitiveSupport]
    creative_contributions: List[CreativeContribution]
    design_parameters: Dict[str, Any]
    collaboration_style: str
    communication_preferences: List[str]

class CognitiveProfileRegistry:
    """
    Registry of neurodivergent cognitive profiles with STEM creative mappings.
    
    Research:
    - Armstrong (2010) - Neurodiversity as competitive advantage
    - Silberman (2015) - Neurotribes: autism as different operating system
    - Singer (2017) - Neurodiversity paradigm shift
    - Grandin (2006) - Thinking in Pictures
    """
    
    CORE_PROFILES = {
        CognitiveProfile.AUTISTIC: {
            "name": "Autistic",
            "strengths": [
                CognitiveStrength(
                    name="Pattern Recognition",
                    description="Exceptional ability to detect patterns in complex data",
                    stem_applications=["Data analysis", "Algorithm optimization", "Anomaly detection"],
                    creative_contributions=["Pattern discovery", "Anomaly detection", "System optimization"]
                ),
                CognitiveStrength(
                    name="Deep Focus",
                    description="Sustained attention on topics of interest for extended periods",
                    stem_applications=["Deep research", "Complex debugging", "Mathematical proofs"],
                    creative_contributions=["Breakthrough insights", "Persistent problem-solving"]
                ),
                CognitiveStrength(
                    name="Systems Thinking",
                    description="Natural ability to understand complex interconnected systems",
                    stem_applications=["Systems engineering", "Ecology modeling", "Network analysis"],
                    creative_contributions=["Holistic system design", "Emergent behavior prediction"]
                ),
                CognitiveStrength(
                    name="Detail Precision",
                    description="Exceptional attention to detail and precision",
                    stem_applications=["Quality assurance", "Precision engineering", "Data validation"],
                    creative_contributions=["Zero-defect designs", "Micro-optimization"]
                )
            ],
            "supports": [
                CognitiveSupport(
                    name="Predictable Structure",
                    description="Clear routines, visual schedules, explicit expectations",
                    implementation="Visual schedules, consistent routines, advance notice of changes"
                ),
                CognitiveSupport(
                    name="Sensory Regulation",
                    description="Environmental modifications for sensory processing differences",
                    implementation="Noise-canceling headphones, adjustable lighting, fidget tools, quiet spaces"
                ),
                CognitiveSupport(
                    name="Clear Explicit Instructions",
                    description="Unambiguous, step-by-step instructions with visual supports",
                    implementation="Written + visual instructions, chunked tasks, checklists"
                ),
                CognitiveSupport(
                    name="Interest-Based Learning",
                    description="Leverage special interests as learning bridges",
                    implementation="Connect STEM concepts to special interests, project-based learning"
                )
            ],
            "creative_contributions": [
                CreativeContribution("Pattern Discovery", "Identifying novel patterns in complex datasets", "Grandin (2006) - visual thinking in engineering"),
                CreativeContribution("Anomaly Detection", "Spotting outliers and edge cases others miss", "Software testing, quality assurance"),
                CreativeContribution("System Optimization", "Finding elegant solutions in complex systems", "Algorithm optimization, resource allocation"),
                CreativeContribution("Zero-Defect Design", "Precision engineering with zero-defect mindset", "Aerospace, medical devices")
            ],
            "design_parameters": {
                "predictability": 0.9,
                "sensory_load": 0.3,
                "social_demand": 0.2,
                "novelty_tolerance": 0.3,
                "structure_need": 0.9
            },
            "collaboration_style": "Parallel deep work with structured check-ins",
            "communication_preferences": ["written", "visual", "direct", "literal"]
        },
        
        CognitiveProfile.ADHD: {
            "name": "ADHD",
            "strengths": [
                CognitiveStrength(
                    name="Divergent Thinking",
                    description="Generates multiple novel ideas and connections rapidly",
                    stem_applications=["Brainstorming", "Hypothesis generation", "Design ideation"],
                    creative_contributions=["Novel connections", "Cross-domain synthesis"]
                ),
                CognitiveStrength(
                    name="Hyperfocus",
                    description="Intense sustained attention on high-interest tasks",
                    stem_applications=["Deep coding sessions", "Complex problem solving", "Rapid prototyping"],
                    creative_contributions=["Breakthrough sprints", "Rapid iteration cycles"]
                ),
                CognitiveStrength(
                    name="Novelty Seeking",
                    description="Natural drive to explore new approaches and ideas",
                    stem_applications=["Innovation labs", "R&D", "Experimental design"],
                    creative_contributions=["Boundary pushing", "Novel methodology"]
                ),
                CognitiveStrength(
                    name="Rapid Iteration",
                    description="Fast cycle of try-fail-learn-adapt",
                    stem_applications=["Agile development", "Design thinking", "Experimental science"],
                    creative_contributions=["Rapid prototyping", "Fail-fast learning"]
                )
            ],
            "supports": [
                CognitiveSupport(
                    name="Movement Integration",
                    description="Physical movement integrated into cognitive work",
                    implementation="Standing desks, movement breaks, walking meetings, fidget tools"
                ),
                CognitiveSupport(
                    name="Novelty Injection",
                    description="Regular introduction of novel elements to maintain engagement",
                    implementation="Rotating tasks, gamification, new challenges, variety"
                ),
                CognitiveSupport(
                    name="External Scaffolding",
                    description="External systems for executive function support",
                    implementation="Digital planners, timers, accountability partners, body doubling"
                ),
                CognitiveSupport(
                    name="Interest-Based Switching",
                    description="Strategic task switching aligned with interest cycles",
                    implementation="Task batching by interest, strategic procrastination"
                )
            ],
            "creative_contributions": [
                CreativeContribution("Novel Connections", "Connecting seemingly unrelated domains", "Cross-disciplinary innovation"),
                CreativeContribution("Rapid Prototyping", "Fast iteration from concept to working model", "MVP development, hackathons"),
                CreativeContribution("Boundary Pushing", "Challenging assumptions and constraints", "Innovation leadership"),
                CreativeContribution("Crisis Creativity", "Creative problem-solving under pressure", "Emergency engineering, hackathons")
            ],
            "design_parameters": {
                "predictability": 0.4,
                "sensory_load": 0.6,
                "social_demand": 0.5,
                "novelty_tolerance": 0.9,
                "structure_need": 0.4
            },
            "collaboration_style": "Burst collaboration with async check-ins",
            "communication_preferences": ["verbal", "visual", "dynamic", "metaphorical"]
        },
        
        CognitiveProfile.DYSLEXIC: {
            "name": "Dyslexic",
            "strengths": [
                CognitiveStrength(
                    name="Holistic Thinking",
                    description="Sees the big picture and connections before details",
                    stem_applications=["Systems architecture", "Strategic planning", "Conceptual design"],
                    creative_contributions=["Big picture synthesis", "Cross-domain integration"]
                ),
                CognitiveStrength(
                    name="Spatial Reasoning",
                    description="Exceptional 3D visualization and mental rotation",
                    stem_applications=["CAD/3D modeling", "Molecular visualization", "Spatial data science"],
                    creative_contributions=["Spatial design", "Systems visualization"]
                ),
                CognitiveStrength(
                    name="Narrative Reasoning",
                    description="Thinks in stories and scenarios rather than abstract symbols",
                    stem_applications=["User experience design", "Science communication", "Scenario planning"],
                    creative_contributions=["Story systems", "Scenario planning", "User journey design"]
                ),
                CognitiveStrength(
                    name="Big Picture Synthesis",
                    description="Integrates disparate information into coherent wholes",
                    stem_applications=["Systems integration", "Interdisciplinary research", "Strategy"],
                    creative_contributions=["Cross-domain integration", "Pattern synthesis"]
                )
            ],
            "supports": [
                CognitiveSupport(
                    name="Multimodal Input",
                    description="Multiple input modalities beyond text",
                    implementation="Audio input, speech-to-text, visual diagrams, voice notes"
                ),
                CognitiveSupport(
                    name="Audio Alternatives",
                    description="Text-to-speech and audio-first content delivery",
                    implementation="Screen readers, audiobooks, podcast-format content"
                ),
                CognitiveSupport(
                    name="Visual Mapping",
                    description="Visual organization tools over linear text",
                    implementation="Mind maps, concept maps, flowcharts, visual outlines"
                ),
                CognitiveSupport(
                    name="Strength-Based Assessment",
                    description="Assess understanding through strengths, not text decoding",
                    implementation="Oral presentations, visual projects, verbal explanations"
                )
            ],
            "creative_contributions": [
                CreativeContribution("Spatial Design", "3D/4D spatial design and visualization", "Architecture, molecular modeling, VR"),
                CreativeContribution("Systems Visualization", "Making complex systems visible and navigable", "Data viz, network mapping"),
                CreativeContribution("Story Systems", "Systems thinking through narrative structures", "UX design, science communication"),
                CreativeContribution("Cross-Domain Integration", "Connecting disparate domains into coherent wholes", "Interdisciplinary research")
            ],
            "design_parameters": {
                "predictability": 0.6,
                "sensory_load": 0.4,
                "social_demand": 0.5,
                "novelty_tolerance": 0.7,
                "structure_need": 0.5
            },
            "collaboration_style": "Visual-verbal collaboration with big-picture framing",
            "communication_preferences": ["visual", "verbal", "metaphorical", "story-based"]
        },
        
        CognitiveProfile.DYSPRAXIC: {
            "name": "Dyspraxic",
            "strengths": [
                CognitiveStrength(
                    name="Empathetic Communication",
                    description="Heightened sensitivity to others' experiences and perspectives",
                    stem_applications=["User research", "Participatory design", "Science communication"],
                    creative_contributions=["Empathetic design", "Inclusive design"]
                ),
                CognitiveStrength(
                    name="Verbal Reasoning",
                    description="Strong verbal reasoning and articulation",
                    stem_applications=["Technical writing", "Science communication", "Grant writing"],
                    creative_contributions=["Communication systems", "Science storytelling"]
                ),
                CognitiveStrength(
                    name="Strategic Thinking",
                    description="Big-picture strategic thinking with long-term vision",
                    stem_applications=["Research strategy", "Project planning", "Systems design"],
                    creative_contributions=["Strategic frameworks", "Long-term planning"]
                )
            ],
            "supports": [
                CognitiveSupport(
                    name="Motor Scaffolds",
                    description="Tools and adaptations for fine/gross motor challenges",
                    implementation="Ergonomic tools, voice control, adaptive keyboards, gesture recognition"
                ),
                CognitiveSupport(
                    name="Alternative Output",
                    description="Multiple ways to demonstrate understanding",
                    implementation="Voice dictation, video recording, diagrams, oral exams"
                ),
                CognitiveSupport(
                    name="Time Flexibility",
                    description="Extended time for motor-intensive tasks",
                    implementation="Extended deadlines, alternative formats, process over product"
                )
            ],
            "creative_contributions": [
                CreativeContribution("Empathetic Design", "Design centered on human experience", "Accessibility, UX, healthcare"),
                CreativeContribution("Communication Systems", "Systems for clear, inclusive communication", "Science comm, technical writing"),
                CreativeContribution("Strategic Frameworks", "Long-term strategic thinking frameworks", "Research strategy, policy")
            ],
            "design_parameters": {
                "predictability": 0.7,
                "sensory_load": 0.3,
                "social_demand": 0.6,
                "novelty_tolerance": 0.6,
                "structure_need": 0.7
            },
            "collaboration_style": "Verbal-strategic collaboration with empathy focus",
            "communication_preferences": ["verbal", "conceptual", "empathetic", "structured"]
        }
    }
    
    EXTENSIBLE_PROFILES = {
        CognitiveProfile.TOURETTE: {
            "name": "Tourette Syndrome",
            "strengths": ["Hyperfocus during tics suppression", "Creative vocalization", "Pattern interruption"],
            "supports": ["Tic accommodation", "Movement breaks", "Stress reduction"]
        },
        CognitiveProfile.OCD: {
            "name": "OCD",
            "strengths": ["Exceptional error detection", "Rigorous quality control", "Systematic thoroughness"],
            "supports": ["Perfectionism management", "Uncertainty tolerance training"]
        },
        CognitiveProfile.GIFTED: {
            "name": "Gifted/2e",
            "strengths": ["Rapid learning", "Abstract reasoning", "Cross-domain synthesis"],
            "supports": ["Intellectual peer groups", "Acceleration", "Depth over breadth"]
        }
    }
    
    def __init__(self):
        self.profiles = {}
        self._load_core_profiles()
        self._load_extensible_profiles()
    
    def _load_core_profiles(self):
        for profile_enum, data in self.CORE_PROFILES.items():
            self.profiles[profile_enum] = CognitiveProfileSpec(
                profile=profile_enum,
                name=data["name"],
                strengths=data["strengths"],
                supports=data["supports"],
                creative_contributions=data["creative_contributions"],
                design_parameters=data["design_parameters"],
                collaboration_style=data["collaboration_style"],
                communication_preferences=data["communication_preferences"]
            )
    
    def _load_extensible_profiles(self):
        for profile_enum, data in self.EXTENSIBLE_PROFILES.items():
            # Create minimal profile for extensible ones
            self.profiles[profile_enum] = CognitiveProfileSpec(
                profile=profile_enum,
                name=data["name"],
                strengths=[CognitiveStrength(s["name"], s["description"], [], []) for s in data["strengths"]],
                supports=[CognitiveSupport(s["name"], s["description"], s["implementation"]) for s in data["supports"]],
                creative_contributions=[CreativeContribution("general", c, "") for c in data["creative_contributions"]],
                design_parameters={},
                collaboration_style="TBD",
                communication_preferences=[]
            )
    
    def get_profile(self, profile: CognitiveProfile) -> Optional[CognitiveProfileSpec]:
        return self.profiles.get(profile)
    
    def get_all_profiles(self) -> Dict[CognitiveProfile, CognitiveProfileSpec]:
        return self.profiles.copy()
    
    def register_custom_profile(self, profile: CognitiveProfileSpec):
        """Register a community-contributed profile."""
        self.profiles[profile.profile] = profile
    
    def get_profiles_by_strength(self, strength_name: str) -> List[CognitiveProfileSpec]:
        """Find profiles with a specific strength."""
        results = []
        for profile in self.profiles.values():
            if any(s.name.lower() == strength_name.lower() for s in profile.strengths):
                results.append(profile)
        return results
    
    def get_profiles_by_design_parameter(self, param: str, min_value: float) -> List[CognitiveProfileSpec]:
        """Find profiles with design parameter above threshold."""
        results = []
        for profile in self.profiles.values():
            if profile.design_parameters.get(param, 0) >= min_value:
                results.append(profile)
        return results

class CognitiveProfileEngine:
    """
    Maps learners to cognitive profiles and infers design parameters.
    """
    
    def __init__(self):
        self.registry = CognitiveProfileRegistry()
    
    def infer_profile(self, learner_data: Dict[str, Any]) -> List[tuple[CognitiveProfile, float]]:
        """
        Infer cognitive profile from learner data.
        Returns list of (profile, confidence) tuples.
        """
        # In practice, would use assessment data, self-report, observation
        # This is a simplified inference based on self-report
        profile_scores = {}
        
        # Simple keyword-based inference (would be ML model in production)
        keywords = {
            CognitiveProfile.AUTISTIC: ["pattern", "detail", "focus", "system", "routine", "sensory"],
            CognitiveProfile.ADHD: ["energy", "ideas", "focus", "novelty", "movement", "hyperfocus"],
            CognitiveProfile.DYSLEXIC: ["visual", "spatial", "big picture", "story", "holistic"],
            CognitiveProfile.DYSPRAXIC: ["empathy", "verbal", "strategy", "motor", "coordination"]
        }
        
        learner_text = " ".join([
            learner_data.get("self_description", ""),
            learner_data.get("interests", ""),
            learner_data.get("challenges", ""),
            learner_data.get("strengths", "")
        ]).lower()
        
        for profile, keywords_list in keywords.items():
            score = sum(1 for kw in keywords_list if kw in learner_text)
            if score > 0:
                profile_scores[profile] = score / len(keywords_list)
        
        # Normalize
        total = sum(profile_scores.values())
        if total > 0:
            return [(p, s/total) for p, s in sorted(profile_scores.items(), key=lambda x: -x[1])]
        return [(CognitiveProfile.AUTISTIC, 0.25), (CognitiveProfile.ADHD, 0.25), 
                (CognitiveProfile.DYSLEXIC, 0.25), (CognitiveProfile.DYSPRAXIC, 0.25)]
    
    def get_design_parameters(self, profile: CognitiveProfile) -> Dict[str, float]:
        """Get design parameters for a profile."""
        spec = self.registry.get_profile(profile)
        if spec:
            return spec.design_parameters
        return {}
    
    def get_collaboration_style(self, profile: CognitiveProfile) -> str:
        spec = self.registry.get_profile(profile)
        return spec.collaboration_style if spec else "Collaborative"
    
    def get_communication_preferences(self, profile: CognitiveProfile) -> List[str]:
        spec = self.registry.get_profile(profile)
        return spec.communication_preferences if spec else ["verbal", "visual"]

# Plugin system for community-contributed profiles
class ProfilePluginSystem:
    """Plugin system for community-contributed cognitive profiles."""
    
    def __init__(self, registry: CognitiveProfileRegistry):
        self.registry = registry
        self.plugins_dir = Path("profiles/plugins")
        self.plugins_dir.mkdir(parents=True, exist_ok=True)
    
    def load_plugin(self, plugin_path: Path) -> bool:
        """Load a profile plugin from JSON/YAML file."""
        try:
            if plugin_path.suffix == '.json':
                with open(plugin_path) as f:
                    data = json.load(f)
            elif plugin_path.suffix in ['.yaml', '.yml']:
                import yaml
                with open(plugin_path) as f:
                    data = yaml.safe_load(f)
            else:
                return False
            
            # Validate and register
            # ... validation logic
            return True
        except Exception as e:
            print(f"Failed to load plugin {plugin_path}: {e}")
            return False
    
    def discover_plugins(self) -> List[Path]:
        """Discover all profile plugins."""
        return list(self.plugins_dir.glob("*.json")) + list(self.plugins_dir.glob("*.yaml"))

if __name__ == "__main__":
    # Demo
    registry = CognitiveProfileRegistry()
    engine = CognitiveProfileEngine()
    
    # Show all profiles
    for profile_enum, spec in registry.get_all_profiles().items():
        print(f"\n{spec.name} ({profile_enum.value})")
        print(f"  Strengths: {[s.name for s in spec.strengths]}")
        print(f"  Creative: {[c.domain for c in spec.creative_contributions]}")
        print(f"  Design params: {spec.design_parameters}")
        print(f"  Collaboration: {spec.collaboration_style}")
    
    # Test inference
    learner = {
        "self_description": "I love finding patterns in data and can focus for hours on coding",
        "interests": "Data analysis, algorithms, system optimization",
        "strengths": "Pattern recognition, deep focus, detail oriented",
        "challenges": "Social situations, sensory overload"
    }
    
    inferred = engine.infer_profile(learner)
    print(f"\nInferred profiles for learner:")
    for profile, confidence in inferred:
        print(f"  {profile.value}: {confidence:.2%}")