#!/usr/bin/env python3
print("🏥 CLINICAL MONITORING PROTOCOL")
print("=" * 55)

monitoring_protocol = {
    "vital_signs": {
        "frequency": "Daily during treatment",
        "parameters": [
            "Body Temperature",
            "Respiratory Rate", 
            "Oxygen Saturation (SpO2)",
            "Heart Rate"
        ]
    },
    "symptom_tracking": {
        "frequency": "Twice daily",
        "parameters": [
            "Fever (℃)",
            "Cough severity (1-10 scale)",
            "Sore throat (1-10 scale)", 
            "Nasal congestion (1-10 scale)",
            "Fatigue level (1-10 scale)",
            "Appetite changes"
        ]
    },
    "safety_monitoring": {
        "frequency": "Throughout treatment",
        "parameters": [
            "Gastrointestinal symptoms (nausea, diarrhea)",
            "Allergic reactions (rash, itching)",
            "Neurological symptoms (dizziness, headache)",
            "Renal function (urine output, color)"
        ]
    },
    "laboratory_parameters": {
        "frequency": "If available",
        "parameters": [
            "Complete Blood Count (CBC)",
            "Liver Function Tests (ALT, AST)",
            "Renal Function Tests (Creatinine)",
            "Inflammatory markers (CRP)"
        ]
    }
}

print("🔍 MONITORING PARAMETERS:")

for category, details in monitoring_protocol.items():
    print(f"\n📊 {category.replace('_', ' ').title()}:")
    print(f"   Frequency: {details['frequency']}")
    print(f"   Parameters:")
    for param in details['parameters']:
        print(f"      • {param}")

print(f"\n🎯 SUCCESS CRITERIA:")
success_criteria = [
    "Fever resolution within 48 hours",
    "Respiratory symptom improvement within 72 hours", 
    "Oxygen saturation maintained ≥95%",
    "No serious adverse events",
    "Return to normal activities within 5-7 days"
]

for criterion in success_criteria:
    print(f"   ✅ {criterion}")

print(f"\n⚠️  RED FLAGS (Stop treatment and consult doctor):")
red_flags = [
    "High fever (>39°C) persisting beyond 48 hours",
    "Difficulty breathing or shortness of breath",
    "Oxygen saturation dropping below 92%",
    "Severe allergic reaction (rash, swelling, breathing difficulty)",
    "Persistent vomiting or severe diarrhea",
    "Confusion or neurological symptoms"
]

for flag in red_flags:
    print(f"   🚨 {flag}")

print(f"\n📝 PATIENT DIARY TEMPLATE:")
diary_template = [
    "DATE: [Date]",
    "TIME: [Morning/Evening]", 
    "TEMPERATURE: ___°C",
    "SYMPTOM SCORES (1-10):",
    "  - Cough: ___",
    "  - Sore throat: ___",
    "  - Congestion: ___",
    "  - Fatigue: ___",
    "OXYGEN SATURATION: ___%",
    "NOTES: [Any side effects or improvements]"
]

for line in diary_template:
    print(f"   📄 {line}")
