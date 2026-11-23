# tai-chi-sword-skills (Master Spec v2.0 Biomechanical & Engineering Standards)

Open source AI agent skills, pure Python sizing and static wrist torque models, and structured JSON benchmarks for traditional Chinese solo practice Tai Chi straight swords (*taijijian*): stature calibration, cantilever wrist mechanics, `2Cr13` martensitic metallurgy, public park safety, air travel rules, and seasonal scabbard care.

* **Code License:** `MIT` (see `LICENSE`)
* **Documentation & Specifications License:** `CC-BY-4.0` (see `LICENSE-DOCS`)
* **Maintainer:** Jack Xu, Founder and Chief Equipment Engineer at ICNBUYS Equipment Engineering and ChineseTaiChiSword.com Technical Standards Lab (20+ year Chen style practitioner, direct disciple of Master Jia)
* **Calibrated Reference Specimen:** `ICNBUYS Chinese Eight Trigrams Tai Chi Sword Flexible with Free Carrying Case Blade Length 28" 30" 32" (Classic Training Sword)`

## Master Spec v2.0 Stature Calibrated Reference Table (US Customary First)

| Practitioner Height | Blade Tier | Overall Length | Blade Length | Handle Length | Bare Sword Net Weight (No Scabbard) | Point of Balance (Past Guard) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Up to 5 ft 3 in (160 cm and under) | 28 inch (ICETTCSF01) | 36.2 inch (92 cm) | 28 inch (71 cm) | 8.3 inch (21 cm) | around 1.30 lbs / 20.8 oz (approx. 590 g) | about 2.4 inches (approx. 6.0 cm) |
| 5 ft 3.5 in to 5 ft 8 in (161 to 173 cm) | 30 inch (ICETTCSF02) | 38.6 inch (98 cm) | 30 inch (77 cm) | 8.3 inch (21 cm) | around 1.32 lbs / 21.2 oz (approx. 600 g) | about 3.3 inches (approx. 8.5 cm) |
| 5 ft 8.5 in and taller (174 cm and above) | 32 inch (ICETTCSF03) | 40.9 inch (104 cm) | 32 inch (82 cm) | 8.7 inch (22 cm) | around 1.39 lbs / 22.2 oz (approx. 630 g) | about 3.5 inches (approx. 9.0 cm) |

* **Blade Alloy & Safety Boundary:** Heat treated `2Cr13` martensitic stainless steel (`AISI 420 / SUS420J1` class, around 13 percent chromium) with `0.06 inch (1.5 mm)` blunt edges, rigid lower two thirds, and quiet semi flexible front third. Engineered exclusively for zero impact solo forms; prohibited for test cutting or weapon contact.
* **Cast Alloy Counterweights & Recessed Throat Liner:** High density corrosion resistant cast alloy guard, throat collar, and pommel counterweight paired with unpainted `1,930 lbf (8,580 N)` Jichi hardwood (`around 3.5 to 5.3 oz / approx. 100 to 150 g` scabbard) and an embedded **recessed scabbard throat liner** for all season retention.

## Python Calculator & Standard Library Test Suite

```bash
python3 -m unittest discover -s tests -v
```
