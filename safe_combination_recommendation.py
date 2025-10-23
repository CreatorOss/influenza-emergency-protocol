#!/usr/bin/env python3
print("💊 REKOMENDASI KOMBINASI PALING AMAN")
print("=" * 55)

print("🎯 BERDASARKAN ANALISIS, REKOMENDASI KOMBINASI:")

safe_combinations = [
    {
        "name": "KOMBINASI AMAN 1: Ambroxol + Zinc + Vitamin B6",
        "target_elements": ["Br", "S", "Co-factor"],
        "components": [
            "Ambroxol 75mg (sumber Bromine)",
            "Zinc Sulfate 50mg (sumber Sulfur)", 
            "Vitamin B6 25mg (co-factor)"
        ],
        "dosage": "3x sehari setelah makan",
        "safety": "SANGAT AMAN - semua OTC",
        "cost": "Rp 50.000-75.000/bulan",
        "rationale": "Mendekati mekanisme senyawa Br-S-Cl kita"
    },
    {
        "name": "KOMBINASI AMAN 2: Ambroxol + Potassium Iodide", 
        "target_elements": ["Br", "I"],
        "components": [
            "Ambroxol 75mg (sumber Bromine)",
            "Potassium Iodide tablet (sumber Iodine)"
        ],
        "dosage": "2x sehari (pagi & sore)",
        "safety": "AMAN dengan monitoring tiroid",
        "cost": "Rp 60.000-80.000/bulan", 
        "rationale": "Meniru senyawa halogen combination"
    },
    {
        "name": "KOMBINASI AMAN 3: Standard Cold Medicine + Zinc",
        "target_elements": ["Multiple", "S"],
        "components": [
            "Obat flu standar (mengandung multiple elements)",
            "Zinc Sulfate 50mg (sumber Sulfur)"
        ],
        "dosage": "Sesuai petunjuk kemasan", 
        "safety": "SANGAT AMAN - terbukti klinis",
        "cost": "Rp 30.000-50.000/bulan",
        "rationale": "Pendekatan praktis dengan obat terbukti"
    }
]

for i, combo in enumerate(safe_combinations, 1):
    print(f"\n{i}. {combo['name']}")
    print(f"   🎯 Target Elements: {combo['target_elements']}")
    print(f"   💊 Components: {', '.join(combo['components'])}")
    print(f"   ⏰ Dosage: {combo['dosage']}")
    print(f"   🛡️ Safety: {combo['safety']}")
    print(f"   💰 Cost: {combo['cost']}")
    print(f"   🔬 Rationale: {combo['rationale']}")

print(f"\n⚠️  KONTRAINDIKASI DAN PERINGATAN:")
contraindications = [
    "Alergi terhadap komponen obat",
    "Gangguan ginjal atau hati berat",
    "Kehamilan dan menyusui (konsultasi dokter)",
    "Penyakit tiroid (untuk kombinasi dengan iodine)",
    "Sedang mengonsumsi obat pengencer darah"
]

for contra in contraindications:
    print(f"   🚫 {contra}")

print(f"\n🎯 PROTOCOL PENGGUNAAN:")
protocol = [
    "1. KONSULTASI DOKTER sebelum memulai",
    "2. START dengan dosis rendah", 
    "3. MONITOR gejala dan efek samping",
    "4. CATAT respons pengobatan",
    "5. HENTIKAN jika ada efek samping serius"
]

for step in protocol:
    print(f"   📋 {step}")

print(f"\n💡 REKOMENDASI UTAMA:")
print("   Gunakan KOMBINASI AMAN 1 (Ambroxol + Zinc + B6)")
print("   Paling aman, OTC, dan mendekati mekanisme senyawa kita")
