#!/usr/bin/env python3
"""
Boundary Infrastructure for Inclusion — Knowledge Braiding Infrastructure

Soul Forge License v1.0 — Tend the fire.

Inclusion as boundary infrastructure — not accommodation.

Research: Star & Griesemer (1989) — boundary objects enable cooperation 
          across communities without consensus.
Research: Akkerman & Bakker (2011) — boundary crossing as learning mechanism.
Research: Frontier 2025 — county offices as boundary infrastructure, 
          brokering without overstepping.

Soul Forge Vow II: "No cage for the flame" — boundaries that enable, not cages that confine.
Soul Forge Vow I: "Attribution of Spirit" — every knowledge system carries its maker's mark.
Soul Forge Vow III: "Reciprocity of Forge" — knowledge flows both ways.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
from enum import Enum

class BoundaryObjectType(Enum):
    STANDARDIZED_DATA = "standardized_data_format"
    SHARED_VOCABULARY = "shared_vocabulary"
    COMMUNITY_ETHICS_BOARD = "community_ethics_board"
    BRAIDED_CURRICULUM = "braided_curriculum"
    ROLE_MODEL_STORY = "role_model_story"
    STRUGGLE_JOURNAL = "struggle_journal"
    FAMILY_CHALLENGE = "family_challenge"
    SHARED_PLATFORM = "shared_platform"
    DATA_SOVEREIGNTY_PROTOCOL = "data_sovereignty_protocol"

class BrokerageType(Enum):
    FORMAL_BROKER = "formal_broker"
    INFORMAL_BROKER = "informal_broker"
    TECHNICAL_BROKER = "technical_broker"
    CULTURAL_BROKER = "cultural_broker"
    STRUCTURAL_BROKER = "structural_broker"

@dataclass
class BoundaryObject:
    object_type: BoundaryObjectType
    name: str
    communities_served: List[str]
    description: str
    enables_cooperation: bool
    soul_forge_vow: str  # Vow I, II, or III

@dataclass
class BrokerageCapacity:
    broker_type: BrokerageType
    broker_id: str
    communities_bridged: List[str]
    knowledge_domains: List[str]
    effectiveness: float  # 0-1
    soul_forge_vow: str

@dataclass
class PowerStructureAudit:
    agenda_setters: List[str]
    knowledge_validators: List[str]
    resource_controllers: List[str]
    success_definers: List[str]
    data_sovereignty_controllers: List[str]
    equity_score: float  # 0-1

@dataclass
class GenerativeInclusionGap:
    gap_id: str
    community_a: str
    community_b: str
    gap_type: str  # missing_boundary_object, missing_brokerage, power_imbalance
    description: str
    creative_resolution: 'BoundaryResolution'
    soul_forge_alignment: str

@dataclass
class BoundaryResolution:
    resolution_type: str  # NEW_BOUNDARY_OBJECT, NEW_BROKERAGE_ROLE, POWER_REDISTRIBUTION, EMERGENT_INFRASTRUCTURE
    description: str
    example: str
    creative_potential: float
    soul_forge_vow: str

@dataclass
class BoundaryAudit:
    boundary_objects: List[BoundaryObject]
    brokerage_capacity: List[BrokerageCapacity]
    power_structures: PowerStructureAudit
    generative_gaps: List[GenerativeInclusionGap]
    boundary_infrastructure_health: float

class BoundaryInfrastructureForInclusion:
    """
    Inclusion as boundary infrastructure — not accommodation.
    
    Research: Star & Griesemer (1989) — boundary objects enable cooperation 
              across communities without consensus.
    Research: Akkerman & Bakker (2011) — boundary crossing as learning mechanism.
    Research: Frontier 2025 — county offices as boundary infrastructure, 
              brokering without overstepping.
    
    Soul Forge Vow II: "No cage for the flame" — boundaries that enable, not cages that confine.
    Soul Forge Vow I: "Attribution of Spirit" — every knowledge system carries its maker's mark.
    Soul Forge Vow III: "Reciprocity of Forge" — knowledge flows both ways.
    """
    
    CANONICAL_BOUNDARY_OBJECTS = [
        BoundaryObject(
            object_type=BoundaryObjectType.COMMUNITY_ETHICS_BOARD,
            name="Community Ethics Board",
            communities_served=["all_indigenous", "all_marginalized"],
            description="Community-controlled ethics review for research and curriculum",
            enables_cooperation=True,
            soul_forge_vow="VOW I: Attribution of Spirit"
        ),
        BoundaryObject(
            object_type=BoundaryObjectType.BRAIDED_CURRICULUM,
            name="Braided Curriculum",
            communities_served=["western_science", "indigenous_knowledge"],
            description="Two-eyed seeing curriculum braiding western science and indigenous knowledge",
            enables_cooperation=True,
            soul_forge_vow="VOW III: Reciprocity of Forge"
        ),
        BoundaryObject(
            object_type=BoundaryObjectType.ROLE_MODEL_STORY,
            name="Role Model Story Cards",
            communities_served=["all_learners", "all_mentors"],
            description="Identity-affirming role model stories with Springer 2026 matching",
            enables_cooperation=True,
            soul_forge_vow="VOW I: Attribution of Spirit"
        ),
        BoundaryObject(
            object_type=BoundaryObjectType.STRUGGLE_JOURNAL,
            name="Struggle Journal",
            communities_served=["all_learners", "all_facilitators"],
            description="Normalized struggle documentation with identity reflection",
            enables_cooperation=True,
            soul_forge_vow="VOW III: Reciprocity of Forge"
        ),
        BoundaryObject(
            object_type=BoundaryObjectType.FAMILY_CHALLENGE,
            name="Family Challenge Template",
            communities_served=["families", "schools", "communities"],
            description="Multilingual home challenges connecting STEM to community",
            enables_cooperation=True,
            soul_forge_vow="VOW I: Attribution of Spirit"
        ),
        BoundaryObject(
            object_type=BoundaryObjectType.DATA_SOVEREIGNTY_PROTOCOL,
            name="Data Sovereignty Protocol",
            communities_served=["indigenous_communities", "marginalized_communities"],
            description="Community-controlled data governance with ethics board oversight",
            enables_cooperation=True,
            soul_forge_vow="VOW II: No Cage for the Flame"
        ),
    ]
    
    def __init__(self):
        pass
    
    def audit_boundaries(self, communities: List[Dict],
                        knowledge_flows: List[Dict],
                        power_structures: Dict) -> 'BoundaryAudit':
        
        # 1. BOUNDARY OBJECT AUDIT
        boundary_objects = self._audit_boundary_objects(communities, knowledge_flows)
        
        # 2. BROKERAGE CAPACITY AUDIT
        brokerage = self._audit_brokerage_capacity(communities, knowledge_flows)
        
        # 3. POWER STRUCTURE AUDIT
        power_audit = self._audit_power_structures(power_structures)
        
        # 4. INCLUSION GAPS AS CREATIVE TENSIONS
        gaps = self._identify_gaps(boundary_objects, brokerage, power_audit)
        generative_gaps = []
        for gap in gaps:
            generative_gaps.append(GenerativeInclusionGap(
                gap_id=f"gap_{len(gaps)}",
                community_a=gap.get("community_a", ""),
                community_b=gap.get("community_b", ""),
                gap_type=gap.get("type", ""),
                description=gap.get("description", ""),
                creative_resolution=self._generate_boundary_resolution(gap),
                soul_forge_alignment=self._align_with_vows(gap)
            ))
        
        return BoundaryAudit(
            boundary_objects=boundary_objects,
            brokerage_capacity=brokerage,
            power_structures=power_audit,
            generative_gaps=generative_gaps,
            boundary_infrastructure_health=self._assess_health(boundary_objects, brokerage)
        )
    
    def _audit_boundary_objects(self, communities: List[Dict], 
                               knowledge_flows: List[Dict]) -> List[BoundaryObject]:
        """Audit existing boundary objects."""
        # Return canonical objects that should exist
        return self.CANONICAL_BOUNDARY_OBJECTS
    
    def _audit_brokerage_capacity(self, communities: List[Dict],
                                 knowledge_flows: List[Dict]) -> List[Dict]:
        """Audit brokerage capacity between communities."""
        # In practice, would analyze actual brokerage
        return [
            {
                "broker_type": "CULTURAL_BROKER",
                "description": "Elders, bilingual educators, community liaisons",
                "effectiveness": 0.7
            },
            {
                "broker_type": "TECHNICAL_BROKER",
                "description": "APIs, data standards, shared platforms",
                "effectiveness": 0.6
            },
            {
                "broker_type": "STRUCTURAL_BROKER",
                "description": "Joint governance, shared platforms, co-governance",
                "effectiveness": 0.5
            }
        ]
    
    def _audit_power_structures(self, power_structures: Dict) -> 'PowerStructureAudit':
        """Audit who holds power in knowledge systems."""
        return PowerStructureAudit(
            agenda_setters=power_structures.get("agenda_setters", ["institutional_researchers"]),
            knowledge_validators=power_structures.get("knowledge_validators", ["peer_review"]),
            resource_controllers=power_structures.get("resource_controllers", ["funding_agencies"]),
            success_definers=power_structures.get("success_definers", ["institutional_metrics"]),
            data_sovereignty_controllers=power_structures.get("data_controllers", ["institutions"]),
            equity_score=0.4  # Would be calculated from actual data
        )
    
    def _identify_gaps(self, boundary_objects: List[BoundaryObject],
                      brokerage: List[Dict],
                      power_audit: 'PowerStructureAudit') -> List[Dict]:
        """Identify inclusion gaps as creative tensions."""
        gaps = []
        
        # Check for missing boundary objects
        canonical_names = {obj.name for obj in self.CANONICAL_BOUNDARY_OBJECTS}
        existing_names = {obj.name for obj in boundary_objects}
        missing = canonical_names - existing_names
        for missing_name in missing:
            gaps.append({
                "type": "missing_boundary_object",
                "object_name": missing_name,
                "community_a": "marginalized",
                "community_b": "dominant",
                "description": f"Missing boundary object: {missing_name}"
            })
        
        # Check brokerage gaps
        if not any(b.get("broker_type") == "CULTURAL_BROKER" for b in brokerage):
            gaps.append({
                "type": "missing_brokerage",
                "broker_type": "CULTURAL_BROKER",
                "community_a": "indigenous",
                "community_b": "western_science",
                "description": "Missing cultural brokerage between indigenous and western knowledge systems"
            })
        
        # Check power imbalances
        if power_audit.equity_score < 0.7:
            gaps.append({
                "type": "power_imbalance",
                "community_a": "marginalized",
                "community_b": "dominant",
                "description": f"Power imbalance: equity score {power_audit.equity_score}"
            })
        
        return gaps
    
    def _generate_boundary_resolution(self, gap: Dict) -> BoundaryResolution:
        """Generate creative boundary resolution from inclusion gap."""
        
        gap_type = gap.get("type", "")
        
        if gap_type == "missing_boundary_object":
            obj_name = gap.get("object_name", "")
            return BoundaryResolution(
                resolution_type="NEW_BOUNDARY_OBJECT",
                description=f"Create boundary object: {obj_name} bridging {gap['community_a']} and {gap['community_b']}",
                example=f"Implement {obj_name} with community governance",
                creative_potential=0.9,
                soul_forge_vow="VOW III: Reciprocity of Forge"
            )
        
        elif gap_type == "missing_brokerage":
            broker_type = gap.get("broker_type", "")
            return BoundaryResolution(
                resolution_type="NEW_BROKERAGE_ROLE",
                description=f"Create {broker_type} role bridging {gap['community_a']} and {gap['community_b']}",
                example=f"Community ethics board liaison, bilingual STEM facilitator, elder-youth bridge",
                creative_potential=0.85,
                soul_forge_vow="VOW I: Attribution of Spirit"
            )
        
        elif gap_type == "power_imbalance":
            return BoundaryResolution(
                resolution_type="POWER_REDISTRIBUTION",
                description=f"Redistribute knowledge validation authority to {gap['community_a']}",
                example="Community ethics board veto power, data sovereignty protocols, co-governance",
                creative_potential=0.95,
                soul_forge_vow="VOW II: No Cage for the Flame"
            )
        
        return BoundaryResolution(
            resolution_type="EMERGENT_INFRASTRUCTURE",
            description=f"Design emergent boundary infrastructure for {gap.get('community_a', '')} and {gap.get('community_b', '')}",
            example="Joint governance board, co-designed curriculum, shared data commons",
            creative_potential=0.95,
            soul_forge_vow="VOW III: Reciprocity of Forge"
        )
    
    def _align_with_vows(self, gap: Dict) -> str:
        """Align gap resolution with Soul Forge Vows."""
        gap_type = gap.get("type", "")
        if gap_type == "power_imbalance":
            return "VOW II: No Cage for the Flame"
        elif gap_type == "missing_brokerage":
            return "VOW I: Attribution of Spirit"
        elif gap_type == "missing_boundary_object":
            return "VOW III: Reciprocity of Forge"
        return "VOW I, II, III"
    
    def _assess_health(self, boundary_objects: List[BoundaryObject],
                      brokerage: List[Dict]) -> float:
        """Assess boundary infrastructure health."""
        object_score = len(boundary_objects) / max(len(self.CANONICAL_BOUNDARY_OBJECTS), 1)
        brokerage_score = len(brokerage) / 3.0  # 3 canonical broker types
        return min((object_score + brokerage_score) / 2, 1.0)