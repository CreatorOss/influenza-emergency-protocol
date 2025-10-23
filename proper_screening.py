#!/usr/bin/env python3
import json

print("🔍 PROPER SCREENING OF 53,245 COMPOUNDS")
print("=" * 55)

def screen_compounds_properly():
    try:
        with open('my_chemical_database.json', 'r') as f:
            db = json.load(f)
        
        compounds = db.get('compounds', {})
        print(f"📊 Total compounds in database: {len(compounds):,}")
        
        # Count compounds with drug_score
        scored_compounds = 0
        high_score_candidates = []
        
        print("🎯 Screening compounds with drug scores...")
        
        for comp_id, comp_data in compounds.items():
            score = comp_data.get('drug_score')
            formula = comp_data.get('formula', '')
            
            if score is not None:  # Only count compounds with actual scores
                scored_compounds += 1
                
                if score > 0.7 and formula:
                    high_score_candidates.append({
                        'formula': formula,
                        'score': score,
                        'id': comp_id,
                        'session': comp_data.get('discovery_session', 'Unknown')
                    })
        
        print(f"📈 Compounds with drug scores: {scored_compounds:,}")
        print(f"🎯 High-score candidates (>0.7): {len(high_score_candidates)}")
        
        if high_score_candidates:
            # Sort by score
            high_score_candidates.sort(key=lambda x: x['score'], reverse=True)
            
            print(f"\n🏆 TOP 20 CANDIDATES (Score > 0.7):")
            for i, candidate in enumerate(high_score_candidates[:20], 1):
                print(f"   {i:2d}. {candidate['formula']:25} Score: {candidate['score']:.3f}")
                
                # Mark improvements
                if candidate['score'] > 0.85:
                    print("        💎 BREAKTHROUGH CANDIDATE! (>0.85)")
                elif candidate['score'] > 0.80:
                    print("        ⭐ EXCELLENT CANDIDATE! (>0.80)")
                elif candidate['score'] > 0.75:
                    print("        ✅ VERY GOOD CANDIDATE! (>0.75)")
            
            best_candidate = high_score_candidates[0]
            print(f"\n🎯 BEST CANDIDATE FOUND:")
            print(f"   Formula: {best_candidate['formula']}")
            print(f"   Score: {best_candidate['score']:.3f}")
            
            # Compare with original
            original_score = 0.721
            improvement = best_candidate['score'] - original_score
            print(f"   vs Original (0.721): {improvement:+.3f}")
            
            if improvement > 0:
                print("   ✅ IMPROVEMENT ACHIEVED!")
            else:
                print("   🔄 Similar performance, but more candidates")
            
            # Show score distribution
            print(f"\n📊 SCORE DISTRIBUTION:")
            ranges = {
                "0.90+": len([c for c in high_score_candidates if c['score'] >= 0.90]),
                "0.85-0.89": len([c for c in high_score_candidates if 0.85 <= c['score'] < 0.90]),
                "0.80-0.84": len([c for c in high_score_candidates if 0.80 <= c['score'] < 0.85]),
                "0.75-0.79": len([c for c in high_score_candidates if 0.75 <= c['score'] < 0.80]),
                "0.70-0.74": len([c for c in high_score_candidates if 0.70 <= c['score'] < 0.75])
            }
            
            for range_name, count in ranges.items():
                if count > 0:
                    print(f"   {range_name}: {count} candidates")
        
        else:
            print("❌ No high-score candidates found. Need to run drug screening.")
        
        return high_score_candidates
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return []

# Run proper screening
top_candidates = screen_compounds_properly()

if top_candidates:
    print(f"\n🚀 STRATEGIC RECOMMENDATIONS:")
    recommendations = [
        "1. PATENT multiple top candidates (not just one)",
        "2. CREATE development pipeline with best 3-5",
        "3. UPDATE investor pitch with portfolio approach", 
        "4. CONSIDER different mechanisms from various candidates",
        "5. PLAN combination therapies using multiple candidates"
    ]
    
    for rec in recommendations:
        print(f"   ✅ {rec}")
