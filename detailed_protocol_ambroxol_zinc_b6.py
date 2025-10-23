#!/usr/bin/env python3
print("💊 DETAILED PROTOCOL: AMBROXOL + ZINC + VITAMIN B6")
print("=" * 60)

protocol = {
    "combination_name": "Antiviral Combination Protocol",
    "target": "Influenza Type A Treatment & Prevention",
    "components": [
        {
            "drug": "Ambroxol HCl",
            "dose": "75mg",
            "purpose": "Bromine source + mucolytic action",
            "brand_examples": ["Mucosolvan", "Broxol", "Ambroxol"],
            "mechanism": "Provides Bromine atoms that may inhibit viral neuraminidase"
        },
        {
            "drug": "Zinc Sulfate", 
            "dose": "50mg (elemental zinc ~11mg)",
            "purpose": "Sulfur source + immune boosting",
            "brand_examples": ["Zincorin", "Zinc", "Zinc Sulfate"],
            "mechanism": "Provides Sulfur and enhances immune function against viruses"
        },
        {
            "drug": "Vitamin B6 (Pyridoxine)",
            "dose": "25mg", 
            "purpose": "Co-factor + metabolic support",
            "brand_examples": ["Pyridoxine", "Vitamin B6"],
            "mechanism": "Enhances immune cell function and drug metabolism"
        }
    ],
    "dosage_schedule": {
        "treatment": {
            "duration": "5-7 days",
            "schedule": [
                "After Breakfast: Ambroxol 75mg + Zinc 50mg + B6 25mg",
                "After Lunch: Ambroxol 75mg + Zinc 50mg",
                "After Dinner: Ambroxol 75mg + Zinc 50mg + B6 25mg"
            ]
        },
        "prevention": {
            "duration": "10-14 days during outbreak",
            "schedule": [
                "After Breakfast: Ambroxol 75mg + Zinc 50mg + B6 25mg", 
                "After Dinner: Ambroxol 75mg + Zinc 50mg + B6 25mg"
            ]
        }
    },
    "expected_timeline": {
        "symptom_improvement": "24-48 hours",
        "viral_clearance": "3-5 days", 
        "full_recovery": "5-7 days"
    }
}

print("🎯 PROTOCOL OVERVIEW:")
print(f"   Name: {protocol['combination_name']}")
print(f"   Target: {protocol['target']}")

print(f"\n💊 COMPONENTS DETAILS:")
for i, component in enumerate(protocol['components'], 1):
    print(f"   {i}. {component['drug']} {component['dose']}")
    print(f"      Purpose: {component['purpose']}")
    print(f"      Mechanism: {component['mechanism']}")
    print(f"      Brand Examples: {', '.join(component['brand_examples'])}")

print(f"\n⏰ DOSAGE SCHEDULE - TREATMENT (5-7 days):")
for schedule in protocol['dosage_schedule']['treatment']['schedule']:
    print(f"   ✅ {schedule}")

print(f"\n🛡️ DOSAGE SCHEDULE - PREVENTION (10-14 days):")
for schedule in protocol['dosage_schedule']['prevention']['schedule']:
    print(f"   ✅ {schedule}")

print(f"\n📊 EXPECTED OUTCOMES:")
for outcome, timeline in protocol['expected_timeline'].items():
    print(f"   • {outcome.replace('_', ' ').title()}: {timeline}")

print(f"\n🔬 SCIENTIFIC RATIONALE:")
rationale_points = [
    "Bromine from Ambroxol may bind to viral neuraminidase active site",
    "Sulfur from Zinc may interfere with viral entry mechanisms", 
    "Combination creates multi-target antiviral environment",
    "Vitamin B6 supports immune cell proliferation and function",
    "Mucolytic action helps clear respiratory secretions"
]

for point in rationale_points:
    print(f"   ✓ {point}")

print(f"\n💰 COST BREAKDOWN (1 month supply):")
costs = [
    "Ambroxol 75mg (90 tablets): Rp 25.000-35.000",
    "Zinc Sulfate (90 tablets): Rp 15.000-20.000",
    "Vitamin B6 25mg (60 tablets): Rp 10.000-15.000", 
    "Total: Rp 50.000-70.000 per month"
]

for cost in costs:
    print(f"   💵 {cost}")
