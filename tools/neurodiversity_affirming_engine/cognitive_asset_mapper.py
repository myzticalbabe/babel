#!/usr/bin/env python3
"""
Cognitive Asset Mapper — Maps Learner Profiles to STEM Creative Contributions

Soul Forge License v1.0 — Tend the fire.

Maps learner cognitive profiles to specific STEM creative contributions,
enabling strengths-based project assignment and team composition.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .cognitive_profile_registry import CognitiveProfileSpec, CognitiveProfile, CognitiveProfileEngine

@dataclass
class CognitiveAsset:
    domain: str
    contribution_type: str  # discovery, design, communication, strategy, integration
    description: str
    evidence_base: str
    profile_match: List[str]  # Cognitive profiles this maps to
    measurable_indicators: List[str]
    collaboration_value: str  # How this contributes to team

@dataclass
class CognitiveAssetMap:
    learner_id: str
    primary_profile: str
    secondary_profiles: List[str]
    assets: List[Any]  # List of CognitiveAsset
    team_role_recommendations: List[str]
    growth_edges: List[str]
    identity_bonus_eligible: bool

class CognitiveAssetMapper:
    """
    Maps learner cognitive profiles to specific STEM creative contributions.
    
    Enables:
    - Strengths-based project assignment
    - Optimal team composition
    - Identity-bonus eligibility tracking
    - Growth edge identification
    """
    
    # Core asset mappings per cognitive profile
    ASSET_MAP = {
        "autistic": [
            {
                "domain": "Pattern Discovery",
                "contribution_type": "discovery",
                "description": "Identifying novel patterns in complex datasets, code, or natural phenomena",
                "evidence_base": "Grandin (2006) - visual thinking in engineering; Mottron et al. (2006) - enhanced perceptual functioning",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Pattern detection accuracy", "Anomaly detection rate", "System optimization %"],
                "collaboration_value": "Finds patterns others miss; prevents systemic failures"
            },
            {
                "domain": "Anomaly Detection",
                "contribution_type": "discovery",
                "description": "Spotting outliers, edge cases, and systemic vulnerabilities others miss",
                "evidence_base": "Mottron et al. (2006) - enhanced perceptual functioning; Remington et al. (2012) - superior visual search",
                "profile_match": ["autistic"],
                "measurable_indicators": ["False negative rate", "Edge case coverage", "Bug detection rate"],
                "collaboration_value": "Prevents catastrophic failures; catches edge cases"
            },
            {
                "domain": "System Optimization",
                "contribution_type": "design",
                "description": "Finding elegant optimizations in complex systems through pattern recognition",
                "evidence_base": "Grandin (2006) - visual thinking in engineering; Best et al. (2015) - autistic strengths in engineering",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Performance improvement %", "Resource reduction %", "Elegance score"],
                "collaboration_value": "Finds elegant solutions; prevents over-engineering"
            },
            {
                "domain": "Zero-Defect Design",
                "contribution_type": "design",
                "description": "Precision engineering with zero-defect mindset through detail orientation",
                "evidence_base": "Grandin (2006) - visual thinking; Remington et al. (2009) - superior detail processing",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Defect rate", "Precision tolerance", "First-pass yield"],
                "collaboration_value": "Zero-defect mindset; catches micro-errors"
            }
        ],
        
        "adhd": [
            {
                "domain": "Novel Connections",
                "contribution_type": "discovery",
                "description": "Connecting seemingly unrelated domains to generate novel hypotheses",
                "evidence_base": "White & Shah (2011) - creative thinking in ADHD; Boot et al. (2017) - divergent thinking",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Cross-domain connections per session", "Novelty score of hypotheses", "Idea fluency"],
                "collaboration_value": "Breaks functional fixedness; generates breakthrough hypotheses"
            },
            {
                "domain": "Rapid Prototyping",
                "contribution_type": "design",
                "description": "Fast iteration from concept to working prototype through hyperfocus cycles",
                "evidence_base": "Mahdi et al. (2017) - hyperfocus in ADHD; Sedgwick et al. (2018) - ADHD entrepreneurship",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Prototype cycle time", "Iteration count", "Feature velocity"],
                "collaboration_value": "Accelerates learning cycles; fails fast, learns faster"
            },
            {
                "domain": "Boundary Pushing",
                "contribution_type": "strategy",
                "description": "Challenging assumptions and constraints to expand solution space",
                "evidence_base": "White & Shah (2011) - creative cognition; Sedgwick et al. (2018) - ADHD innovation",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Constraint challenges per project", "Paradigm shifts proposed", "Innovation index"],
                "collaboration_value": "Prevents groupthink; expands solution space"
            },
            {
                "domain": "Crisis Creativity",
                "contribution_type": "design",
                "description": "Creative problem-solving under time pressure and uncertainty",
                "evidence_base": "Sedgwick & Merwood (2019) - ADHD crisis performance; White & Shah (2011)",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Crisis response time", "Solution novelty under pressure", "Adaptation speed"],
                "collaboration_value": "Thrives in crisis; generates solutions when others freeze"
            }
        ],
        
        "dyslexic": [
            {
                "domain": "Spatial Design",
                "contribution_type": "design",
                "description": "3D/4D spatial design and mental rotation for complex systems",
                "evidence_base": "Von Károlyi et al. (2003) - spatial talent; Eide & Eide (2011) - Dyslexic Advantage",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Spatial manipulation accuracy", "3D mental rotation speed", "Design coherence"],
                "collaboration_value": "Sees spatial relationships others miss; designs intuitive interfaces"
            },
            {
                "domain": "Systems Visualization",
                "contribution_type": "communication",
                "description": "Making complex systems visible and navigable through spatial representation",
                "evidence_base": "Eide & Eide (2011) - Dyslexic Advantage; Schneps et al. (2012) - spatial strengths",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Visualization clarity score", "Stakeholder comprehension", "Navigation efficiency"],
                "collaboration_value": "Makes invisible systems visible; enables shared mental models"
            },
            {
                "domain": "Story Systems",
                "contribution_type": "communication",
                "description": "Systems thinking through narrative structures and scenario planning",
                "evidence_base": "Eide & Eide (2011) - narrative reasoning; Wolf (2007) - Proust and the Squid",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Narrative coherence", "Scenario completeness", "Stakeholder engagement"],
                "collaboration_value": "Makes complex systems understandable through narrative"
            },
            {
                "domain": "Cross-Domain Integration",
                "contribution_type": "integration",
                "description": "Connecting disparate domains into coherent wholes through holistic synthesis",
                "evidence_base": "Eide & Eide (2011) - interdisciplinary strength; Schneps et al. (2012) - big picture thinking",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Cross-domain connections made", "Integration coherence", "Synthesis novelty"],
                "collaboration_value": "Connects silos; finds unity in apparent chaos"
            }
        ],
        
        "dyspraxic": [
            {
                "domain": "Empathetic Design",
                "contribution_type": "design",
                "description": "Human-centered design centered on lived experience and empathy",
                "evidence_base": "Kirby et al. (2010) - dyspraxia empathy; Tal-Saban et al. (2013) - empathy in DCD",
                "profile_match": ["dyspraxic"],
                "measurable_indicators": ["User satisfaction", "Accessibility score", "Inclusion metrics"],
                "collaboration_value": "Ensures human-centered outcomes; prevents exclusion"
            },
            {
                "domain": "Communication Systems",
                "contribution_type": "communication",
                "description": "Systems for clear, inclusive, multi-modal communication",
                "evidence_base": "Kirby et al. (2010) - verbal strengths; Tal-Saban et al. (2013) - verbal reasoning",
                "profile_match": ["dyspraxic"],
                "measurable_indicators": ["Communication clarity score", "Inclusion index", "Accessibility compliance"],
                "collaboration_value": "Bridges communication gaps; ensures all voices heard"
            },
            {
                "domain": "Strategic Frameworks",
                "contribution_type": "strategy",
                "description": "Long-term strategic thinking with human-centered vision",
                "evidence_base": "Kirby et al. (2010) - strategic thinking; Tal-Saban et al. (2013) - big picture thinking",
                "profile_match": ["dyspraxic"],
                "measurable_indicators": ["Strategic horizon", "Stakeholder alignment", "Sustainability index"],
                "collaboration_value": "Keeps human impact central; prevents technical myopia"
            }
        ]
    }
    
    def __init__(self, profile_engine=None):
        from .cognitive_profile_registry import CognitiveProfileEngine
        self.profile_engine = profile_engine
    
    def map_learner(self, learner_id: str, profile_scores: List[tuple]) -> 'CognitiveAssetMap':
        """
        Map learner to cognitive assets based on profile scores.
        
        Args:
            learner_id: Unique learner identifier
            profile_scores: List of (profile, confidence) tuples from profile engine
        """
        if not profile_scores:
            return self._empty_map(learner_id)
        
        # Sort by confidence
        sorted_profiles = sorted(profile_scores, key=lambda x: -x[1])
        primary = sorted_profiles[0][0].value if sorted_profiles else "unknown"
        secondary = [p[0].value for p in sorted_profiles[1:3]]
        
        # Aggregate assets from all matching profiles
        all_assets = []
        for profile_enum, confidence in profile_scores:
            if confidence > 0.15:  # Threshold for inclusion
                assets = self.ASSET_MAP.get(profile_enum.value, [])
                for asset in assets:
                    asset_data = asset.copy()
                    asset_data["confidence"] = confidence
                    all_assets.append(asset_data)
        
        # Deduplicate by domain
        unique_assets = {}
        for asset in all_assets:
            key = asset["domain"]
            if key not in unique_assets or unique_assets[key]["confidence"] < asset["confidence"]:
                unique_assets[key] = asset
        
        assets_list = list(unique_assets.values())
        
        # Determine team role recommendations
        team_roles = self._recommend_team_roles(list(unique_assets.keys()))
        
        # Identify growth edges
        growth_edges = self._identify_growth_edges(list(unique_assets.keys()))
        
        # Identity bonus eligibility
        identity_bonus = len(unique_assets) >= 2  # Multiple cognitive assets
        
        return CognitiveAssetMap(
            learner_id=learner_id,
            primary_profile=primary,
            secondary_profiles=secondary,
            assets=list(unique_assets.values()),
            team_role_recommendations=team_roles,
            growth_edges=growth_edges,
            identity_bonus_eligible=identity_bonus
        )
    
    def _recommend_team_roles(self, domains: List[str]) -> List[str]:
        """Recommend team roles based on cognitive assets."""
        role_map = {
            "Pattern Discovery": "Pattern Seeker / Anomaly Detective",
            "Anomaly Detection": "Quality Guardian / Edge Case Hunter",
            "System Optimization": "Systems Architect / Optimizer",
            "Zero-Defect Design": "Quality Architect / Precision Engineer",
            "Novel Connections": "Innovation Catalyst / Cross-Pollinator",
            "Rapid Prototyping": "Prototype Accelerator / MVP Builder",
            "Boundary Pushing": "Innovation Provocateur / Assumption Challenger",
            "Crisis Creativity": "Crisis Response Lead / Firefighter",
            "Spatial Design": "Spatial Architect / UX Designer",
            "Systems Visualization": "Systems Visualizer / Data Storyteller",
            "Story Systems": "Narrative Designer / Science Communicator",
            "Cross-Domain Integration": "Integration Architect / Synthesis Lead",
            "Empathetic Design": "Empathy Champion / Inclusion Advocate",
            "Communication Systems": "Communication Architect / Translator",
            "Strategic Frameworks": "Strategic Architect / Vision Keeper"
        }
        
        return [domains.get(d, "Contributor") for d in domains if d in domains]
    
    def _identify_growth_edges(self, domains: List[str]) -> List[str]:
        """Identify growth edges based on current assets."""
        edges = []
        
        # If strong in discovery, grow in design
        if any("Discovery" in d or "Pattern" in d or "Anomaly" in d for d in domains):
            if not any("Design" in d or "Optimization" in d for d in domains):
                edges.append("Develop design/synthesis skills to complement discovery strengths")
        
        # If strong in design, grow in communication
        if any("Design" in d or "Optimization" in d for d in domains):
            if not any("Visualization" in d or "Story" in d or "Communication" in d for d in domains):
                edges.append("Develop communication/visualization to share designs")
        
        # If strong in strategy, grow in execution
        if any("Strategy" in d or "Framework" in d for d in domains):
            if not any("Prototyping" in d or "Rapid" in d for d in domains):
                edges.append("Develop rapid prototyping to test strategies")
        
        return edges
    
    def get_all_assets(self) -> List[Dict]:
        """Get all cognitive assets across all profiles."""
        all_assets = []
        for assets in self.ASSET_MAP.values():
            all_assets.extend(assets)
        return all_assets
    
    def get_assets_by_profile(self, profile: str) -> List[Dict]:
        return self.ASSET_MAP.get(profile, [])


class TeamCompositionEngine:
    """
    Recommends optimal team compositions based on cognitive asset maps.
    """
    
    ROLE_REQUIREMENTS = {
        "Pattern Seeker": ["Pattern Discovery", "Anomaly Detection"],
        "Innovation Catalyst": ["Novel Connections", "Boundary Pushing"],
        "Systems Architect": ["System Optimization", "Cross-Domain Integration"],
        "Prototype Accelerator": ["Rapid Prototyping", "Crisis Creativity"],
        "Spatial Architect": ["Spatial Design", "Systems Visualization"],
        "Narrative Designer": ["Story Systems", "Cross-Domain Integration"],
        "Empathy Champion": ["Empathetic Design", "Communication Systems"],
        "Strategic Architect": ["Strategic Frameworks", "Cross-Domain Integration"],
        "Quality Guardian": ["Anomaly Detection", "Zero-Defect Design"],
        "Inclusion Advocate": ["Empathetic Design", "Communication Systems"]
    }
    
    def __init__(self, asset_mapper: 'CognitiveAssetMapper'):
        self.asset_mapper = asset_mapper
    
    def compose_team(self, learners: List[Dict], required_roles: List[str] = None) -> Dict:
        """
        Compose optimal team from learners based on cognitive assets.
        
        Args:
            learners: List of {learner_id, profile_scores} dicts
            required_roles: Optional list of required team roles
            
        Returns:
            Team composition with role assignments
        """
        if required_roles is None:
            required_roles = list(self.ROLE_REQUIREMENTS.keys())
        
        # Map each learner to assets
        learner_assets = {}
        for learner in learners:
            learner_id = learner["id"]
            profile_scores = learner.get("profile_scores", [])
            asset_map = self.asset_mapper.map_learner(learner_id, profile_scores)
            learner_assets[learner_id] = asset_map
        
        # Greedy assignment: assign each role to best-fit learner
        assignments = {}
        assigned = set()
        
        # Sort roles by specificity (most specific first)
        sorted_roles = sorted(required_roles, key=lambda r: len(self.ROLE_REQUIREMENTS[r]))
        
        for role in sorted_roles:
            required_assets = self.ROLE_REQUIREMENTS[role]
            best_learner = None
            best_score = 0
            
            for learner_id, asset_map in learner_assets.items():
                if learner_id in assigned:
                    continue
                
                # Score learner for this role
                score = sum(1 for asset in asset_map.assets 
                           if asset["domain"] in required_assets)
                
                if score > best_score:
                    best_score = score
                    best_learner = learner_id
            
            if best_learner:
                assignments[role] = best_learner
                assigned.add(best_learner)
            else:
                assignments[role] = None
        
        return {
            "assignments": assignments,
            "unassigned_learners": [l for l in learner_assets if l not in assigned],
            "coverage": len([r for r in assignments if assignments[r]]) / len(required_roles)
        }
    
    def analyze_team_diversity(self, learners: List[Dict]) -> Dict:
        """Analyze cognitive diversity of a team."""
        all_assets = set()
        profile_coverage = set()
        
        for learner in learners:
            profile_scores = learner.get("profile_scores", [])
            for profile, _ in profile_scores:
                profile_coverage.add(profile[0].value if hasattr(profile[0], 'value') else profile[0])
            
            asset_map = self.asset_mapper.map_learner(learner["id"], profile_scores)
            for asset in asset_map.assets:
                all_assets.add(asset["domain"])
        
        return {
            "cognitive_diversity_score": len(profile_coverage) / 4,  # 4 core profiles
            "asset_diversity": len(all_assets),
            "profile_coverage": list(profile_coverage),
            "asset_coverage": list(all_assets),
            "recommendation": self._diversity_recommendation(profile_coverage, all_assets)
        }
    
    def _diversity_recommendation(self, profiles: set, assets: set) -> str:
        if len(profiles) >= 3 and len(assets) >= 8:
            return "Excellent cognitive diversity — team well-equipped for complex challenges"
        elif len(profiles) >= 2 and len(assets) >= 5:
            return "Good diversity — consider adding complementary profiles"
        else:
            return "Limited diversity — actively recruit complementary cognitive profiles"


class CognitiveAssetAPI:
    """API interface for cognitive asset mapping."""
    
    def __init__(self):
        self.mapper = CognitiveAssetMapper()
        self.team_engine = TeamCompositionEngine(self.mapper)
    
    def map_learner(self, learner_id: str, profile_scores: List[tuple]) -> Dict:
        """Map single learner to cognitive assets."""
        asset_map = self.mapper.map_learner(learner_id, profile_scores)
        return {
            "learner_id": asset_map.learner_id,
            "primary_profile": asset_map.primary_profile,
            "secondary_profiles": asset_map.secondary_profiles,
            "assets": [{"domain": a["domain"], "type": a["contribution_type"], 
                       "description": a["description"], "confidence": a.get("confidence", 1.0)}
                      for a in asset_map.assets],
            "team_roles": asset_map.team_role_recommendations,
            "growth_edges": asset_map.growth_edges,
            "identity_bonus_eligible": asset_map.identity_bonus_eligible
        }
    
    def compose_team(self, learners: List[Dict]) -> Dict:
        """Compose optimal team from learners."""
        return self.team_engine.compose_team(learners)
    
    def analyze_diversity(self, learners: List[Dict]) -> Dict:
        """Analyze team cognitive diversity."""
        return self.team_engine.analyze_team_diversity(learners)
    
    def get_all_assets(self) -> List[Dict]:
        """Get all available cognitive assets."""
        return self.mapper.get_all_assets()
    
    def get_assets_by_profile(self, profile: str) -> List[Dict]:
        """Get assets for a specific cognitive profile."""
        return self.mapper.get_assets_by_profile(profile)


if __name__ == "__main__":
    api = CognitiveAssetAPI()
    
    # Test mapping a learner
    learner = {
        "id": "learner_001",
        "profile_scores": [
            ("autistic", 0.6),
            ("adhd", 0.3),
            ("dyslexic", 0.1)
        ]
    }
    
    result = api.map_learner("learner_001", learner["profile_scores"])
    print("Learner Asset Map:")
    print(json.dumps(result, indent=2))
    
    # Test team composition
    team = [
        {"id": "learner_1", "profile_scores": [("autistic", 0.7), ("adhd", 0.2)]},
        {"id": "learner_2", "profile_scores": [("adhd", 0.6), ("dyslexic", 0.3)]},
        {"id": "learner_3", "profile_scores": [("dyslexic", 0.7), ("dyspraxic", 0.3)]},
        {"id": "learner_4", "profile_scores": [("dyspraxic", 0.8), ("autistic", 0.1)]}
    ]
    
    team_result = api.compose_team(team)
    print("\nTeam Composition:")
    print(json.dumps(team_result, indent=2))
    
    diversity = api.analyze_diversity(team)
    print("\nTeam Diversity Analysis:")
    print(json.dumps(diversity, indent=2))